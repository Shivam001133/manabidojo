import io
import requests
from django.core.management.base import BaseCommand
from gtts import gTTS
from django.core.files.base import ContentFile
from manabhi_dojo.languages.models import Kanji


class Command(BaseCommand):
    help = "Import Kanji data and generate audio saved to R2 bucket."

    def add_arguments(self, parser):
        parser.add_argument(
            "-n",
            type=int,
            help="No of kanji words",
            default=30,
        )

    def generate_audio_for_kanji(self, kanji_obj):
        """Generates and uploads audio to kanji_audio/<character>.mp3 in R2."""
        try:
            tts = gTTS(text=kanji_obj.character, lang="ja")
            buffer = io.BytesIO()
            tts.write_to_fp(buffer)
            buffer.seek(0)

            filename = f"{kanji_obj.character}.mp3"
            upload_path = f"kanji_audio/{filename}"

            kanji_obj.audio.save(upload_path, ContentFile(buffer.read()))
            kanji_obj.save()
            self.stdout.write(f"🎵 Audio uploaded to: {kanji_obj.audio.name}")
        except Exception as e:  # noqa: BLE001
            self.stdout.write(
                self.style.WARNING(f"⚠️ Audio generation failed for {kanji_obj.character}: {e}")
            )

    def handle(self, *args, **kwargs):
        url = "https://raw.githubusercontent.com/davidluzgouveia/kanji-data/master/kanji.json"

        try:
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            kanji_data = response.json()
        except Exception as e:  # noqa: F401 BLE001 RUF100
            self.stdout.write(self.style.ERROR(f"❌ Failed to fetch Kanji data: {e}"))
            return

        added = 0
        skipped = 0
        no_of_words = kwargs["n"]

        for _ in range(no_of_words):
            for character, details in kanji_data.items():
                onyomi = ", ".join(details.get("readings_on", []))
                kunyomi = ", ".join(details.get("readings_kun", []))
                meaning = ", ".join(details.get("meanings", []))
                jlpt_level = details.get("jlpt_new")
                grade = details.get("grade")

                obj, created = Kanji.objects.get_or_create(
                    character=character,
                    defaults={
                        "onyomi": onyomi,
                        "kunyomi": kunyomi,
                        "meaning": meaning,
                        "jlpt_level": jlpt_level,
                        "grade": grade,
                    },
                )

                if created or not obj.audio:
                    self.generate_audio_for_kanji(obj)
                    self.stdout.write(f"✓ Added + Audio: {character}")
                    added += 1
                else:
                    self.stdout.write(f"⏭ Skipped (exists): {character}")
                    skipped += 1

        self.stdout.write(self.style.SUCCESS(f"✅ Finished: {added} added, {skipped} skipped."))

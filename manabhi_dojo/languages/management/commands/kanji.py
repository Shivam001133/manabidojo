import os
import requests
from django.core.management.base import BaseCommand
from django.conf import settings
from manabhi_dojo.languages.models import Kanji

class Command(BaseCommand):
    help = "Import Kanji data from the updated dataset into kanji_master table with optional audio"

    def handle(self, *args, **kwargs):
        url = "https://raw.githubusercontent.com/davidluzgouveia/kanji-data/master/kanji.json"
        try:
            response = requests.get(url)
            response.raise_for_status()
            kanji_data = response.json()
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"❌ Error fetching or parsing JSON: {e}"))
            return

        media_root = getattr(settings, 'MEDIA_ROOT', 'media')
        audio_dir = os.path.join(media_root, "kanji_audio")
        os.makedirs(audio_dir, exist_ok=True)

        added = 0
        for character, details in kanji_data.items():
            # Extract relevant details
            onyomi = ', '.join(details.get("readings_on", []))
            kunyomi = ', '.join(details.get("readings_kun", []))
            meaning = ', '.join(details.get("meanings", []))
            jlpt_level = details.get("jlpt_new")
            grade = details.get("grade")
            stroke_count = details.get("strokes")

            # Simulate audio file path
            audio_filename = f"{character}.mp3"
            audio_path = os.path.join("kanji_audio", audio_filename)

            try:
                obj, created = Kanji.objects.get_or_create(
                    character=character,
                    defaults={
                        "onyomi": onyomi,
                        "kunyomi": kunyomi,
                        "meaning": meaning,
                        "jlpt_level": jlpt_level,
                        "grade": grade,
                        "stroke_count": stroke_count,
                        "audio": audio_path
                    }
                )

                if created:
                    added += 1
                self.stdout.write(self.style.SUCCESS(f"✅ Successfully ->{added} added for {obj} Kanji.   "))

            except Exception as e:
                self.stdout.write(self.style.WARNING(f"⚠️ Could not add {character}: {e}"))

        self.stdout.write(self.style.SUCCESS(f"✅ Successfully added {added} Kanji to kanji_master table."))

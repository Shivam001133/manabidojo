from django.core.management.base import BaseCommand
from manabhi_dojo.languages.models import LanguageScript, Character
from gtts import gTTS
from django.core.files.base import ContentFile
import io


class Command(BaseCommand):
    help = "Seed all 46 basic Hiragana characters into the database and generate audio"

    def generate_audio_for_character(self, character):
        tts = gTTS(text=character.symbol, lang="ja")
        buffer = io.BytesIO()
        tts.write_to_fp(buffer)
        buffer.seek(0)

        filename = f"{character.romaji}.mp3"
        character.audio.save(filename, ContentFile(buffer.read()))
        character.save()
        self.stdout.write(f"🎵 Audio uploaded: {character.audio.name}")

    def handle(self, *args, **kwargs):
        script, created = LanguageScript.objects.get_or_create(
            name="hiragana",
            defaults={
                "title": "Hiragana Script",
                "description": "Basic Japanese phonetic script used primarily for native words."
            }
        )

        characters = [
            {"symbol": "あ", "romaji": "a", "example_word": "あめ (ame - rain)"},
            {"symbol": "い", "romaji": "i", "example_word": "いぬ (inu - dog)"},
            {"symbol": "う", "romaji": "u", "example_word": "うみ (umi - sea)"},
            {"symbol": "え", "romaji": "e", "example_word": "えき (eki - station)"},
            {"symbol": "お", "romaji": "o", "example_word": "おちゃ (ocha - tea)"},
            {"symbol": "か", "romaji": "ka", "example_word": "かさ (kasa - umbrella)"},
            {"symbol": "き", "romaji": "ki", "example_word": "きつね (kitsune - fox)"},
            {"symbol": "く", "romaji": "ku", "example_word": "くも (kumo - cloud)"},
            {"symbol": "け", "romaji": "ke", "example_word": "けむし (kemushi - caterpillar)"},
            {"symbol": "こ", "romaji": "ko", "example_word": "こども (kodomo - child)"},
            {"symbol": "さ", "romaji": "sa", "example_word": "さかな (sakana - fish)"},
            {"symbol": "し", "romaji": "shi", "example_word": "しろ (shiro - white)"},
            {"symbol": "す", "romaji": "su", "example_word": "すし (sushi)"},
            {"symbol": "せ", "romaji": "se", "example_word": "せかい (sekai - world)"},
            {"symbol": "そ", "romaji": "so", "example_word": "そら (sora - sky)"},
            {"symbol": "た", "romaji": "ta", "example_word": "たまご (tamago - egg)"},
            {"symbol": "ち", "romaji": "chi", "example_word": "ちず (chizu - map)"},
            {"symbol": "つ", "romaji": "tsu", "example_word": "つき (tsuki - moon)"},
            {"symbol": "て", "romaji": "te", "example_word": "てがみ (tegami - letter)"},
            {"symbol": "と", "romaji": "to", "example_word": "とり (tori - bird)"},
            {"symbol": "な", "romaji": "na", "example_word": "なつ (natsu - summer)"},
            {"symbol": "に", "romaji": "ni", "example_word": "にほん (nihon - Japan)"},
            {"symbol": "ぬ", "romaji": "nu", "example_word": "ぬの (nuno - cloth)"},
            {"symbol": "ね", "romaji": "ne", "example_word": "ねこ (neko - cat)"},
            {"symbol": "の", "romaji": "no", "example_word": "のう (nou - brain)"},
            {"symbol": "は", "romaji": "ha", "example_word": "はな (hana - flower/nose)"},
            {"symbol": "ひ", "romaji": "hi", "example_word": "ひと (hito - person)"},
            {"symbol": "ふ", "romaji": "fu", "example_word": "ふね (fune - ship)"},
            {"symbol": "へ", "romaji": "he", "example_word": "へや (heya - room)"},
            {"symbol": "ほ", "romaji": "ho", "example_word": "ほし (hoshi - star)"},
            {"symbol": "ま", "romaji": "ma", "example_word": "まど (mado - window)"},
            {"symbol": "み", "romaji": "mi", "example_word": "みず (mizu - water)"},
            {"symbol": "む", "romaji": "mu", "example_word": "むし (mushi - insect)"},
            {"symbol": "め", "romaji": "me", "example_word": "めがね (megane - glasses)"},
            {"symbol": "も", "romaji": "mo", "example_word": "もり (mori - forest)"},
            {"symbol": "や", "romaji": "ya", "example_word": "やま (yama - mountain)"},
            {"symbol": "ゆ", "romaji": "yu", "example_word": "ゆき (yuki - snow)"},
            {"symbol": "よ", "romaji": "yo", "example_word": "よる (yoru - night)"},
            {"symbol": "ら", "romaji": "ra", "example_word": "らいおん (raion - lion)"},
            {"symbol": "り", "romaji": "ri", "example_word": "りす (risu - squirrel)"},
            {"symbol": "る", "romaji": "ru", "example_word": "るす (rusu - absence)"},
            {"symbol": "れ", "romaji": "re", "example_word": "れいぞうこ (reizouko - fridge)"},
            {"symbol": "ろ", "romaji": "ro", "example_word": "ろうそく (rousoku - candle)"},
            {"symbol": "わ", "romaji": "wa", "example_word": "わに (wani - crocodile)"},
            {"symbol": "を", "romaji": "wo", "example_word": "を - particle (direct object marker)"},
            {"symbol": "ん", "romaji": "n", "example_word": "ほん (hon - book)"}
        ]

        for char in characters:
            obj, created = Character.objects.get_or_create(
                script=script,
                symbol=char["symbol"],
                defaults={
                    "romaji": char["romaji"],
                    "example_word": char["example_word"],
                    "meaning": None
                }
            )
            if created or not obj.audio:
                self.generate_audio_for_character(obj)
                self.stdout.write(f"✓ Added + Audio: {char['symbol']} ({char['romaji']})")
            else:
                self.stdout.write(f"⏭ Skipped (already exists): {char['symbol']} ({char['romaji']})")

        self.stdout.write(self.style.SUCCESS("✅ Hiragana characters seeded and audio generated!"))

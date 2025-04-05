from django.core.management.base import BaseCommand
from manabhi_dojo.languages.models import Character, LanguageScript, TypeScriptCharacter
from gtts import gTTS
from django.core.files.base import ContentFile
import io
from os import path

class Command(BaseCommand):
    help = "Seed all 46 basic Hiragana characters into the database and generate audio"

    def generate_audio_for_character(self, character):
        """
        Generates and saves audio for a given character using gTTS.
        """
        filename = f"{character.romaji}.mp3"

        # Check if the character already has an audio file associated
        if character.audio:
            self.stdout.write(f"🎵 Audio file already exists: {character.audio.name}")
            return 
        
        # Generate the audio
        tts = gTTS(text=character.symbol, lang="ja")
        buffer = io.BytesIO()
        tts.write_to_fp(buffer)
        buffer.seek(0)

        # Save the generated audio file
        character.audio.save(filename, ContentFile(buffer.read()))
        character.save()

        self.stdout.write(f"🎵 Audio uploaded: {character.audio.name}")

    def get_script_data(self):
        """
        Returns the data for the basic Hiragana characters.
        """
        main_list = [
            {"symbol": "あ", "romaji": "a", "example_word": "あめ (ame - rain)"},
            {"symbol": "い", "romaji": "i", "example_word": "いぬ (inu - dog)"},
            {"symbol": "う", "romaji": "u", "example_word": "うみ (umi - sea)"},
            {"symbol": "え", "romaji": "e", "example_word": "えき (eki - station)"},
            {"symbol": "お", "romaji": "o", "example_word": "おちゃ (ocha - tea)"},
            {"symbol": "か", "romaji": "ka", "example_word": "かさ (kasa - umbrella)"},
            {"symbol": "き", "romaji": "ki", "example_word": "きつね (kitsune - fox)"},
            {"symbol": "く", "romaji": "ku", "example_word": "くも (kumo - cloud)"},
            {
                "symbol": "け",
                "romaji": "ke",
                "example_word": "けむし (kemushi - caterpillar)",
            },
            {"symbol": "こ", "romaji": "ko", "example_word": "こども (kodomo - child)"},
            {"symbol": "さ", "romaji": "sa", "example_word": "さかな (sakana - fish)"},
            {"symbol": "し", "romaji": "shi", "example_word": "しろ (shiro - white)"},
            {"symbol": "す", "romaji": "su", "example_word": "すし (sushi)"},
            {"symbol": "せ", "romaji": "se", "example_word": "せかい (sekai - world)"},
            {"symbol": "そ", "romaji": "so", "example_word": "そら (sora - sky)"},
            {"symbol": "た", "romaji": "ta", "example_word": "たまご (tamago - egg)"},
            {"symbol": "ち", "romaji": "chi", "example_word": "ちず (chizu - map)"},
            {"symbol": "つ", "romaji": "tsu", "example_word": "つき (tsuki - moon)"},
            {
                "symbol": "て",
                "romaji": "te",
                "example_word": "てがみ (tegami - letter)",
            },
            {"symbol": "と", "romaji": "to", "example_word": "とり (tori - bird)"},
            {"symbol": "な", "romaji": "na", "example_word": "なつ (natsu - summer)"},
            {"symbol": "に", "romaji": "ni", "example_word": "にほん (nihon - Japan)"},
            {"symbol": "ぬ", "romaji": "nu", "example_word": "ぬの (nuno - cloth)"},
            {"symbol": "ね", "romaji": "ne", "example_word": "ねこ (neko - cat)"},
            {"symbol": "の", "romaji": "no", "example_word": "のう (nou - brain)"},
            {
                "symbol": "は",
                "romaji": "ha",
                "example_word": "はな (hana - flower/nose)",
            },
            {"symbol": "ひ", "romaji": "hi", "example_word": "ひと (hito - person)"},
            {"symbol": "ふ", "romaji": "fu", "example_word": "ふね (fune - ship)"},
            {"symbol": "へ", "romaji": "he", "example_word": "へや (heya - room)"},
            {"symbol": "ほ", "romaji": "ho", "example_word": "ほし (hoshi - star)"},
            {"symbol": "ま", "romaji": "ma", "example_word": "まど (mado - window)"},
            {"symbol": "み", "romaji": "mi", "example_word": "みず (mizu - water)"},
            {"symbol": "む", "romaji": "mu", "example_word": "むし (mushi - insect)"},
            {
                "symbol": "め",
                "romaji": "me",
                "example_word": "めがね (megane - glasses)",
            },
            {"symbol": "も", "romaji": "mo", "example_word": "もり (mori - forest)"},
            {"symbol": "や", "romaji": "ya", "example_word": "やま (yama - mountain)"},
            {"symbol": "ゆ", "romaji": "yu", "example_word": "ゆき (yuki - snow)"},
            {"symbol": "よ", "romaji": "yo", "example_word": "よる (yoru - night)"},
            {"symbol": "ら", "romaji": "ra", "example_word": "らいおん (raion - lion)"},
            {"symbol": "り", "romaji": "ri", "example_word": "りす (risu - squirrel)"},
            {"symbol": "る", "romaji": "ru", "example_word": "るす (rusu - absence)"},
            {
                "symbol": "れ",
                "romaji": "re",
                "example_word": "れいぞうこ (reizouko - fridge)",
            },
            {
                "symbol": "ろ",
                "romaji": "ro",
                "example_word": "ろうそく (rousoku - candle)",
            },
            {"symbol": "わ", "romaji": "wa", "example_word": "わに (wani - crocodile)"},
            {
                "symbol": "を",
                "romaji": "wo",
                "example_word": "を - particle (direct object marker)",
            },
            {"symbol": "ん", "romaji": "n", "example_word": "ほん (hon - book)"},
        ]

        dakuten = [
            {"symbol": "が", "romaji": "ga", "example_word": "がく (gaku - study)"},
            {"symbol": "ぎ", "romaji": "gi", "example_word": "ぎんこう (ginkou - bank)"},
            {"symbol": "ぐ", "romaji": "gu", "example_word": "ぐあい (guai - condition)"},
            {"symbol": "げ", "romaji": "ge", "example_word": "げんき (genki - healthy)"},
            {"symbol": "ご", "romaji": "go", "example_word": "ごはん (gohan - rice/meal)"},
            {"symbol": "ざ", "romaji": "za", "example_word": "ざっし (zasshi - magazine)"},
            {"symbol": "じ", "romaji": "ji", "example_word": "じてんしゃ (jitensha - bicycle)"},
            {"symbol": "ず", "romaji": "zu", "example_word": "ずっと (zutto - forever)"},
            {"symbol": "ぜ", "romaji": "ze", "example_word": "ぜんぶ (zenbu - everything)"},
            {"symbol": "ぞ", "romaji": "zo", "example_word": "ぞう (zou - elephant)"},
            {"symbol": "だ", "romaji": "da", "example_word": "だいがく (daigaku - university)"},
            {"symbol": "ぢ", "romaji": "ji", "example_word": "ぢかん (jikan - time)"},
            {"symbol": "づ", "romaji": "zu", "example_word": "づけもの (dzukemono - pickles)"},
            {"symbol": "で", "romaji": "de", "example_word": "できる (dekiru - can)"},
            {"symbol": "ど", "romaji": "do", "example_word": "どうぞ (douzo - please)"},
            {"symbol": "ば", "romaji": "ba", "example_word": "ばしょ (basho - place)"},
            {"symbol": "び", "romaji": "bi", "example_word": "びょういん (byouin - hospital)"},
            {"symbol": "ぶ", "romaji": "bu", "example_word": "ぶた (buta - pig)"},
            {"symbol": "べ", "romaji": "be", "example_word": "べんきょう (benkyou - study)"},
            {"symbol": "ぼ", "romaji": "bo", "example_word": "ぼうし (boushi - hat)"},
        ]

        handakuten = [
            {"symbol": "ぱ", "romaji": "pa", "example_word": "ぱん (pan - bread)"},
            {"symbol": "ぴ", "romaji": "pi", "example_word": "ぴあの (piano)"},
            {"symbol": "ぷ", "romaji": "pu", "example_word": "ぷーる (puuru - pool)"},
            {"symbol": "ぺ", "romaji": "pe", "example_word": "ぺん (pen - pen)"},
            {"symbol": "ぽ", "romaji": "po", "example_word": "ぽけっと (poketto - pocket)"},
        ]

        yoon = [
            {"symbol": "きゃ", "romaji": "kya", "example_word": "きゃく (kyaku - guest)"},
            {"symbol": "きゅ", "romaji": "kyu", "example_word": "きゅう (kyuu - nine)"},
            {"symbol": "きょ", "romaji": "kyo", "example_word": "きょう (kyou - today)"},
            {"symbol": "しゃ", "romaji": "sha", "example_word": "しゃしん (shashin - photo)"},
            {"symbol": "しゅ", "romaji": "shu", "example_word": "しゅくだい (shukudai - homework)"},
            {"symbol": "しょ", "romaji": "sho", "example_word": "しょうがっこう (shougakkou - elementary school)"},
            {"symbol": "ちゃ", "romaji": "cha", "example_word": "ちゃわん (chawan - bowl)"},
            {"symbol": "ちゅ", "romaji": "chu", "example_word": "ちゅうごく (chuugoku - China)"},
            {"symbol": "ちょ", "romaji": "cho", "example_word": "ちょうちょう (chouchou - butterfly)"},
            {"symbol": "ぢゃ", "romaji": "dya", "example_word": "ぢゃんけん (janken - rock-paper-scissors)"},
            {"symbol": "ぢゅ", "romaji": "dyu", "example_word": "ぢゅう (juu - ten)"},
            {"symbol": "ぢょ", "romaji": "dyo", "example_word": "ぢょう (jou - situation)"},
            {"symbol": "にゃ", "romaji": "nya", "example_word": "にゃんこ (nyanko - cat)"},
            {"symbol": "にゅ", "romaji": "nyu", "example_word": "にゅうりょく (nyuuryoku - input)"},
            {"symbol": "にょ", "romaji": "nyo", "example_word": "にょき (nyoki - growth)"},
            {"symbol": "ひゃ", "romaji": "hya", "example_word": "ひゃく (hyaku - hundred)"},
            {"symbol": "ひゅ", "romaji": "hyu", "example_word": "ひゅうが (hyuuga - the sun)"},
            {"symbol": "ひょ", "romaji": "hyo", "example_word": "ひょう (hyou - leopard)"},
            {"symbol": "みゃ", "romaji": "mya", "example_word": "みゃく (myaku - pulse)"},
            {"symbol": "みゅ", "romaji": "myu", "example_word": "みゅう (myuu - music)"},
            {"symbol": "みょ", "romaji": "myo", "example_word": "みょう (myou - unusual)"},
            {"symbol": "りゃ", "romaji": "rya", "example_word": "りゃく (ryaku - abbreviation)"},
            {"symbol": "りゅ", "romaji": "ryu", "example_word": "りゅう (ryuu - dragon)"},
            {"symbol": "りょ", "romaji": "ryo", "example_word": "りょう (ryou - fee)"},
            {"symbol": "ぎゃ", "romaji": "gya", "example_word": "ぎゃく (gyaku - reverse)"},
            {"symbol": "ぎゅ", "romaji": "gyu", "example_word": "ぎゅうにく (gyuuniku - beef)"},
            {"symbol": "ぎょ", "romaji": "gyo", "example_word": "ぎょう (gyou - business)"},
            {"symbol": "ぴゃ", "romaji": "pya", "example_word": "ぴゃく (pyaku - hundred)"},
            {"symbol": "ぴゅ", "romaji": "pyu", "example_word": "ぴゅう (pyuu - sound of wind)"},
            {"symbol": "ぴょ", "romaji": "pyo", "example_word": "ぴょう (pyou - calculation)"},
        ]

        return [
            (main_list, TypeScriptCharacter.NONE),
            (dakuten, TypeScriptCharacter.DAKUTEN),
            (handakuten, TypeScriptCharacter.HANDAKUTEN),
            (yoon, TypeScriptCharacter.Yoon)
        ]


    def insert_to_db(self, script, script_type):
        """
        Inserts characters into the database and generates audio if necessary.
        """
        characters_to_create = []
        for order_val, character in enumerate(script):
            obj, created = Character.objects.get_or_create(
                script=LanguageScript.HIRAGANA,
                symbol=character["symbol"],
                script_type=script_type,
                order=order_val,
                defaults={
                    "romaji": character["romaji"],
                    "example_word": character["example_word"],
                },
            )
            if created or not obj.audio:
                # Collect objects for audio generation
                characters_to_create.append(obj)
            else:
                self.stdout.write(
                    f"⏭ Skipped (already exists): {character['symbol']} ({character['romaji']})"
                )

        # Bulk update characters with audio generation
        for character in characters_to_create:
            self.generate_audio_for_character(character)

        self.stdout.write(
            self.style.SUCCESS("✅ Hiragana characters seeded and audio generated!")
        )

    def handle(self, *args, **kwargs):
        # Insert Hiragana characters
        script_list = self.get_script_data()
        for data in script_list:
            self.insert_to_db(script=data[0], script_type=data[1])

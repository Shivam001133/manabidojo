from django.core.management.base import BaseCommand
from manabhi_dojo.languages.models import Character, LanguageScript, TypeScriptCharacter
from django.core.files.base import ContentFile
from gtts import gTTS
import io


class Command(BaseCommand):
    help = "Seed all 46 basic Katakana characters into the database and generate audio"

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
        Returns the data for the basic Katakana characters including Dakuten, Handakuten,
        and Yoon variations.
        """
        katakana_main_list = [
            {
                "symbol": "ア",
                "romaji": "a",
                "example_word": "アイス (aisu - ice cream)",
            },
            {"symbol": "イ", "romaji": "i", "example_word": "インク (inku - ink)"},
            {"symbol": "ウ", "romaji": "u", "example_word": "ウサギ (usagi - rabbit)"},
            {"symbol": "エ", "romaji": "e", "example_word": "エビ (ebi - shrimp)"},
            {
                "symbol": "オ",
                "romaji": "o",
                "example_word": "オレンジ (orenji - orange)",
            },
            {
                "symbol": "カ",
                "romaji": "ka",
                "example_word": "カメラ (kamera - camera)",
            },
            {
                "symbol": "キ",
                "romaji": "ki",
                "example_word": "キリン (kirin - giraffe)",
            },
            {"symbol": "ク", "romaji": "ku", "example_word": "クマ (kuma - bear)"},
            {"symbol": "ケ", "romaji": "ke", "example_word": "ケーキ (keeki - cake)"},
            {
                "symbol": "コ",
                "romaji": "ko",
                "example_word": "コーヒー (koohii - coffee)",
            },
            {"symbol": "サ", "romaji": "sa", "example_word": "サラダ (sarada - salad)"},
            {
                "symbol": "シ",
                "romaji": "shi",
                "example_word": "シーツ (shiitsu - sheets)",
            },
            {
                "symbol": "ス",
                "romaji": "su",
                "example_word": "スイカ (suika - watermelon)",
            },
            {
                "symbol": "セ",
                "romaji": "se",
                "example_word": "セーター (seetaa - sweater)",
            },
            {"symbol": "ソ", "romaji": "so", "example_word": "ソファ (sofa - sofa)"},
            {"symbol": "タ", "romaji": "ta", "example_word": "タコ (tako - octopus)"},
            {
                "symbol": "チ",
                "romaji": "chi",
                "example_word": "チーズ (chiizu - cheese)",
            },
            {"symbol": "ツ", "romaji": "tsu", "example_word": "ツナ (tsuna - tuna)"},
            {
                "symbol": "テ",
                "romaji": "te",
                "example_word": "テレビ (terebi - television)",
            },
            {"symbol": "ト", "romaji": "to", "example_word": "トマト (tomato)"},
            {"symbol": "ナ", "romaji": "na", "example_word": "ナス (nasu - eggplant)"},
            {
                "symbol": "ニ",
                "romaji": "ni",
                "example_word": "ニンジン (ninjin - carrot)",
            },
            {
                "symbol": "ヌ",
                "romaji": "nu",
                "example_word": "ヌードル (nuudoru - noodles)",
            },
            {
                "symbol": "ネ",
                "romaji": "ne",
                "example_word": "ネックレス (nekkuresu - necklace)",
            },
            {
                "symbol": "ノ",  # noqa: RUF001
                "romaji": "no",
                "example_word": "ノート (nooto - notebook)",
            },
            {
                "symbol": "ハ",
                "romaji": "ha",
                "example_word": "ハサミ (hasami - scissors)",
            },
            {
                "symbol": "ヒ",
                "romaji": "hi",
                "example_word": "ヒツジ (hitsuji - sheep)",
            },
            {
                "symbol": "フ",
                "romaji": "fu",
                "example_word": "フルーツ (furuutsu - fruits)",
            },
            {"symbol": "ヘ", "romaji": "he", "example_word": "ヘアー (heaa - hair)"},
            {"symbol": "ホ", "romaji": "ho", "example_word": "ホテル (hoteru - hotel)"},
            {"symbol": "マ", "romaji": "ma", "example_word": "マスク (masuku - mask)"},
            {"symbol": "ミ", "romaji": "mi", "example_word": "ミルク (miruku - milk)"},
            {"symbol": "ム", "romaji": "mu", "example_word": "ムシ (mushi - insect)"},
            {
                "symbol": "メ",
                "romaji": "me",
                "example_word": "メガネ (megane - glasses)",
            },
            {"symbol": "モ", "romaji": "mo", "example_word": "モモ (momo - peach)"},
            {
                "symbol": "ヤ",
                "romaji": "ya",
                "example_word": "ヤサイ (yasai - vegetable)",
            },
            {"symbol": "ユ", "romaji": "yu", "example_word": "ユキ (yuki - snow)"},
            {"symbol": "ヨ", "romaji": "yo", "example_word": "ヨット (yotto - yacht)"},
            {
                "symbol": "ラ",
                "romaji": "ra",
                "example_word": "ラーメン (raamen - ramen)",
            },
            {"symbol": "リ", "romaji": "ri", "example_word": "リス (risu - squirrel)"},
            {"symbol": "ル", "romaji": "ru", "example_word": "ルール (ruuru - rule)"},
            {"symbol": "レ", "romaji": "re", "example_word": "レモン (remon - lemon)"},
            {
                "symbol": "ロ",
                "romaji": "ro",
                "example_word": "ロボット (robotto - robot)",
            },
            {"symbol": "ワ", "romaji": "wa", "example_word": "ワイン (wain - wine)"},
            {
                "symbol": "ヲ",
                "romaji": "wo",
                "example_word": "ヲ - particle (rare use)",
            },
            {"symbol": "ン", "romaji": "n", "example_word": "パン (pan - bread)"},
        ]

        dakuten = [
            {"symbol": "ガ", "romaji": "ga", "example_word": "ガク (gaku - study)"},
            {"symbol": "ギ", "romaji": "gi", "example_word": "ギンコウ (ginkou - bank)"},
            {"symbol": "グ", "romaji": "gu", "example_word": "グアイ (guai - condition)"},
            {"symbol": "ゲ", "romaji": "ge", "example_word": "ゲンキ (genki - healthy)"},
            {"symbol": "ゴ", "romaji": "go", "example_word": "ゴハン (gohan - meal/rice)"},
            {"symbol": "ザ", "romaji": "za", "example_word": "ザッシ (zasshi - magazine)"},
            {"symbol": "ジ", "romaji": "ji", "example_word": "ジテンシャ (jitensha - bicycle)"},
            {"symbol": "ズ", "romaji": "zu", "example_word": "ズッキーニ (zukkiini - zucchini)"},
            {"symbol": "ゼ", "romaji": "ze", "example_word": "ゼンブ (zenbu - everything)"},
            {"symbol": "ゾ", "romaji": "zo", "example_word": "ゾウ (zou - elephant)"},
            {"symbol": "ダ", "romaji": "da", "example_word": "ダイガク (daigaku - university)"},
            {"symbol": "ヂ", "romaji": "ji", "example_word": "ヂカン (jikan - time)"},
            {"symbol": "ヅ", "romaji": "zu", "example_word": "ヅケモノ (dzukemono - pickles)"},
            {"symbol": "デ", "romaji": "de", "example_word": "デキル (dekiru - can)"},
            {"symbol": "ド", "romaji": "do", "example_word": "ドウゾ (douzo - please)"},
            {"symbol": "バ", "romaji": "ba", "example_word": "バシヨ (basho - place)"},
            {"symbol": "ビ", "romaji": "bi", "example_word": "ビョウイン (byouin - hospital)"},
            {"symbol": "ブ", "romaji": "bu", "example_word": "ブタ (buta - pig)"},
            {"symbol": "ベ", "romaji": "be", "example_word": "ベンキョウ (benkyou - study)"},
            {"symbol": "ボ", "romaji": "bo", "example_word": "ボウシ (boushi - hat)"},
        ]

        handakuten = [
            {"symbol": "パ", "romaji": "pa", "example_word": "パン (pan - bread)"},
            {"symbol": "ピ", "romaji": "pi", "example_word": "ピアノ (piano)"},
            {"symbol": "プ", "romaji": "pu", "example_word": "プール (puuru - pool)"},
            {"symbol": "ペ", "romaji": "pe", "example_word": "ペン (pen - pen)"},
            {"symbol": "ポ", "romaji": "po", "example_word": "ポケット (poketto - pocket)"},
        ]

        yoon = [
            {"symbol": "キャ", "romaji": "kya", "example_word": "キャット (kyatto - cat)"},
            {"symbol": "キュ", "romaji": "kyu", "example_word": "キュウリ (kyuuri - cucumber)"},
            {"symbol": "キョ", "romaji": "kyo", "example_word": "キョウ (kyou - today)"},
            {"symbol": "シャ", "romaji": "sha", "example_word": "シャワー (shawaa - shower)"},
            {"symbol": "シュ", "romaji": "shu", "example_word": "シュウマイ (shuumai - dumplings)"},
            {"symbol": "ショ", "romaji": "sho", "example_word": "ショウガ (shouga - ginger)"},
            {"symbol": "チャ", "romaji": "cha", "example_word": "チャワン (chawan - bowl)"},
            {"symbol": "チュ", "romaji": "chu", "example_word": "チューリップ (chuurippu - tulip)"},
            {
                "symbol": "チョ",
                "romaji": "cho",
                "example_word": "チョコレート (chokoreeto - chocolate)",
            },
            {"symbol": "ニャ", "romaji": "nya", "example_word": "ニャンコ (nyanko - cat)"},
            {"symbol": "ニュ", "romaji": "nyu", "example_word": "ニュウリョク (nyuuryoku - input)"},
            {"symbol": "ニョ", "romaji": "nyo", "example_word": "ニョキ (nyoki - growth)"},
            {"symbol": "ヒャ", "romaji": "hya", "example_word": "ヒャク (hyaku - hundred)"},
            {"symbol": "ヒュ", "romaji": "hyu", "example_word": "ヒュウガ (hyuuga - the sun)"},
            {"symbol": "ヒョ", "romaji": "hyo", "example_word": "ヒョウ (hyou - leopard)"},
            {"symbol": "ミャ", "romaji": "mya", "example_word": "ミャク (myaku - pulse)"},
            {"symbol": "ミュ", "romaji": "myu", "example_word": "ミュウ (myuu - music)"},
            {"symbol": "ミョ", "romaji": "myo", "example_word": "ミョウ (myou - unusual)"},
            {"symbol": "リャ", "romaji": "rya", "example_word": "リャク (ryaku - abbreviation)"},
            {"symbol": "リュ", "romaji": "ryu", "example_word": "リュウ (ryuu - dragon)"},
            {"symbol": "リョ", "romaji": "ryo", "example_word": "リョウ (ryou - fee)"},
            {"symbol": "ギャ", "romaji": "gya", "example_word": "ギャク (gyaku - reverse)"},
            {"symbol": "ギュ", "romaji": "gyu", "example_word": "ギュウニク (gyuuniku - beef)"},
            {"symbol": "ギョ", "romaji": "gyo", "example_word": "ギョウ (gyou - business)"},
            {"symbol": "ピャ", "romaji": "pya", "example_word": "ピャク (pyaku - hundred)"},
            {"symbol": "ピュ", "romaji": "pyu", "example_word": "ピュウ (pyuu - sound of wind)"},
            {"symbol": "ピョ", "romaji": "pyo", "example_word": "ピョウ (pyou - calculation)"},
        ]

        return [
            (katakana_main_list, TypeScriptCharacter.NONE),
            (dakuten, TypeScriptCharacter.DAKUTEN),
            (handakuten, TypeScriptCharacter.HANDAKUTEN),
            (yoon, TypeScriptCharacter.Yoon),
        ]

    def insert_to_db(self, script, script_type):
        """
        Inserts characters into the database and generates audio if necessary.
        """
        characters_to_create = []
        for order_val, character in enumerate(script):
            obj, created = Character.objects.get_or_create(
                script=LanguageScript.KATAKANA,
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

        self.stdout.write(self.style.SUCCESS("✅ Katakana characters seeded and audio generated!"))

    def handle(self, *args, **kwargs):
        # Insert Katakana characters including Dakuten, Handakuten, and Yoon
        script_list = self.get_script_data()
        for data in script_list:
            self.insert_to_db(script=data[0], script_type=data[1])

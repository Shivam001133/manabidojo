from django.core.management.base import BaseCommand
from manabhi_dojo.languages.models import LanguageScript, Character


class Command(BaseCommand):
    help = "Seed the Katakana script with 46 basic characters"

    def handle(self, *args, **kwargs):
        script, _ = LanguageScript.objects.get_or_create(
            name="katakana",
            defaults={
                "title": "Katakana Script",
                "description": "Katakana is used for foreign words, names, technical terms, and onomatopoeia."
            }
        )

        katakana_characters = [
            {"symbol": "ア", "romaji": "a", "example_word": "アイス (aisu - ice cream)"},
            {"symbol": "イ", "romaji": "i", "example_word": "インク (inku - ink)"},
            {"symbol": "ウ", "romaji": "u", "example_word": "ウサギ (usagi - rabbit)"},
            {"symbol": "エ", "romaji": "e", "example_word": "エビ (ebi - shrimp)"},
            {"symbol": "オ", "romaji": "o", "example_word": "オレンジ (orenji - orange)"},

            {"symbol": "カ", "romaji": "ka", "example_word": "カメラ (kamera - camera)"},
            {"symbol": "キ", "romaji": "ki", "example_word": "キリン (kirin - giraffe)"},
            {"symbol": "ク", "romaji": "ku", "example_word": "クマ (kuma - bear)"},
            {"symbol": "ケ", "romaji": "ke", "example_word": "ケーキ (keeki - cake)"},
            {"symbol": "コ", "romaji": "ko", "example_word": "コーヒー (koohii - coffee)"},

            {"symbol": "サ", "romaji": "sa", "example_word": "サラダ (sarada - salad)"},
            {"symbol": "シ", "romaji": "shi", "example_word": "シーツ (shiitsu - sheets)"},
            {"symbol": "ス", "romaji": "su", "example_word": "スイカ (suika - watermelon)"},
            {"symbol": "セ", "romaji": "se", "example_word": "セーター (seetaa - sweater)"},
            {"symbol": "ソ", "romaji": "so", "example_word": "ソファ (sofa - sofa)"},

            {"symbol": "タ", "romaji": "ta", "example_word": "タコ (tako - octopus)"},
            {"symbol": "チ", "romaji": "chi", "example_word": "チーズ (chiizu - cheese)"},
            {"symbol": "ツ", "romaji": "tsu", "example_word": "ツナ (tsuna - tuna)"},
            {"symbol": "テ", "romaji": "te", "example_word": "テレビ (terebi - television)"},
            {"symbol": "ト", "romaji": "to", "example_word": "トマト (tomato)"},

            {"symbol": "ナ", "romaji": "na", "example_word": "ナス (nasu - eggplant)"},
            {"symbol": "ニ", "romaji": "ni", "example_word": "ニンジン (ninjin - carrot)"},
            {"symbol": "ヌ", "romaji": "nu", "example_word": "ヌードル (nuudoru - noodles)"},
            {"symbol": "ネ", "romaji": "ne", "example_word": "ネックレス (nekkuresu - necklace)"},
            {"symbol": "ノ", "romaji": "no", "example_word": "ノート (nooto - notebook)"},

            {"symbol": "ハ", "romaji": "ha", "example_word": "ハサミ (hasami - scissors)"},
            {"symbol": "ヒ", "romaji": "hi", "example_word": "ヒツジ (hitsuji - sheep)"},
            {"symbol": "フ", "romaji": "fu", "example_word": "フルーツ (furuutsu - fruits)"},
            {"symbol": "ヘ", "romaji": "he", "example_word": "ヘアー (heaa - hair)"},
            {"symbol": "ホ", "romaji": "ho", "example_word": "ホテル (hoteru - hotel)"},

            {"symbol": "マ", "romaji": "ma", "example_word": "マスク (masuku - mask)"},
            {"symbol": "ミ", "romaji": "mi", "example_word": "ミルク (miruku - milk)"},
            {"symbol": "ム", "romaji": "mu", "example_word": "ムシ (mushi - insect)"},
            {"symbol": "メ", "romaji": "me", "example_word": "メガネ (megane - glasses)"},
            {"symbol": "モ", "romaji": "mo", "example_word": "モモ (momo - peach)"},

            {"symbol": "ヤ", "romaji": "ya", "example_word": "ヤサイ (yasai - vegetable)"},
            {"symbol": "ユ", "romaji": "yu", "example_word": "ユキ (yuki - snow)"},
            {"symbol": "ヨ", "romaji": "yo", "example_word": "ヨット (yotto - yacht)"},

            {"symbol": "ラ", "romaji": "ra", "example_word": "ラーメン (raamen - ramen)"},
            {"symbol": "リ", "romaji": "ri", "example_word": "リス (risu - squirrel)"},
            {"symbol": "ル", "romaji": "ru", "example_word": "ルール (ruuru - rule)"},
            {"symbol": "レ", "romaji": "re", "example_word": "レモン (remon - lemon)"},
            {"symbol": "ロ", "romaji": "ro", "example_word": "ロボット (robotto - robot)"},

            {"symbol": "ワ", "romaji": "wa", "example_word": "ワイン (wain - wine)"},
            {"symbol": "ヲ", "romaji": "wo", "example_word": "ヲ - particle (rare use)"},
            {"symbol": "ン", "romaji": "n", "example_word": "パン (pan - bread)"}
        ]

        for char in katakana_characters:
            obj, created = Character.objects.get_or_create(
                script=script,
                symbol=char["symbol"],
                defaults={
                    "romaji": char["romaji"],
                    "example_word": char["example_word"]
                }
            )
            status = "✓ Added" if created else "⏭ Skipped"
            self.stdout.write(f"{status}: {char['symbol']} ({char['romaji']})")

        self.stdout.write(self.style.SUCCESS("✅ All Katakana characters seeded successfully."))

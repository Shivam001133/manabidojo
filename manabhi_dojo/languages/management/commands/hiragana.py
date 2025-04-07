from django.core.management.base import BaseCommand
from manabhi_dojo.languages.models import Character, LanguageScript, TypeScriptCharacter
from gtts import gTTS
from django.core.files.base import ContentFile
import io


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
            {
                "symbol": "あ",
                "romaji": "a",
                "example_word": "あめ (ame - rain)",
                "quiz_options": [
                    {"question": "あ", "options": ["yo", "he", "a", "shi"], "answer": "a"}
                ],
            },
            {
                "symbol": "い",
                "romaji": "i",
                "example_word": "いぬ (inu - dog)",
                "quiz_options": [
                    {"question": "い", "options": ["hi", "te", "i", "shi"], "answer": "i"}
                ],
            },
            {
                "symbol": "う",
                "romaji": "u",
                "example_word": "うみ (umi - sea)",
                "quiz_options": [
                    {"question": "う", "options": ["u", "ya", "me", "ka"], "answer": "u"}
                ],
            },
            {
                "symbol": "え",
                "romaji": "e",
                "example_word": "えき (eki - station)",
                "quiz_options": [
                    {"question": "え", "options": ["ke", "ru", "me", "e"], "answer": "e"}
                ],
            },
            {
                "symbol": "お",
                "romaji": "o",
                "example_word": "おちゃ (ocha - tea)",
                "quiz_options": [
                    {"question": "お", "options": ["yu", "he", "wa", "o"], "answer": "o"}
                ],
            },
            {
                "symbol": "か",
                "romaji": "ka",
                "example_word": "かさ (kasa - umbrella)",
                "quiz_options": [
                    {"question": "か", "options": ["ka", "ya", "e", "na"], "answer": "ka"}
                ],
            },
            {
                "symbol": "き",
                "romaji": "ki",
                "example_word": "きつね (kitsune - fox)",
                "quiz_options": [
                    {"question": "き", "options": ["tsu", "ku", "ki", "ra"], "answer": "ki"}
                ],
            },
            {
                "symbol": "く",
                "romaji": "ku",
                "example_word": "くも (kumo - cloud)",
                "quiz_options": [
                    {"question": "く", "options": ["a", "yo", "ku", "ko"], "answer": "ku"}
                ],
            },
            {
                "symbol": "け",
                "romaji": "ke",
                "example_word": "けむし (kemushi - caterpillar)",
                "quiz_options": [
                    {"question": "け", "options": ["se", "shi", "ke", "he"], "answer": "ke"}
                ],
            },
            {
                "symbol": "こ",
                "romaji": "ko",
                "example_word": "こども (kodomo - child)",
                "quiz_options": [
                    {"question": "こ", "options": ["mi", "te", "chi", "ko"], "answer": "ko"}
                ],
            },
            {
                "symbol": "さ",
                "romaji": "sa",
                "example_word": "さかな (sakana - fish)",
                "quiz_options": [
                    {"question": "さ", "options": ["nu", "n", "na", "sa"], "answer": "sa"}
                ],
            },
            {
                "symbol": "し",
                "romaji": "shi",
                "example_word": "しろ (shiro - white)",
                "quiz_options": [
                    {"question": "し", "options": ["na", "no", "mu", "shi"], "answer": "shi"}
                ],
            },
            {
                "symbol": "す",
                "romaji": "su",
                "example_word": "すし (sushi)",
                "quiz_options": [
                    {"question": "す", "options": ["sa", "su", "hi", "wo"], "answer": "su"}
                ],
            },
            {
                "symbol": "せ",
                "romaji": "se",
                "example_word": "せかい (sekai - world)",
                "quiz_options": [
                    {"question": "せ", "options": ["sa", "ni", "se", "mi"], "answer": "se"}
                ],
            },
            {
                "symbol": "そ",
                "romaji": "so",
                "example_word": "そら (sora - sky)",
                "quiz_options": [
                    {"question": "そ", "options": ["ta", "so", "se", "wa"], "answer": "so"}
                ],
            },
            {
                "symbol": "た",
                "romaji": "ta",
                "example_word": "たまご (tamago - egg)",
                "quiz_options": [
                    {"question": "た", "options": ["nu", "u", "ta", "ki"], "answer": "ta"}
                ],
            },
            {
                "symbol": "ち",
                "romaji": "chi",
                "example_word": "ちず (chizu - map)",
                "quiz_options": [
                    {"question": "ち", "options": ["shi", "chi", "se", "he"], "answer": "chi"}
                ],
            },
            {
                "symbol": "つ",
                "romaji": "tsu",
                "example_word": "つき (tsuki - moon)",
                "quiz_options": [
                    {"question": "つ", "options": ["fu", "tsu", "n", "wa"], "answer": "tsu"}
                ],
            },
            {
                "symbol": "て",
                "romaji": "te",
                "example_word": "てがみ (tegami - letter)",
                "quiz_options": [
                    {"question": "て", "options": ["se", "te", "n", "a"], "answer": "te"}
                ],
            },
            {
                "symbol": "と",
                "romaji": "to",
                "example_word": "とり (tori - bird)",
                "quiz_options": [
                    {"question": "と", "options": ["n", "o", "re", "to"], "answer": "to"}
                ],
            },
            {
                "symbol": "な",
                "romaji": "na",
                "example_word": "なつ (natsu - summer)",
                "quiz_options": [
                    {"question": "な", "options": ["yu", "ro", "a", "na"], "answer": "na"}
                ],
            },
            {
                "symbol": "に",
                "romaji": "ni",
                "example_word": "にほん (nihon - Japan)",
                "quiz_options": [
                    {"question": "に", "options": ["wo", "ni", "e", "he"], "answer": "ni"}
                ],
            },
            {
                "symbol": "ぬ",
                "romaji": "nu",
                "example_word": "ぬの (nuno - cloth)",
                "quiz_options": [
                    {"question": "ぬ", "options": ["tsu", "no", "nu", "su"], "answer": "nu"}
                ],
            },
            {
                "symbol": "ね",
                "romaji": "ne",
                "example_word": "ねこ (neko - cat)",
                "quiz_options": [
                    {"question": "ね", "options": ["mu", "ne", "ta", "su"], "answer": "ne"}
                ],
            },
            {
                "symbol": "の",
                "romaji": "no",
                "example_word": "のう (nou - brain)",
                "quiz_options": [
                    {"question": "の", "options": ["ku", "no", "su", "ko"], "answer": "no"}
                ],
            },
            {
                "symbol": "は",
                "romaji": "ha",
                "example_word": "はな (hana - flower/nose)",
                "quiz_options": [
                    {"question": "は", "options": ["ru", "mi", "su", "ha"], "answer": "ha"}
                ],
            },
            {
                "symbol": "ひ",
                "romaji": "hi",
                "example_word": "ひと (hito - person)",
                "quiz_options": [
                    {"question": "ひ", "options": ["ka", "hi", "re", "ru"], "answer": "hi"}
                ],
            },
            {
                "symbol": "ふ",
                "romaji": "fu",
                "example_word": "ふね (fune - ship)",
                "quiz_options": [
                    {"question": "ふ", "options": ["ta", "ko", "fu", "ya"], "answer": "fu"}
                ],
            },
            {
                "symbol": "へ",
                "romaji": "he",
                "example_word": "へや (heya - room)",
                "quiz_options": [
                    {"question": "へ", "options": ["hi", "he", "tsu", "nu"], "answer": "he"}
                ],
            },
            {
                "symbol": "ほ",
                "romaji": "ho",
                "example_word": "ほし (hoshi - star)",
                "quiz_options": [
                    {"question": "ほ", "options": ["n", "chi", "u", "ho"], "answer": "ho"}
                ],
            },
            {
                "symbol": "ま",
                "romaji": "ma",
                "example_word": "まど (mado - window)",
                "quiz_options": [
                    {"question": "ま", "options": ["ko", "sa", "yu", "ma"], "answer": "ma"}
                ],
            },
            {
                "symbol": "み",
                "romaji": "mi",
                "example_word": "みず (mizu - water)",
                "quiz_options": [
                    {"question": "み", "options": ["wo", "mi", "to", "ka"], "answer": "mi"}
                ],
            },
            {
                "symbol": "む",
                "romaji": "mu",
                "example_word": "むし (mushi - insect)",
                "quiz_options": [
                    {"question": "む", "options": ["ya", "yo", "mu", "chi"], "answer": "mu"}
                ],
            },
            {
                "symbol": "め",
                "romaji": "me",
                "example_word": "めがね (megane - glasses)",
                "quiz_options": [
                    {"question": "め", "options": ["yo", "me", "i", "su"], "answer": "me"}
                ],
            },
            {
                "symbol": "も",
                "romaji": "mo",
                "example_word": "もり (mori - forest)",
                "quiz_options": [
                    {"question": "も", "options": ["chi", "ko", "mo", "ro"], "answer": "mo"}
                ],
            },
            {
                "symbol": "や",
                "romaji": "ya",
                "example_word": "やま (yama - mountain)",
                "quiz_options": [
                    {"question": "や", "options": ["fu", "mo", "ya", "ku"], "answer": "ya"}
                ],
            },
            {
                "symbol": "ゆ",
                "romaji": "yu",
                "example_word": "ゆき (yuki - snow)",
                "quiz_options": [
                    {"question": "ゆ", "options": ["ne", "no", "yu", "re"], "answer": "yu"}
                ],
            },
            {
                "symbol": "よ",
                "romaji": "yo",
                "example_word": "よる (yoru - night)",
                "quiz_options": [
                    {"question": "よ", "options": ["yo", "ho", "chi", "n"], "answer": "yo"}
                ],
            },
            {
                "symbol": "ら",
                "romaji": "ra",
                "example_word": "らいおん (raion - lion)",
                "quiz_options": [
                    {"question": "ら", "options": ["wo", "o", "ke", "ra"], "answer": "ra"}
                ],
            },
            {
                "symbol": "り",
                "romaji": "ri",
                "example_word": "りす (risu - squirrel)",
                "quiz_options": [
                    {"question": "り", "options": ["ri", "mi", "o", "ka"], "answer": "ri"}
                ],
            },
            {
                "symbol": "る",
                "romaji": "ru",
                "example_word": "るす (rusu - absence)",
                "quiz_options": [
                    {"question": "る", "options": ["n", "ru", "mi", "ra"], "answer": "ru"}
                ],
            },
            {
                "symbol": "れ",
                "romaji": "re",
                "example_word": "れいぞうこ (reizouko - fridge)",
                "quiz_options": [
                    {"question": "れ", "options": ["na", "wa", "wo", "re"], "answer": "re"}
                ],
            },
            {
                "symbol": "ろ",
                "romaji": "ro",
                "example_word": "ろうそく (rousoku - candle)",
                "quiz_options": [
                    {"question": "ろ", "options": ["ro", "mo", "shi", "re"], "answer": "ro"}
                ],
            },
            {
                "symbol": "わ",
                "romaji": "wa",
                "example_word": "わに (wani - crocodile)",
                "quiz_options": [
                    {"question": "わ", "options": ["ke", "wa", "ru", "me"], "answer": "wa"}
                ],
            },
            {
                "symbol": "を",
                "romaji": "wo",
                "example_word": "を - particle (direct object marker)",
                "quiz_options": [
                    {"question": "を", "options": ["shi", "ri", "mo", "wo"], "answer": "wo"}
                ],
            },
            {
                "symbol": "ん",
                "romaji": "n",
                "example_word": "ほん (hon - book)",
                "quiz_options": [
                    {"question": "ん", "options": ["n", "yo", "ro", "u"], "answer": "n"}
                ],
            },
        ]

        dakuten = [
            {
                "symbol": "が",
                "romaji": "ga",
                "example_word": "がく (gaku - study)",
                "quiz_options": [
                    {"question": "が", "options": ["ga", "za", "bu", "zu"], "answer": "ga"}
                ],
            },
            {
                "symbol": "ぎ",
                "romaji": "gi",
                "example_word": "ぎんこう (ginkou - bank)",
                "quiz_options": [
                    {"question": "ぎ", "options": ["za", "gi", "do", "ze"], "answer": "gi"}
                ],
            },
            {
                "symbol": "ぐ",
                "romaji": "gu",
                "example_word": "ぐあい (guai - condition)",
                "quiz_options": [
                    {"question": "ぐ", "options": ["zo", "gu", "ga", "ji"], "answer": "gu"}
                ],
            },
            {
                "symbol": "げ",
                "romaji": "ge",
                "example_word": "げんき (genki - healthy)",
                "quiz_options": [
                    {"question": "げ", "options": ["ji", "ge", "go", "bo"], "answer": "ge"}
                ],
            },
            {
                "symbol": "ご",
                "romaji": "go",
                "example_word": "ごはん (gohan - rice/meal)",
                "quiz_options": [
                    {"question": "ご", "options": ["ba", "go", "ze", "bu"], "answer": "go"}
                ],
            },
            {
                "symbol": "ざ",
                "romaji": "za",
                "example_word": "ざっし (zasshi - magazine)",
                "quiz_options": [
                    {"question": "ざ", "options": ["zu", "za", "bi", "gu"], "answer": "za"}
                ],
            },
            {
                "symbol": "じ",
                "romaji": "ji",
                "example_word": "じてんしゃ (jitensha - bicycle)",
                "quiz_options": [
                    {"question": "じ", "options": ["be", "ji", "do", "bu"], "answer": "ji"}
                ],
            },
            {
                "symbol": "ず",
                "romaji": "zu",
                "example_word": "ずっと (zutto - forever)",
                "quiz_options": [
                    {"question": "ず", "options": ["zu", "go", "de", "bu"], "answer": "zu"}
                ],
            },
            {
                "symbol": "ぜ",
                "romaji": "ze",
                "example_word": "ぜんぶ (zenbu - everything)",
                "quiz_options": [
                    {"question": "ぜ", "options": ["ze", "za", "da", "bu"], "answer": "ze"}
                ],
            },
            {
                "symbol": "ぞ",
                "romaji": "zo",
                "example_word": "ぞう (zou - elephant)",
                "quiz_options": [
                    {"question": "ぞ", "options": ["ga", "zo", "bi", "do"], "answer": "zo"}
                ],
            },
            {
                "symbol": "だ",
                "romaji": "da",
                "example_word": "だいがく (daigaku - university)",
                "quiz_options": [
                    {"question": "だ", "options": ["gi", "da", "ga", "ji"], "answer": "da"}
                ],
            },
            {
                "symbol": "ぢ",
                "romaji": "ji",
                "example_word": "ぢかん (jikan - time)",
                "quiz_options": [
                    {"question": "ぢ", "options": ["be", "ji", "ge", "ga"], "answer": "ji"}
                ],
            },
            {
                "symbol": "づ",
                "romaji": "zu",
                "example_word": "づけもの (dzukemono - pickles)",
                "quiz_options": [
                    {"question": "づ", "options": ["bi", "ga", "za", "zu"], "answer": "zu"}
                ],
            },
            {
                "symbol": "で",
                "romaji": "de",
                "example_word": "できる (dekiru - can)",
                "quiz_options": [
                    {"question": "で", "options": ["ba", "bu", "zo", "de"], "answer": "de"}
                ],
            },
            {
                "symbol": "ど",
                "romaji": "do",
                "example_word": "どうぞ (douzo - please)",
                "quiz_options": [
                    {"question": "ど", "options": ["bi", "do", "ge", "bo"], "answer": "do"}
                ],
            },
            {
                "symbol": "ば",
                "romaji": "ba",
                "example_word": "ばしょ (basho - place)",
                "quiz_options": [
                    {"question": "ば", "options": ["ga", "de", "do", "ba"], "answer": "ba"}
                ],
            },
            {
                "symbol": "び",
                "romaji": "bi",
                "example_word": "びょういん (byouin - hospital)",
                "quiz_options": [
                    {"question": "び", "options": ["bu", "bi", "ze", "ji"], "answer": "bi"}
                ],
            },
            {
                "symbol": "ぶ",
                "romaji": "bu",
                "example_word": "ぶた (buta - pig)",
                "quiz_options": [
                    {"question": "ぶ", "options": ["bi", "do", "bu", "zu"], "answer": "bu"}
                ],
            },
            {
                "symbol": "べ",
                "romaji": "be",
                "example_word": "べんきょう (benkyou - study)",
                "quiz_options": [
                    {"question": "べ", "options": ["gu", "be", "do", "ba"], "answer": "be"}
                ],
            },
            {
                "symbol": "ぼ",
                "romaji": "bo",
                "example_word": "ぼうし (boushi - hat)",
                "quiz_options": [
                    {"question": "ぼ", "options": ["bo", "bu", "gi", "do"], "answer": "bo"}
                ],
            },
        ]

        handakuten = [
            {
                "symbol": "ぱ",
                "romaji": "pa",
                "example_word": "ぱん (pan - bread)",
                "options": [
                    {"question": "ぱ", "options": ["pe", "pi", "pa", "pu"], "answer": "pa"}
                ],
            },
            {
                "symbol": "ぴ",
                "romaji": "pi",
                "example_word": "ぴあの (piano)",
                "options": [
                    {"question": "ぴ", "options": ["pu", "po", "pa", "pi"], "answer": "pi"}
                ],
            },
            {
                "symbol": "ぷ",
                "romaji": "pu",
                "example_word": "ぷーる (puuru - pool)",
                "options": [
                    {"question": "ぷ", "options": ["pu", "pa", "po", "pi"], "answer": "pu"}
                ],
            },
            {
                "symbol": "ぺ",
                "romaji": "pe",
                "example_word": "ぺん (pen - pen)",
                "options": [
                    {"question": "ぺ", "options": ["pe", "pi", "pu", "po"], "answer": "pe"}
                ],
            },
            {
                "symbol": "ぽ",
                "romaji": "po",
                "example_word": "ぽけっと (poketto - pocket)",
                "options": [
                    {"question": "ぽ", "options": ["po", "pi", "pu", "pe"], "answer": "po"}
                ],
            },
        ]

        yoon = [
            {
                "symbol": "きゃ",
                "romaji": "kya",
                "example_word": "きゃく (kyaku - guest)",
                "options": [
                    {"question": "きゃ", "options": ["chu", "mya", "kya", "gyu"], "answer": "kya"}
                ],
            },
            {
                "symbol": "きゅ",
                "romaji": "kyu",
                "example_word": "きゅう (kyuu - nine)",
                "options": [
                    {"question": "きゅ", "options": ["kyu", "dya", "pya", "ryo"], "answer": "kyu"}
                ],
            },
            {
                "symbol": "きょ",
                "romaji": "kyo",
                "example_word": "きょう (kyou - today)",
                "options": [
                    {"question": "きょ", "options": ["kyo", "nyo", "mya", "cha"], "answer": "kyo"}
                ],
            },
            {
                "symbol": "しゃ",
                "romaji": "sha",
                "example_word": "しゃしん (shashin - photo)",
                "options": [
                    {"question": "しゃ", "options": ["chu", "shu", "dyo", "sha"], "answer": "sha"}
                ],
            },
            {
                "symbol": "しゅ",
                "romaji": "shu",
                "example_word": "しゅくだい (shukudai - homework)",
                "options": [
                    {"question": "しゅ", "options": ["sho", "shu", "myu", "hyu"], "answer": "shu"}
                ],
            },
            {
                "symbol": "しょ",
                "romaji": "sho",
                "example_word": "しょうがっこう (shougakkou - elementary school)",
                "options": [
                    {"question": "しょ", "options": ["gyo", "sho", "hyu", "nyu"], "answer": "sho"}
                ],
            },
            {
                "symbol": "ちゃ",
                "romaji": "cha",
                "example_word": "ちゃわん (chawan - bowl)",
                "options": [
                    {"question": "ちゃ", "options": ["hyo", "cha", "mya", "chu"], "answer": "cha"}
                ],
            },
            {
                "symbol": "ちゅ",
                "romaji": "chu",
                "example_word": "ちゅうごく (chuugoku - China)",
                "options": [
                    {"question": "ちゅ", "options": ["chu", "pyo", "gyo", "gya"], "answer": "chu"}
                ],
            },
            {
                "symbol": "ちょ",
                "romaji": "cho",
                "example_word": "ちょうちょう (chouchou - butterfly)",
                "options": [
                    {"question": "ちょ", "options": ["pya", "pyu", "cho", "nyo"], "answer": "cho"}
                ],
            },
            {
                "symbol": "ぢゃ",
                "romaji": "dya",
                "example_word": "ぢゃんけん (janken - rock-paper-scissors)",
                "options": [
                    {"question": "ぢゃ", "options": ["pyo", "mya", "dyu", "dya"], "answer": "dya"}
                ],
            },
            {
                "symbol": "ぢゅ",
                "romaji": "dyu",
                "example_word": "ぢゅう (juu - ten)",
                "options": [
                    {"question": "ぢゅ", "options": ["cha", "dyu", "cho", "kya"], "answer": "dyu"}
                ],
            },
            {
                "symbol": "ぢょ",
                "romaji": "dyo",
                "example_word": "ぢょう (jou - situation)",
                "options": [
                    {"question": "ぢょ", "options": ["dyo", "gyo", "hyo", "nyu"], "answer": "dyo"}
                ],
            },
            {
                "symbol": "にゃ",
                "romaji": "nya",
                "example_word": "にゃんこ (nyanko - cat)",
                "options": [
                    {"question": "にゃ", "options": ["nya", "shu", "chu", "dyu"], "answer": "nya"}
                ],
            },
            {
                "symbol": "にゅ",
                "romaji": "nyu",
                "example_word": "にゅうりょく (nyuuryoku - input)",
                "options": [
                    {"question": "にゅ", "options": ["nyu", "shu", "sha", "chu"], "answer": "nyu"}
                ],
            },
            {
                "symbol": "にょ",
                "romaji": "nyo",
                "example_word": "にょき (nyoki - growth)",
                "options": [
                    {"question": "にょ", "options": ["sho", "nyo", "shu", "dya"], "answer": "nyo"}
                ],
            },
            {
                "symbol": "ひゃ",
                "romaji": "hya",
                "example_word": "ひゃく (hyaku - hundred)",
                "options": [
                    {"question": "ひゃ", "options": ["dyu", "pyu", "sha", "hya"], "answer": "hya"}
                ],
            },
            {
                "symbol": "ひゅ",
                "romaji": "hyu",
                "example_word": "ひゅうが (hyuuga - the sun)",
                "options": [
                    {"question": "ひゅ", "options": ["hyu", "ryo", "chu", "shu"], "answer": "hyu"}
                ],
            },
            {
                "symbol": "ひょ",
                "romaji": "hyo",
                "example_word": "ひょう (hyou - leopard)",
                "options": [
                    {"question": "ひょ", "options": ["myo", "hyo", "sha", "pyu"], "answer": "hyo"}
                ],
            },
            {
                "symbol": "みゃ",
                "romaji": "mya",
                "example_word": "みゃく (myaku - pulse)",
                "options": [
                    {"question": "みゃ", "options": ["mya", "chu", "kyo", "sha"], "answer": "mya"}
                ],
            },
            {
                "symbol": "みゅ",
                "romaji": "myu",
                "example_word": "みゅう (myuu - music)",
                "options": [
                    {"question": "みゅ", "options": ["myo", "myu", "sho", "nyu"], "answer": "myu"}
                ],
            },
            {
                "symbol": "みょ",
                "romaji": "myo",
                "example_word": "みょう (myou - unusual)",
                "options": [
                    {"question": "みょ", "options": ["hyo", "myo", "kya", "cha"], "answer": "myo"}
                ],
            },
            {
                "symbol": "りゃ",
                "romaji": "rya",
                "example_word": "りゃく (ryaku - abbreviation)",
                "options": [
                    {"question": "りゃ", "options": ["rya", "dyu", "hya", "pya"], "answer": "rya"}
                ],
            },
            {
                "symbol": "りゅ",
                "romaji": "ryu",
                "example_word": "りゅう (ryuu - dragon)",
                "options": [
                    {"question": "りゅ", "options": ["ryu", "kya", "dyo", "gya"], "answer": "ryu"}
                ],
            },
            {
                "symbol": "りょ",
                "romaji": "ryo",
                "example_word": "りょう (ryou - fee)",
                "options": [
                    {"question": "りょ", "options": ["dyo", "ryo", "pya", "myo"], "answer": "ryo"}
                ],
            },
            {
                "symbol": "ぎゃ",
                "romaji": "gya",
                "example_word": "ぎゃく (gyaku - reverse)",
                "options": [
                    {"question": "ぎゃ", "options": ["gya", "hyu", "dyo", "shu"], "answer": "gya"}
                ],
            },
            {
                "symbol": "ぎゅ",
                "romaji": "gyu",
                "example_word": "ぎゅうにく (gyuuniku - beef)",
                "options": [
                    {"question": "ぎゅ", "options": ["gyu", "hya", "mya", "nyo"], "answer": "gyu"}
                ],
            },
            {
                "symbol": "ぎょ",
                "romaji": "gyo",
                "example_word": "ぎょう (gyou - business)",
                "options": [
                    {"question": "ぎょ", "options": ["nyo", "hyo", "gyo", "nyu"], "answer": "gyo"}
                ],
            },
            {
                "symbol": "ぴゃ",
                "romaji": "pya",
                "example_word": "ぴゃく (pyaku - hundred)",
                "options": [
                    {"question": "ぴゃ", "options": ["kyo", "nyo", "pya", "dyu"], "answer": "pya"}
                ],
            },
            {
                "symbol": "ぴゅ",
                "romaji": "pyu",
                "example_word": "ぴゅう (pyuu - sound of wind)",
                "options": [
                    {"question": "ぴゅ", "options": ["pyu", "sho", "sha", "nyo"], "answer": "pyu"}
                ],
            },
            {
                "symbol": "ぴょ",
                "romaji": "pyo",
                "example_word": "ぴょう (pyou - calculation)",
                "options": [
                    {"question": "ぴゅ", "options": ["pyu", "sho", "sha", "nyo"], "answer": "pyu"}
                ],
            },
        ]

        return [
            (main_list, TypeScriptCharacter.NONE),
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

        self.stdout.write(self.style.SUCCESS("✅ Hiragana characters seeded and audio generated!"))

    def handle(self, *args, **kwargs):
        # Insert Hiragana characters
        script_list = self.get_script_data()
        for data in script_list:
            self.insert_to_db(script=data[0], script_type=data[1])

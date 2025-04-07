from django.shortcuts import render

# from django.contrib.auth.decorators import login_required
from manabhi_dojo.languages.models import Character, LanguageScript, TypeScriptCharacter, Kanji


def hiragana_view(request):
    # Fetch characters from the database
    basic_hiragana = Character.objects.filter(
        script=LanguageScript.HIRAGANA, script_type=TypeScriptCharacter.NONE
    ).order_by("order")

    # Organize characters into the 3 sections
    dakuten_handakuten = Character.objects.filter(
        script=LanguageScript.HIRAGANA,
        script_type__in=[TypeScriptCharacter.DAKUTEN, TypeScriptCharacter.HANDAKUTEN],
    ).order_by("order")

    yoon_combinations = Character.objects.filter(
        script=LanguageScript.HIRAGANA, script_type=TypeScriptCharacter.Yoon
    ).order_by("order")

    return render(
        request,
        "pages/consonants.html",
        {
            "title": "Hiragana Chart",
            "basic": basic_hiragana,
            "dakuten": dakuten_handakuten,
            "yoon": yoon_combinations,
        },
    )


def katakana_view(request):
    # Fetch characters from the database
    basic_katakana = Character.objects.filter(
        script=LanguageScript.KATAKANA, script_type=TypeScriptCharacter.NONE
    ).order_by("order")

    # Organize characters into the 3 sections
    dakuten_handakuten = Character.objects.filter(
        script=LanguageScript.KATAKANA,
        script_type__in=[TypeScriptCharacter.DAKUTEN, TypeScriptCharacter.HANDAKUTEN],
    ).order_by("order")

    yoon_combinations = Character.objects.filter(
        script=LanguageScript.KATAKANA, script_type=TypeScriptCharacter.Yoon
    ).order_by("order")

    return render(
        request,
        "pages/consonants.html",
        {
            "title": "Katakana Chart",
            "basic": basic_katakana,
            "dakuten": dakuten_handakuten,
            "yoon": yoon_combinations,
        },
    )


def kanji_view(request):
    kanji_characters = Kanji.objects.all()

    return render(
        request,
        "pages/kanji.html",
        {
            "kanji": kanji_characters,
        },
    )


HIRA_QUIZ = [
    {"hiragana_symbol": "あ", "options": ["a", "e", "i", "u"], "correct_answer": "a"},
    {"hiragana_symbol": "い", "options": ["a", "i", "u", "e"], "correct_answer": "i"},
    {"hiragana_symbol": "う", "options": ["a", "i", "u", "e"], "correct_answer": "u"},
    {"hiragana_symbol": "え", "options": ["a", "i", "e", "u"], "correct_answer": "e"},
    {"hiragana_symbol": "お", "options": ["o", "i", "e", "u"], "correct_answer": "o"},
]

from django.shortcuts import render
from django.db.models import Q
from manabhi_dojo.languages.models import Character, Kanji
from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from manabhi_dojo.languages.models import Character, LanguageScript, TypeScriptCharacter


def hiragana_view(request):
    # Fetch characters from the database
    basic_hiragana = Character.objects.filter(
        script=LanguageScript.HIRAGANA, script_type=TypeScriptCharacter.NONE
    ).order_by("order")

    # Organize characters into the 3 sections
    dakuten_handakuten = Character.objects.filter(
        script=LanguageScript.HIRAGANA, 
        script_type__in=[TypeScriptCharacter.DAKUTEN, TypeScriptCharacter.HANDAKUTEN]
    ).order_by("order")

    yoon_combinations = Character.objects.filter(
        script=LanguageScript.HIRAGANA, 
        script_type=TypeScriptCharacter.Yoon
    ).order_by("order")


    return render(request, 'pages/consonants.html', {
        'title': "Hiragana Chart",
        'basic_hiragana': basic_hiragana,
        'dakuten_handakuten': dakuten_handakuten,
        'yoon_combinations': yoon_combinations,
    })


def katakana_view(request):
    katakana_characters = Character.objects.filter(script__name="katakana")

    return render(request, 'pages/consonants.html', {
        'consonants': katakana_characters,
    })


def kanji_view(request):
    kanji_characters = Kanji.objects.all()

    return render(request, 'pages/kanji.html', {
        'kanji': kanji_characters,
    })


@login_required
def lesson_view(request):
    characters = Character.objects.all()

    return render(request, 'pages/quiz.html', {
        'lesson': [],
        'characters': characters,
        'quiz_questions': [],
    })

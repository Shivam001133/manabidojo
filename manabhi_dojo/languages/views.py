from django.shortcuts import render
from django.conf import settings
from manabhi_dojo.languages.models import Character, HiraganaProgress, Kanji
from django.contrib.auth.decorators import login_required


def hiragana_view(request):
    consonants = Character.objects.all()

    return render(request, 'pages/consonants.html', {
        'consonants': consonants,
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

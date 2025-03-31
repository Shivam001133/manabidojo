from django.shortcuts import render
from django.conf import settings
from manabhi_dojo.languages.models import Character, HiraganaProgress, Kanji
from django.contrib.auth.decorators import login_required


# @login_required
def hiragana_view(request):
    # Retrieve all Katakana rows and consonants from your database
    consonants = Character.objects.all()

    # Pass the data to the template
    return render(request, 'pages/hiragana.html', {
        'consonants': consonants,
    })


def katakana_view(request):
    # Retrieve all Katakana characters from your database
    katakana_characters = Character.objects.filter(script__name="katakana")  # Adjust based on your model

    # Pass the data to the template
    return render(request, 'pages/katakana.html', {
        'katakana_characters': katakana_characters,
    })


def kanji_view(request):
    # Retrieve all Kanji characters from your database
    kanji_characters = Kanji.objects.all()  # Adjust based on your model

    # Pass the data to the template
    return render(request, 'pages/kanji.html', {
        'kanji_characters': kanji_characters,
    })


def lesson_view(request):
    # Retrieve characters and quiz questions for the lesson
    characters = Character.objects.all()

    # Pass the data to the template
    return render(request, 'pages/quiz.html', {
        'lesson': [],
        'characters': characters,
        'quiz_questions': [],
    })

from django.shortcuts import render

# from django.contrib.auth.decorators import login_required
from manabhi_dojo.languages.models import Character, LanguageScript, TypeScriptCharacter, Kanji
from django.http import JsonResponse
import random


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


def hiragana_quiz(request):
    hiragana_list = Character.objects.filter(script=LanguageScript.HIRAGANA)
    current_question = random.choice(hiragana_list).quiz_options[0]

    current_answer = request.session.get("current_question", None)
    if current_answer:
        current_answer = current_answer["answer"]
    request.session['current_question'] = current_question
    request.session.set_expiry(60)

    if request.method == "POST":
        selected_answer = request.POST.get("answer")
        is_correct = selected_answer == current_answer

        return JsonResponse(
            {   "answer": current_answer,
                "is_correct": is_correct,
                "next_question": current_question,
            }
        )
    return render(request, "pages/quiz.html", {"question": current_question})

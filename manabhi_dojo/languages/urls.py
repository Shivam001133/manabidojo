from django.urls import path
from . import views

app_name = "languages"

urlpatterns = [
    path("hiragana/", views.hiragana_view, name="hiragana"),
    path("katakana/", views.katakana_view, name="katakana"),
    path("kanji/", views.kanji_view, name="kanji"),
    path("quiz/", views.hiragana_quiz, name="hquiz"),
]

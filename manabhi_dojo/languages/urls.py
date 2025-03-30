from django.urls import path
from . import views

app_name = "languages"

urlpatterns = [
    path("katakana/", views.katakana_view, name="katakana"),
]

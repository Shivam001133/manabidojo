from django.db import models
from django.utils.translation import gettext_lazy as _


def character_audio_upload_path(instance, filename):
    script_name = instance.script.name.lower()
    return f"script_audio/{script_name}/{filename}"


class LanguageScript(models.TextChoices):
    NONE = "n", _("None")
    HIRAGANA = "h", _("Hiragana")
    KATAKANA = "k", _("Katakana")


class TypeScriptCharacter(models.TextChoices):
    NONE = "nn", _("Characters")
    DAKUTEN = "da", _("Dakuten Characters")
    HANDAKUTEN = "ha", _("Han-Dakuten Characters")
    Yoon = "yo", _("Yoon Characters")


class Character(models.Model):
    script = models.CharField(
        choices=LanguageScript.choices, default=LanguageScript.NONE, max_length=2, db_index=True
    )
    symbol = models.CharField(max_length=5)
    romaji = models.CharField(max_length=20, blank=True)
    example_word = models.CharField(max_length=100, blank=True)
    audio = models.FileField(upload_to=character_audio_upload_path, blank=True, null=True)
    script_type = models.CharField(
        choices=TypeScriptCharacter.choices, default=TypeScriptCharacter.NONE, db_index=True
    )
    order = models.PositiveIntegerField(default=0)
    quiz_options = models.JSONField(default=list)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("script", "script_type", "order")

    def __str__(self):
        return self.symbol


class Kanji(models.Model):
    character = models.CharField(max_length=5, unique=True, db_index=True)
    onyomi = models.CharField(max_length=100, blank=True)
    kunyomi = models.CharField(max_length=100, blank=True)
    meaning = models.TextField(blank=True)
    jlpt_level = models.CharField(max_length=10, blank=True)
    grade = models.IntegerField(blank=True, null=True)
    audio = models.FileField(upload_to="kanji_audio/", blank=True, null=True)
    image = models.ImageField(upload_to="kanji/", null=True)

    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "kanji_master"

    def __str__(self):
        return self.character


class Vocabulary(models.Model):
    script = models.CharField(
        choices=LanguageScript.choices, default=LanguageScript.NONE, max_length=2, db_index=True
    )
    word = models.CharField(max_length=50, blank=True, db_index=True)
    romaji = models.CharField(max_length=50, blank=True, db_index=True)
    img = models.ImageField(upload_to="vocab/", null=True, blank=True)
    img_url = models.URLField()

    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.word} - {self.romaji}"

from django.db import models
from manabhi_dojo.users.models import User


def character_audio_upload_path(instance, filename):
    script_name = instance.script.name.lower()
    return f"script_audio/{script_name}/{filename}"


class LanguageScript(models.Model):
    name = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name}"


class Character(models.Model):
    script = models.ForeignKey(
        "LanguageScript", on_delete=models.CASCADE, related_name="characters"
    )
    symbol = models.CharField(max_length=5)
    romaji = models.CharField(max_length=20, blank=True, null=True)
    meaning = models.CharField(max_length=100, blank=True, null=True)
    example_word = models.CharField(max_length=100, blank=True, null=True)
    audio = models.FileField(upload_to=character_audio_upload_path, blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.symbol


class Kanji(models.Model):

    character = models.CharField(max_length=5, unique=True)
    onyomi = models.CharField(max_length=100, blank=True, null=True)
    kunyomi = models.CharField(max_length=100, blank=True, null=True)
    meaning = models.TextField(blank=True, null=True)
    jlpt_level = models.CharField(max_length=10, blank=True, null=True)
    grade = models.IntegerField(blank=True, null=True)
    stroke_count = models.IntegerField(blank=True, null=True)
    audio = models.FileField(upload_to="kanji_audio/", blank=True, null=True)

    class Meta:
        db_table = "kanji_master"

    def __str__(self):
        return self.character


class HiraganaProgress(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    completed_characters = models.JSONField(default=list)  # List of completed character IDs
    streak = models.IntegerField(default=0)  # Current learning streak
    points = models.IntegerField(default=0)  # Points earned by the user

    def __str__(self):
        return f"{self.user.username}'s Hiragana Progress"

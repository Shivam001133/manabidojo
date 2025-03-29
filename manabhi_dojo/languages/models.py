from django.db import models


class LanguageScript(models.Model):
    name = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.name} ({self.language.iso_code})"


class Character(models.Model):
    script = models.ForeignKey(LanguageScript, on_delete=models.CASCADE, related_name='characters')
    symbol = models.CharField(max_length=5)
    romaji = models.CharField(max_length=20, blank=True, null=True)
    meaning = models.CharField(max_length=100, blank=True, null=True)
    example_word = models.CharField(max_length=100, blank=True, null=True)
    audio = models.FileField(upload_to='character_audio/', blank=True, null=True)

    def __str__(self):
        return self.symbol


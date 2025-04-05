from django.contrib import admin
from django.utils.html import format_html
from .models import LanguageScript, Character, Kanji


@admin.register(Character)
class CharacterAdmin(admin.ModelAdmin):
    list_display = (
        "symbol",
        "script",
        "script_type",
        "order",
        "audio_preview",
    )
    search_fields = ("symbol", "romaji", "example_word", "meaning")
    list_filter = ("symbol", "script", "script_type",)

    def audio_preview(self, obj):
        if obj.audio:
            return format_html(
                f'<audio controls><source src="{obj.audio.url}" type="audio/mpeg">No audio</audio>'
            )
        return "—"

    audio_preview.short_description = "Audio"


@admin.register(Kanji)
class KanjiAdmin(admin.ModelAdmin):
    list_display = (
        "character",
        "onyomi",
        "kunyomi",
        "jlpt_level",
        "grade",
        "audio_player",
    )
    search_fields = ("character", "onyomi", "kunyomi", "meaning")
    list_filter = ("jlpt_level", "grade")
    readonly_fields = ("character", "audio_player")

    fieldsets = (
        (None, {"fields": ("character", "onyomi", "kunyomi", "meaning")}),
        (
            "Details",
            {
                "fields": (
                    "jlpt_level",
                    "grade",
                    "stroke_count",
                    "audio",
                    "audio_player",
                )
            },
        ),
    )

    def audio_player(self, obj):
        if obj.audio:
            return format_html(
                f'<audio controls style="max-width: 200px;"><source src="{obj.audio.url}" '
                f'type="audio/mpeg">Your browser does not support the audio element.</audio>'
            )
        return "No audio available"

    audio_player.short_description = "Preview"

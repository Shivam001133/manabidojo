from typing import ClassVar

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.conf import settings

from manabhi_dojo.users.managers import UserManager
from manabhi_dojo.languages.models import Character


## User choices and other common models
class UserProgressType(models.TextChoices):
    NONE = "none", _("None")
    SCRIPT = "sc", _("Script")
    KANJI = "kj", _("Kanji")
    VOCABULARY = "vc", _("Vocabulary")
    GRAMMAR = "gm", _("Grammar")
    READING = "rd", _("Reading")
    LISTENING = "ls", _("Listening")


class UserJlptLevel(models.TextChoices):
    N1 = "1", _("JLPT N1")
    N2 = "2", _("JLPT N2")
    N3 = "3", _("JLPT N3")
    N4 = "4", _("JLPT N4")
    N5 = "5", _("JLPT N5")


## User models
class User(AbstractUser):
    """
    Default custom user model for MangaLab.
    If adding fields that need to be filled at user signup,
    check forms.SignupForm and forms.SocialSignupForms accordingly.
    """

    # First and last name do not cover name patterns around the globe
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
    email = models.EmailField(_("email address"), unique=True)

    REQUIRED_FIELDS = [
        "email",
    ]

    objects: ClassVar[UserManager] = UserManager()

    def get_absolute_url(self) -> str:
        """Get URL for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"pk": self.id})


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile"
    )
    full_name = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10, blank=True)
    location = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.full_name or self.user.email or f"Profile #{self.pk}"


class ScriptProgres(models.Model):
    script = models.ForeignKey(Character, on_delete=models.DO_NOTHING, related_name="scriptprogres_character")
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name="scriptprogres_user")
    currect = models.BooleanField(default=True)
    progress_timestamp = models.JSONField(default=dict)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.script.script} - {self.user.email} - {self.currect}"


class UserProgress(models.Model):
    jlpt = models.CharField(
        choices=UserJlptLevel.choices,
        default=UserJlptLevel.N5,
        max_length=10,
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_progress")
    progress_type = models.CharField(
        choices=UserProgressType.choices,
        default=UserProgressType.NONE,
        max_length=10,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.email} - {self.jlpt} - {self.progress_type}"

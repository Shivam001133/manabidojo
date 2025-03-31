# forms.py
from django import forms
from django.contrib.auth.models import User


class UserAdminCreationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 != password2:
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data


class UserAdminChangeForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Password", required=False)

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        if password and len(password) < 8:
            raise forms.ValidationError("Password must be at least 8 characters long.")
        return cleaned_data


class UserSignUpForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Password")
    password_confirmation = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")
    avatar = forms.ImageField(required=False, label="Choose Avatar")

    class Meta:
        model = User
        fields = ['username', 'email']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirmation = cleaned_data.get("password_confirmation")

        if password != password_confirmation:
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data
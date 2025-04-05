# forms.py
from django import forms
from django.contrib.auth import get_user_model


class UserAdminCreationForm(forms.ModelForm):
    password1 = forms.CharField(widget=forms.PasswordInput, label="Password")
    password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = get_user_model()
        fields = ("username", "email")

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
        model = get_user_model()
        fields = ("username", "email")

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
        model = get_user_model()
        fields = [
            "username",
            "email",
            "avatar",
            "password",
            "password_confirmation",
        ]  # Explicitly include all fields

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs.update(
                {
                    "class": (
                        "w-full px-4 py-2 border border-gray-300 dark:border-gray-600 rounded-lg "
                        "bg-white dark:bg-gray-800 text-gray-900 dark:text-gray-100 "
                        "placeholder-gray-400 dark:placeholder-gray-500 "
                        "focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                    ),
                    "placeholder": f"Enter your {field.label.lower()}",
                }
            )

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirmation = cleaned_data.get("password_confirmation")

        if password != password_confirmation:
            raise forms.ValidationError("Passwords do not match")
        return cleaned_data

from django import forms
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm

User = get_user_model()


class LoginModelForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = forms.widgets.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Email',
            'aria - label': 'Email'
        })
        self.fields['password'].widget = forms.widgets.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'aria - label': 'Password'
        })

    def clean_username(self):
        email = self.cleaned_data['username']
        if email not in settings.ALLOWED_EMAILS:
            self.add_error('username', 'Your email not in whitelist!')
        return email

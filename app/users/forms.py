from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm

User = get_user_model()


class LoginModelForm(AuthenticationForm):
    def clean_username(self):
        email = self.cleaned_data['username']
        if email not in settings.ALLOWED_EMAILS:
            self.add_error('username', 'Your email not in whitelist!')
        return email

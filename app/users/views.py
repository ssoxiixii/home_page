from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView

from .forms import CreationForm


class SignUpView(CreateView):
    form_class = CreationForm
    success_url = reverse_lazy('login')
    template_name = 'auth/registration.html'

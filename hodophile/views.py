
from django.views.generic import CreateView

from .forms import RegisterForm


class register(CreateView):
    form_class = RegisterForm
    success_url = '/login'
    template_name = 'registration/register.html'
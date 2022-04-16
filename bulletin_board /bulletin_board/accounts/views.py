from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from .forms import RegisterUserForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView


class BBLoginView(LoginView):
    template_name = 'accounts/login.html'
    success_url = '/'


class BBLogoutView(LogoutView, LoginRequiredMixin):
    template_name = 'accounts/logout.html'


class RegisterUserView(CreateView):
    model = User
    template_name = 'accounts/register_user.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('account/register_done.html')


class RegisterDoneView(TemplateView):
    template_name = 'account/register_done.html.html'






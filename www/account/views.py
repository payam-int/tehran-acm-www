from django.shortcuts import render

# Create your views here.
from django.views.generic import FormView

from account.form import RegisterForm


class Register(FormView):
    form_class = RegisterForm
    template_name = 'account/register.html'


from django.shortcuts import render
from django.contrib.auth.views import LoginView

from django.urls import reverse_lazy


##################################################################################
class Login(LoginView):
    template_name = "dashboard/login.html"

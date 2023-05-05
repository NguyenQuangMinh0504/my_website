from django.http import HttpRequest
from django.shortcuts import render


def register(request: HttpRequest):
    return render(request=request, template_name="register.html", context={})


def login(request: HttpRequest):
    return render(request=request, template_name="login.html", context={})

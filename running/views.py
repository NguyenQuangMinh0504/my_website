from django.shortcuts import render
from django.http import HttpRequest
from db import running_table

# Create your views here.


def index(request: HttpRequest):
    context = {}
    if "user_cookie" in request.COOKIES:
        context["user_cookie"] = request.COOKIES["user_cookie"]
    context["consecutive_day"] = len(running_table.keys())
    return render(request=request,
                  template_name="running/index.html",
                  context=context)

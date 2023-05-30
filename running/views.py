from django.shortcuts import render
from django.http import HttpRequest
from db import cursor

# Create your views here.


def index(request: HttpRequest):
    context = {}
    if "user_cookie" in request.COOKIES:
        context["user_cookie"] = request.COOKIES["user_cookie"]

    cursor.execute("SELECT * FROM running_data")
    context["consecutive_day"] = len(cursor.fetchall())

    return render(request=request,
                  template_name="running/index.html",
                  context=context)

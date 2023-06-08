from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.


def mainpage(request: HttpRequest):
    context = {}
    if "user_cookie" in request.COOKIES:
        context["user_cookie"] = request.COOKIES["user_cookie"]

    response = render(request, "mainpage/mainpage.html", context=context)
    response.set_cookie("foo", "bar")
    response.set_cookie("ad", "tristana")
    # response.set_cookie("support", "thresh")
    return response

from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from db import user_table

matplotlib.use("agg")


def register(request: HttpRequest):
    return render(request=request,
                  template_name="register.html",
                  context={"title": "Đăng ký"})


def login(request: HttpRequest):
    if request.method == "POST":
        data = request.POST
        for i in user_table:
            if i["username"] == data["username"] and \
               i["password"] == data["password"]:
                response = HttpResponseRedirect(redirect_to="/")
                response.set_cookie(key="user_cookie",
                                    value="helloworld",
                                    max_age=30)
                return response
        return HttpResponse("hey")
    return render(request=request,
                  template_name="login.html",
                  context={"title": "Log in"})


def logout(request: HttpRequest):
    response = HttpResponseRedirect(redirect_to="/")
    response.set_cookie("user_cookie", "", max_age=0.01)
    return response


def blog(request: HttpRequest):
    return render(request=request, template_name="blog.html",
                  context={"leader": "good-leader",
                           "title": "Blog cá nhân"})


def blog_detail(request: HttpRequest, leader: str):
    return render(request=request,
                  template_name="blog_detail.html",
                  context={})


def about_me(request: HttpRequest):
    return render(request=request,
                  template_name="about_me.html",
                  context={"title": "About me"})


def homepage(request: HttpRequest):
    context = {}
    context["title"] = "Trang chủ"
    if "user_cookie" in request.COOKIES:
        context["user_cookie"] = request.COOKIES["user_cookie"]
    response = render(request, "homepage.html", context=context)
    return response


def useful_link(request: HttpRequest):
    return render(request, template_name="useful_link.html", context={})

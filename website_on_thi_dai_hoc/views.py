from django.http import HttpRequest
from django.shortcuts import render


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

from django.http import HttpRequest, Http404
from django.shortcuts import render
from db import get_blog_detail, add_blog, get_all_blog


def add_blog_view(request: HttpRequest):
    if request.method == "POST":
        data = request.POST
        print(data)
        add_blog(title=data["title"],
                 snippet=data["snippet"],
                 content=data["content"],
                 )
    return render(request=request, template_name="add_blog.html", context={})


def blog(request: HttpRequest):
    return render(request=request,
                  template_name="blog.html",
                  context={"blogs": get_all_blog()})


def blog_detail(request: HttpRequest, title: str):
    blog_data = get_blog_detail(title=title.replace("-", " "))
    if blog_data is None:
        raise Http404
    return render(request=request,
                  template_name="blog_detail.html",
                  context={"detail": blog_data["content"]})


def about_me(request: HttpRequest):
    return render(request=request,
                  template_name="about_me.html",
                  context={"title": "About me"})


def homepage(request: HttpRequest):
    context = {"title": "Trang chủ", "canonical_link": "https://saugau.com"}
    if "user_cookie" in request.COOKIES:
        context["user_cookie"] = request.COOKIES["user_cookie"]
    response = render(request, "homepage.html", context=context)
    return response

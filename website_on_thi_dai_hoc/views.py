from django.http import HttpRequest, Http404, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from db import (get_blog_detail, add_blog, get_all_blog,
                get_all_comment, add_comment, get_running_data)


def add_blog_view(request: HttpRequest):
    if request.method == "POST":
        data = request.POST
        print(data)
        add_blog(title=data["title"],
                 snippet=data["snippet"],
                 content=data["content"],
                 )
    return render(request=request, template_name="add_blog.html", context={
        "title": "Tạo blog",
        "canonical_links": "https://saugau.com/add-blog/"
    })


def blog(request: HttpRequest):
    return render(request=request,
                  template_name="blog.html",
                  context={"blogs": get_all_blog(),
                           "title": "Blog cá nhân",
                           "canonical_link": "https://saugau.com/blog/"})


def blog_detail(request: HttpRequest, title: str):
    blog_data = get_blog_detail(title=title.replace("-", " "))
    if blog_data is None:
        raise Http404
    return render(
        request=request,
        template_name="blog_detail.html",
        context={
            "detail": blog_data["content"],
            "id": blog_data["id"],
            "title": blog_data["title"],
            "comments": get_all_comment(blog_data["id"],),
            "canonical_link": f"https://saugau.com/blog/{title}/"}
            )


def about_me(request: HttpRequest):
    return render(request=request,
                  template_name="about_me.html",
                  context={"title": "About me",
                           "canonical_link": "https://saugau.com/about-me/"})


def homepage(request: HttpRequest):
    context = {"title": "Trang chủ", "canonical_link": "https://saugau.com"}
    if "user_cookie" in request.COOKIES:
        context["user_cookie"] = request.COOKIES["user_cookie"]
    response = render(request, "homepage.html", context=context)
    return response


def add_comment_view(request: HttpRequest, blog_id):
    if request.method == "POST":
        add_comment(blog_id=blog_id, content=request.POST["content"])
    return HttpResponseRedirect(reverse(viewname="blog-detail",
                                        args=[request.POST["title"]])
                                )


def running_view(request: HttpRequest):
    context = {}
    context["title"] = "Chạy bộ"
    context["canonical_link"] = "https://saugau.com/running/"
    context["consecutive_day"] = len(get_running_data())
    return render(request=request,
                  template_name="running.html",
                  context=context)

from django.http import HttpRequest, Http404, HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
import json
import subprocess
import os
from .utils import generate_graph, send_telegram_notification, add_metadata
from django.urls import reverse
from db import (get_blog_detail, add_blog, get_all_blog,
                get_all_comment, add_comment, get_running_data, edit_blog,
                increment_view_counter, add_running_data, add_other_data, get_all_tag, get_blog_tag,
                get_all_blog_with_tag)
from config import IP_GRAPH_LINK, REQUEST_GRAPH_LINK, DATE_FORMAT


def add_blog_view(request: HttpRequest):
    meta_data = add_metadata(request)
    if meta_data != "":
        send_telegram_notification(
            reverse(viewname="add-blog") + meta_data
        )

    if request.method == "POST":
        data = request.POST
        add_blog(title=data["title"],
                 snippet=data["snippet"],
                 content=data["content"],
                 )

    return render(request=request, template_name="add_blog.html", context={
        "title": "Tạo blog",
        "canonical_links": "https://saugau.com/add-blog"
    })


def blog(request: HttpRequest):
    meta_data = add_metadata(request)
    if meta_data != "":
        send_telegram_notification(
            reverse(viewname="blog") + meta_data
        )

    order = request.GET.get("order")
    if order is not None:
        blogs = get_all_blog(order=order)
    else:
        blogs = get_all_blog(order=None)

    tag = request.GET.get("tag")
    if tag is not None:
        blogs = get_all_blog_with_tag(tag_name=tag)

    tags = get_all_tag()
    # Reformat date from datetime -> string
    for blog in blogs:
        blog["date"] = blog["date"].strftime(DATE_FORMAT)
        blog["tags"] = get_blog_tag(blog_id=blog["id"])
    return render(request=request,
                  template_name="blog.html",
                  context={"blogs": blogs,
                           "title": "Blog cá nhân",
                           "order": order,
                           "tags": tags,
                           "canonical_link": "https://saugau.com/blog"})


def blog_detail(request: HttpRequest, title: str):
    meta_data = add_metadata(request)
    if meta_data != "":
        send_telegram_notification(
            reverse(viewname="blog-detail", args=[title]) + meta_data
            )

    increment_view_counter(title=title.replace("-", " "))
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
            "total_view": blog_data["total_view"],
            "date": blog_data["date"].strftime(DATE_FORMAT),
            "comments": get_all_comment(blog_data["id"],),
            "canonical_link": f"https://saugau.com/blog/{title}"}
            )


def edit_blog_view(request: HttpRequest, title: str):
    meta_data = add_metadata(request)
    if meta_data != "":
        send_telegram_notification(
            reverse(viewname="edit-blog", args=[title]) + meta_data)
    title = title.replace("-", " ")
    blog_data = get_blog_detail(title=title.replace("-", " "))
    if blog_data is None:
        raise Http404
    if request.method == "POST":
        data = request.POST
        edit_blog(old_title=title, new_title=data["title"],
                  snippet=data["snippet"], content=data["content"])
        return HttpResponseRedirect(reverse(viewname="blog"))
    return render(request=request, template_name="edit_blog.html",
                  context=blog_data)


def about_me(request: HttpRequest):
    meta_data = add_metadata(request)
    if meta_data != "":
        send_telegram_notification(
            reverse(viewname="about-me") + meta_data)
    return render(request=request,
                  template_name="about_me.html",
                  context={"title": "About me",
                           "canonical_link": "https://saugau.com/about-me"})


def list_100_view(request: HttpRequest):
    meta_data = add_metadata(request)
    if meta_data != "":
        send_telegram_notification(
            reverse(viewname="list-100") + meta_data)
    return render(request=request,
                  template_name="list_100.html",
                  context={"title": "List 100",
                           "canonical_link": "https://saugau.com/list-100"})


def homepage(request: HttpRequest):
    # Disable sending telegram in homepage
    meta_data = add_metadata(request)
    if meta_data != "":
        send_telegram_notification("homepage" + meta_data)
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
    # send_telegram_notification(
    #     reverse(viewname="running") + add_metadata(request)
    #     )
    if request.method == "POST":
        data = request.POST
        add_running_data(date=data["date"],
                         duration=data["duration"],
                         distance=data["distance"])
        generate_graph()
        return HttpResponseRedirect(reverse(viewname="running"))
    context = {}
    context["title"] = "Chạy bộ"
    context["canonical_link"] = "https://saugau.com/running"
    counter = 0
    for row in reversed(get_running_data()):
        if row["distance"] > 0:
            counter += 1
        else:
            break
    context["consecutive_day"] = counter
    return render(request=request,
                  template_name="running.html",
                  context=context)


def website_traffic_view(request: HttpRequest):
    # send_telegram_notification(
    #     reverse(viewname="website-traffic") + add_metadata(request))
    context = {}
    context["title"] = "Website traffic"
    context["canonical_link"] = "https://saugau.com/website-traffic"
    context["ip_graph_link"] = IP_GRAPH_LINK
    context["request_graph_link"] = REQUEST_GRAPH_LINK
    return render(request=request, template_name="website_traffic.html",
                  context=context)


def statistics_view(request: HttpRequest):
    # send_telegram_notification(
    #     reverse(viewname="statistics") + add_metadata(request))
    if request.method == "POST":
        data = request.POST
        add_other_data(date=data["date"], study_time=data["study_time"],
                       play_time=data["play_time"])
        generate_graph()
        return HttpResponseRedirect(redirect_to=reverse(viewname="statistics"))
    context = {}
    context["title"] = "Statistics"
    context["canonical_link"] = "https://saugau.com/statistics"
    return render(request=request, template_name="statistics.html",
                  context=context)


def add_data_view(request: HttpRequest):
    send_telegram_notification(
        reverse(viewname="add-data") + add_metadata(request))
    context = {}
    context["title"] = "Add data"
    context["canonical_link"] = "https://saugau.com/add-data"
    return render(request=request, template_name="add_data.html",
                  context=context)


def test_view(request: HttpRequest):
    send_telegram_notification(
        reverse(viewname="test") + add_metadata(request))
    return render(request=request, template_name="test.html", context={})


@csrf_exempt
def github_view(request: HttpRequest):
    data = json.loads(request.POST["payload"])
    os.chdir("/opt/my_website")
    subprocess.run(["git", "pull"])
    if "django_my_website/requirements.txt" in data["head_commit"]["modified"]:
        command = [
            '/opt/my_website_venv/bin/python3.9',
            '-m',
            'pip',
            'install',
            '-r',
            '/opt/my_website/django_my_website/requirements.txt'
            ]
        subprocess.run(command, check=True)
        send_telegram_notification("Update environment successfully!!!")
    return HttpResponse(content="Success")

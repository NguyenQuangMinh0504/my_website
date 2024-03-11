from django.http import HttpRequest
from django.shortcuts import render
from .utils import send_telegram_notification, add_metadata
from django.urls import reverse
from config import IP_GRAPH_LINK, REQUEST_GRAPH_LINK


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
    # meta_data = add_metadata(request)
    # if meta_data != "":
    #     send_telegram_notification("homepage" + meta_data)
    context = {"title": "Trang chủ", "canonical_link": "https://saugau.com"}
    if "user_cookie" in request.COOKIES:
        context["user_cookie"] = request.COOKIES["user_cookie"]
    response = render(request, "homepage.html", context=context)
    return response


def test_view(request: HttpRequest):
    # send_telegram_notification(
    #     reverse(viewname="test") + add_metadata(request))
    return render(request=request, template_name="test.html", context={})

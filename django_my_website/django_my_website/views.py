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


def add_data_view(request: HttpRequest):
    send_telegram_notification(
        reverse(viewname="add-data") + add_metadata(request))
    context = {}
    context["title"] = "Add data"
    context["canonical_link"] = "https://saugau.com/add-data"
    return render(request=request, template_name="add_data.html",
                  context=context)


def test_view(request: HttpRequest):
    # send_telegram_notification(
    #     reverse(viewname="test") + add_metadata(request))
    return render(request=request, template_name="test.html", context={})

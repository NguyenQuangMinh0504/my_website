from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render
from .utils import generate_graph, send_telegram_notification, add_metadata
from django.urls import reverse
from db import (get_running_data,
                add_running_data, add_other_data)
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

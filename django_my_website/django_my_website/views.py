"""Django view, Handle logic of website"""
from django.http import HttpRequest
from django.shortcuts import render
from django.urls import reverse
from .utils import send_telegram_notification, add_metadata


def about_me(request: HttpRequest):
    """About me view """
    meta_data = add_metadata(request)
    if meta_data != "":
        send_telegram_notification(
            reverse(viewname="about-me") + meta_data)
    return render(request=request,
                  template_name="about_me.html",
                  context={"title": "About me",
                           "canonical_link": "https://saugau.com/about-me"})


def list_100_view(request: HttpRequest):
    """List 100 view"""
    meta_data = add_metadata(request)
    if meta_data != "":
        send_telegram_notification(
            reverse(viewname="list-100") + meta_data)
    return render(request=request,
                  template_name="list_100.html",
                  context={"title": "List 100",
                           "canonical_link": "https://saugau.com/list-100"})


def homepage(request: HttpRequest):
    """Homepage view"""
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
    """Test view"""
    # send_telegram_notification(
    #     reverse(viewname="test") + add_metadata(request))
    return render(request=request, template_name="test.html", context={})

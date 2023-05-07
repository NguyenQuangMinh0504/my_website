from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from db import user_table


def register(request: HttpRequest):
    return render(request=request, template_name="register.html", context={})


def login(request: HttpRequest):
    if request.method == "POST":
        data = request.POST
        for i in user_table:
            if i["username"] == data["username"] and i["password"] == data["password"]:
                response = HttpResponseRedirect(redirect_to="/")
                response.set_cookie(key="user_cookie", value="helloworld", max_age=30)
                return response
        return HttpResponse("hey")
    return render(request=request, template_name="login.html", context={})


def logout(request: HttpRequest):
    response = HttpResponseRedirect(redirect_to="/")
    response.set_cookie("user_cookie", "", max_age=0.01)
    return response

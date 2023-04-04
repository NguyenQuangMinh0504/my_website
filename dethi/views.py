from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.

def dethi(request: HttpRequest):
    print("Request body is: ", request.body)
    print("Resquest content type: ", request.content_type)
    print("HTTP POST is: ", request.POST)
    if request.method == "POST":
        return HttpResponse("Hello World")
    return render(request, "dethi/something.html", {})

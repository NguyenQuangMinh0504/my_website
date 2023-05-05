from django.shortcuts import render
from django.http import HttpRequest
from db import running_table

# Create your views here.


def index(request: HttpRequest):
    return render(request, "running/index.html",
                  {"consecutive_day": len(running_table.keys())})

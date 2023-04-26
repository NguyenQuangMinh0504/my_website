from django.shortcuts import render
from .data import running_list

# Create your views here.


def index(request):
    return render(request, "running/index.html", {})

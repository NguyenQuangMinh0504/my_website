from django.shortcuts import render
from redis import Redis
redis_client = Redis(host="127.0.0.1", db=0, port=6379)

# Create your views here.


def index(request):
    return render(request, "running/index.html",
                  {"consecutive_day": len(redis_client.keys())})

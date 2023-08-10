from django.shortcuts import render
from django.http import HttpRequest
from mysql import connector

# Create your views here.


def index(request: HttpRequest):
    context = {}
    context["title"] = "Chạy bộ"
    context["canonical_link"] = "https://saugau.com/running/"
    if "user_cookie" in request.COOKIES:
        context["user_cookie"] = request.COOKIES["user_cookie"]
    cnx = connector.connect(user="root",
                            password="qmqmqm8c3",
                            database="my_data")
    cursor = cnx.cursor()
    cursor.execute("SELECT * FROM running_data")
    context["consecutive_day"] = len(cursor.fetchall())
    cursor.close()
    cnx.close()
    return render(request=request,
                  template_name="running/index.html",
                  context=context)

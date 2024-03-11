"""
URL configuration for django_my_website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from .views import (about_me, homepage,
                    website_traffic_view, test_view,
                    statistics_view, add_data_view, list_100_view)

urlpatterns = [
    path(route="", view=homepage, name="homepage"),
    path(route="accounts/", view=include("django.contrib.auth.urls")),
    path('admin', admin.site.urls),
    path(route="blog/", view=include("blog.urls")),
    path(route="about-me", view=about_me, name="about-me"),
    path(route="website-traffic", view=website_traffic_view,
         name="website-traffic"),
    path(route="test", view=test_view, name="test"),
    path(route="statistics", view=statistics_view, name="statistics"),
    path(route="add-data", view=add_data_view, name="add-data"),
    path(route="list-100", view=list_100_view, name="list-100"),
]

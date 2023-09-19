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
from django.urls import path
from .views import (blog, blog_detail, about_me, homepage,
                    add_blog_view, add_comment_view, running_view,
                    edit_blog_view, website_traffic_view, test_view,
                    statistics_view, add_data_view)

urlpatterns = [
    path(route="", view=homepage, name="homepage"),
    path('admin', admin.site.urls),
    path("running", view=running_view, name="running"),
    path(route="blog", view=blog, name="blog"),
    path(route="add-blog", view=add_blog_view, name="add-blog"),
    path(route="about-me", view=about_me, name="about-me"),
    path(route="blog/<str:title>", view=blog_detail, name="blog-detail"),
    path(route="blog/add-comment/<int:blog_id>",
         view=add_comment_view, name="add-comment"),
    path(route="edit-blog/<str:title>", view=edit_blog_view,
         name="edit-blog"),
    path(route="website-traffic", view=website_traffic_view,
         name="website-traffic"),
    path(route="test", view=test_view, name="test"),
    path(route="statistics", view=statistics_view, name="statistics"),
    path(route="add-data", view=add_data_view, name="add-data"),
]

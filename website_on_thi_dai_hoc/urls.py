"""website_on_thi_dai_hoc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from .views import register, login

urlpatterns = [
    path("polls/", include("polls.urls")),
    path("dethi/", include("dethi.urls")),
    path("login/", view=login, name="login"),
    path(route="register/", view=register, name="register"),
    path('admin/', admin.site.urls),
    path("running/", include("running.urls")),
    path("", include("mainpage.urls")),
]

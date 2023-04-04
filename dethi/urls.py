from django.urls import path
from . import views
app_name = "dethi"
urlpatterns = [
    # ex: /dethi
    path(route="", view=views.dethi, name="dethi"),
]
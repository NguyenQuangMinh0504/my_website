from django.urls import path
from .views import blog, blog_detail, add_comment_view

urlpatterns = [
    path(route="", view=blog, name="blog"),
    path(route="<str:title>", view=blog_detail, name="blog-detail"),
    path(route="add-comment/<int:blog_id>", view=add_comment_view, name="add-comment"),
]

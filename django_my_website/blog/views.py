from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.utils.text import slugify

from config import DATE_FORMAT
from db import get_all_blog, get_all_blog_with_tag, get_all_tag, get_blog_tag, get_all_comment, increment_view_counter, add_comment
from django_my_website.utils import add_metadata, send_telegram_notification

from .models import Blog


def blog(request: HttpRequest):
    meta_data = add_metadata(request)
    if meta_data != "":
        send_telegram_notification(
            reverse(viewname="blog") + meta_data
        )
    order = request.GET.get("order")

    if order is not None:
        # blogs = get_all_blog(order=order)
        blogs = Blog.objects.order_by("total_view")
    else:
        # blogs = get_all_blog(order=None)
        blogs = Blog.objects.order_by("-id")

    tag = request.GET.get("tag")
    if tag is not None:
        blogs = get_all_blog_with_tag(tag_name=tag)

    tags = get_all_tag()
    # Reformat date from datetime -> string
    # for blog in blogs:
    #     blog["date"] = blog["date"].strftime(DATE_FORMAT)
    #     # handle slugify error
    #     blog["slug_url"] = slugify(blog["title"].replace("đ", "d").replace("Đ", "D"))

    for blog in blogs:
        blog.slug_url = slugify(blog.title.replace("đ", "d").replace("Đ", "D"))
        blog.tags = get_blog_tag(blog_id=blog.id)

    return render(request=request,
                  template_name="blog.html",
                  context={"blogs": blogs,
                           "title": "Blog cá nhân",
                           "order": order,
                           "tags": tags,
                           "canonical_link": "https://saugau.com/blog"})


def blog_detail(request: HttpRequest, title: str):
    meta_data = add_metadata(request)
    if meta_data != "":
        send_telegram_notification(
            reverse(viewname="blog-detail", args=[title]) + meta_data
            )

    increment_view_counter(title=title.replace("-", " "))
    blog = get_object_or_404(Blog, title=title.replace("-", " "))
    return render(
        request=request,
        template_name="blog_detail.html",
        context={
            "blog": blog,
            "comments": get_all_comment(blog.id,),
            "canonical_link": f"https://saugau.com/blog/{title}"}
            )


def add_comment_view(request: HttpRequest, blog_id):
    if request.method == "POST":
        add_comment(blog_id=blog_id, content=request.POST["content"])
    return HttpResponseRedirect(reverse(viewname="blog-detail",
                                        args=[request.POST["title"]])
                                )

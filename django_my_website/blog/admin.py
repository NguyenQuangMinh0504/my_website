"""Admin page"""
from django.contrib import admin
from .models import Blog, Tag, BlogTag, Comment
# Register your models here.

admin.site.register([Blog, Tag, BlogTag, Comment])

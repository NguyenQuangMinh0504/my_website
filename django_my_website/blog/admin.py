"""Admin page"""
from django.contrib import admin
from .models import Blog, Tag, Blog_Tag, Comment
# Register your models here.

admin.site.register([Blog, Tag, Blog_Tag, Comment])

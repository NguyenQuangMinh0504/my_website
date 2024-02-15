from django.contrib import admin
from .models import Blog, Tag, Blog_Tag
# Register your models here.

admin.site.register([Blog, Tag, Blog_Tag])

"""BLog App Config"""
from django.apps import AppConfig


class BlogConfig(AppConfig):
    """Blog App Config"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'

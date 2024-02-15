from django.db import models

# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=255)
    snippet = models.CharField(max_length=255)
    content = models.TextField()
    total_view = models.SmallIntegerField(default=0)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        db_table = "blog"

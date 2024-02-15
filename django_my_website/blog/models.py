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


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "tag"


class Blog_Tag(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.blog)

    class Meta:
        db_table = "blog_tag"
        unique_together = ("blog", "tag")

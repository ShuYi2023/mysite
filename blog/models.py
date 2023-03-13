from django.db import models
from django.contrib.auth.models import User


STATUS = (
    (0, "Draft"),
    (1, "Publish")
)


class Post(models.Model):
    title = models.CharField(max_length=200)
    section = models.CharField(max_length=200)
    project = models.CharField(max_length=200)
    chapter = models.CharField(max_length=200)
    level = models.CharField(max_length=200)
    # slug = models.SlugField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    views = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['-updated_on']

    def __str__(self):
        return self.title

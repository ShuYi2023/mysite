from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse
from taggit.managers import TaggableManager

# STATUS = (
#     (0, "Draft"),
#     (1, "Publish")
# )

class ArticleColumn(models.Model):
    """
    栏目的 Model
    """
    # 栏目标题
    title = models.CharField(max_length=100, blank=True)
    # 创建时间
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class ArticlePost(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)

    section = models.CharField(max_length=200)
    project = models.CharField(max_length=200)
    chapter = models.CharField(max_length=200)
    level = models.CharField(max_length=200)
    # slug = models.SlugField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200)
    # status = models.IntegerField(choices=STATUS, default=0)
    views = models.PositiveIntegerField(default=0)
    tags = TaggableManager(blank=True)

    for_vip = models.BooleanField(default=False)

    # 文章栏目的 “一对多” 外键
    column = models.ForeignKey(
        ArticleColumn,
        null=True,
        blank=True,
        on_delete=models.CASCADE,
        related_name='article'
    )

    class Meta:
        ordering = ['-updated_on']

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        # return reverse('article:article_detail', args=[self.slug])
        return reverse('article:article_detail', args=[self.id])
    


from django.contrib import admin
from .models import ArticlePost

# 注册ArticlePost到admin中, 这样才能用admin网址管理ArticlePost数据库
admin.site.register(ArticlePost)

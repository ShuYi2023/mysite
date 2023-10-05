from django.contrib import admin
from .models import ArticlePost
from .models import ArticleColumn

# 注册ArticlePost到admin中, 这样才能用admin网址管理ArticlePost数据库
admin.site.register(ArticlePost)

# 注册ArticleColumn
admin.site.register(ArticleColumn)

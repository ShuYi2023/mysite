from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
    path('article-list/', views.article_list, name='article_list'),  # 访问的网址要设置为: article/article-list/
    path('article-detail/<slug:slug>', views.article_detail, name='article_detail'),
    path('article-create/', views.article_create, name='article_create'),
    path('article-delete/<slug:slug>/', views.article_delete, name='article_delete'),
    path('article-update/<slug:slug>/', views.article_update, name='article_update'),
]

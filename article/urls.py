from django.urls import path
from . import views

app_name = 'article'

urlpatterns = [
    path('', views.article_list, name='article_list'),  # 访问的网址是: article/article-list/
    path('article-list/', views.article_list, name='article_list'),  # 访问的网址是: article/article-list/
    # path('article-detail/<slug:slug>', views.article_detail, name='article_detail'),
    path('article-detail/<int:id>/', views.article_detail, name='article_detail'),
    path('article-create/', views.article_create, name='article_create'),
    path('article-delete/<int:id>/', views.article_delete, name='article_delete'),
    path('article-update/<int:id>/', views.article_update, name='article_update'),
    # path('article-list/<str:tag>', views.tag_list, name='tag_list'),  # 访问的网址是: article/tag-list/
]

from . import views
from django.urls import path

urlpatterns = [
    # path('', views.PostList.as_view(), name='home'),  # url: 192.168.0.244:8000
    path('', views.post_list, name='home'),  # url: 192.168.0.244:8000
    path('<slug:slug>', views.PostDetail.as_view(), name='post_detail'), # http://127.0.0.1:8000/django002ch02
]

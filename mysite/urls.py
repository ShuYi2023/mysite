"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    1_1. Max经验: path 要在makemigrations和migrate之后再添加, 否则报错 No module named 'comment.urls
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),  # 访问的时候, slash不能省略, localhost:8000/admin/
    # path('', include('blog.urls')),
    # 下面的path 要在makemigrations和migrate之后再添加, 否则报错 No module named 'comment.urls
    path('article/', include('article.urls', namespace='article')),
    path('comment/', include('comment.urls', namespace='comment')),
    # 用户管理
    path('userprofile/', include('userprofile.urls', namespace='userprofile')),
]

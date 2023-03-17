from django.urls import path
from . import views

app_name = 'comment'

urlpatterns = [
    path('post-comment/<slug:slug>', views.post_comment, name='post_comment'),
]

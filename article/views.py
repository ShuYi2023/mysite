from django.shortcuts import render
from django.http import HttpResponse
from .models import ArticlePost

def article_list(request):
    # 取出所有文章
    articles = ArticlePost.objects.all()
    context = {'articles': articles}
    # return HttpResponse("Hello World.")
    return render(request, 'article/list.html', context)

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ArticlePost
from .forms import ArticlePostForm
from django.contrib.auth.models import User
import markdown  # 用于处理 Markdown 格式
import random
import re
import datetime

# 文章列表
def article_list(request):
    # 取出所有文章
    articles = ArticlePost.objects.all()
    context = {'articles': articles}
    # return HttpResponse("Hello World.")
    return render(request, 'article/list.html', context)

# 文章详情
def article_detail(request, slug):
    """
    从数据库中取出文章, 判断文章是Markdown格式, 还是HTML格式。
    如果是HTML格式, 则不改动。
    如果是Markdown格式, 则用Markdown模块解析成HTML
    """

    article = ArticlePost.objects.get(slug=slug)

    if '</h2>' in article.body: # 如果文章中已经有html标签了, 就不转换
        context = {"article": article}
        return render(request, 'article/detail.html', context)

    # 如果body中没有html标签, 表明是Markdown格式的文件↓
    else:
        article.body = markdown.markdown(article.body,
        extensions=[
        # 包含 缩写、表格等常用扩展
        'markdown.extensions.extra',
        # 语法高亮扩展
        'markdown.extensions.codehilite',
        ])

        context = {"article": article}
        return render(request, 'article/detail.html', context)

def article_create(request):
    # 判断用户是否提交数据
    if request.method == "POST":
        article_post_form = ArticlePostForm(data=request.POST)
        # 判断提交的数据是否满足模型的要求
        if article_post_form.is_valid:
            # 保存数据, 但暂时不提交到数据库中
            new_article = article_post_form.save(commit=False)
            sue_or_max=random.choice(['max','ShuYi'])
            new_article.author = User.objects.get(username=sue_or_max)

            # 用时间戳生成slug
            now_str = str(datetime.datetime.now())
            now_str = re.sub('[.:-]','', str(now_str)[10:])
            new_article.slug = 'ugc' + now_str.strip()

            # 对其他的键赋值
            new_article.section = 'ugc'
            new_article.project = 'prj01'
            new_article.chapter = 'ch001'
            new_article.level = 'beginner'

            new_article.save()
            return redirect("article:article_list")
        else:
            return HttpResponse("表单有错误, 请重新填写")
    else:
        # 创建表单类实例
        article_post_form = ArticlePostForm()
        context = {'article_post_form': article_post_form}
        return render(request, 'article/create.html', context)

def article_delete(request, slug):
    article = ArticlePost.objects.get(slug=slug)
    article.delete()
    return redirect("article:article_list")

def article_update(request, slug):
    """本函数用于修改文章"""
    article = ArticlePost.objects.get(slug=slug)

    if request.method=="POST":
        article_post_form = ArticlePostForm(data=request.POST)
        if article_post_form.is_valid:
            article.title = request.POST['title']
            article.body = request.POST['body']
            article.save()
            return redirect("article:article_detail", slug=slug)
        else:
            return HttpResponse("表单内容有误，请重新填写。")
        
    # 如果用户 GET 请求获取数据
    else:
        # 创建表单类实例
        article_post_form = ArticlePostForm()
        # 赋值上下文，将 article 文章对象也传递进去，以便提取旧的内容
        context = { 'article': article, 'article_post_form': article_post_form }
        # 将响应返回到模板中
        return render(request, 'article/update.html', context)

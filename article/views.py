from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ArticlePost
from .forms import ArticlePostForm
from django.contrib.auth.models import User
import markdown  # 用于处理 Markdown 格式
import random
import re
import datetime
from comment.models import Comment
from django.core.paginator import Paginator
from taggit.models import Tag

# 文章列表
def article_list(request):
    # 取出所有文章
    article_list = ArticlePost.objects.all()
    tags = Tag.objects.all()

    paginator = Paginator(article_list, 4)
    page = request.GET.get('page')
    articles = paginator.get_page(page)

    context = {'articles': articles, 'tags': tags}
    return render(request, 'article/list.html', context)

# 文章详情
# def article_detail(request, slug):
def article_detail(request, id):
    """
    从数据库中取出文章--文章已经变成HTML格式了, 不用Markdown模块解析了。
    """

    # article = ArticlePost.objects.get(slug=slug)
    article = ArticlePost.objects.get(id=id)

    article.views += 1
    article.save(update_fields=['views'])

    # art_id = article.id
    # comments = Comment.objects.filter(slug=slug)
    comments = Comment.objects.filter(article=id)


    # if '</h2>' in article.body: # 如果文章中已经有html标签了, 就不转换
    #     pass
    # # 如果body中没有html标签, 表明是Markdown格式的文件↓
    # else:
    #     article.body = markdown.markdown(article.body,
    #     extensions=[
    #     # 包含 缩写、表格等常用扩展
    #     'markdown.extensions.extra',
    #     # 语法高亮扩展
    #     'markdown.extensions.codehilite',
    #     ])

    # context = { 'article': article, 'toc': md.toc, 'comments': comments }
    context = { 'article': article, 'comments': comments }
    return render(request, 'article/detail.html', context)
    #return render(request, 'post_detail.html', context)


def article_create(request):
    # 判断用户是否提交数据
    if request.method == "POST":
        article_post_form = ArticlePostForm(data=request.POST)
        # 判断提交的数据是否满足模型的要求
        if article_post_form.is_valid:
            # 保存数据, 但暂时不提交到数据库中
            new_article = article_post_form.save(commit=False)
            # sue_or_max=random.choice(['max','ShuYi'])
            sue_or_max='max'
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
            article_post_form.save_m2m()
            return redirect("article:article_list")
        else:
            return HttpResponse("表单有错误, 请重新填写")
    else:
        # 创建表单类实例
        article_post_form = ArticlePostForm()
        context = {'article_post_form': article_post_form}
        return render(request, 'article/create.html', context)

def article_delete(request, id):
    article = ArticlePost.objects.get(id=id)
    article.delete()
    return redirect("article:article_list")

def article_update(request, id):
    """本函数用于修改文章"""
    article = ArticlePost.objects.get(id=id)

    if request.method=="POST":
        article_post_form = ArticlePostForm(data=request.POST)
        if article_post_form.is_valid:
            article.title = request.POST['title']
            article.body = request.POST['body']
            article.save()
            return redirect("article:article_detail", id=id)
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

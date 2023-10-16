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
from django.contrib.auth.decorators import login_required, user_passes_test

# 文章列表
def article_list(request):
    # 取出所有文章, tags, sections
    article_list = ArticlePost.objects.all()
    tags = Tag.objects.all()
    # 取出字段section中的所有值
    sects = ArticlePost.objects.values_list('section', flat=True).distinct()
    sects = list(set(section.lower() for section in sects))

    sect = request.GET.get('sect', 'gao') # sect的default的值是'gao'
    tag = request.GET.get('tag')
    if tag is not None:
        article_list = article_list.filter(tags__name__in=[tag]).order_by('title')
    else:
        article_list = article_list.filter(section=sect).order_by('title')

    paginator = Paginator(article_list, 8)
    page = request.GET.get('page')
    articles = paginator.get_page(page)

    context = {'articles': articles, 'tags': tags, 'sects': sects}
    return render(request, 'article/list.html', context)

# 文章详情
# def article_detail(request, slug):
# @login_required
def article_detail(request, id):
    """
    从数据库中取出文章--文章已经变成HTML格式了, 不用Markdown模块解析了。
    """

    # article = ArticlePost.objects.get(slug=slug)
    article = ArticlePost.objects.get(id=id)

    # Check group membership
    is_vip = request.user.groups.filter(name='VIP').exists()
    if request.user.is_superuser:
        is_vip = True

    article.views += 1
    article.save(update_fields=['views'])
    comments = Comment.objects.filter(article=id)
    context = { 'article': article, 'comments': comments }

    if not article.for_vip:
            return render(request, 'article/detail.html', context)
    else: # article.for_vip:
        if not is_vip:
            return render(request, 'article/not_a_vip.html')
        if is_vip:
            return render(request, 'article/detail.html', context)

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

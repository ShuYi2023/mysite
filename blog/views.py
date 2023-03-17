from django.shortcuts import render
from django.views import generic
from .models import Post
from comment.models import Comment
from django.core.paginator import Paginator


class PostList(generic.ListView):
    model = Post
    template_name = 'index.html'

    queryset = Post.objects.filter(status=1).order_by('-created_on')
    context_object_name = 'post_list'
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 加入自己的参数
        context['sections'] = set([obj.section for obj in Post.objects.all()])

        object_list = context['post_list']
        paginator = Paginator(object_list, self.paginate_by)
        page = self.request.GET.get('page')
        context['post_list'] = paginator.get_page(page)
        return context

def post_list(request):
    post_list = Post.objects.all()

    paginator = Paginator(post_list, 2)

    page = request.GET.get('page')

    posts = paginator.get_page(page)

    context = {'posts': posts}
    context['sections'] = set([post.section for post in post_list])

    return render(request, 'index.html', context)


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj.views += 1
        obj.save()
        return obj

# 文章详情
def post_detail(request, slug):
    # 取出相应的文章
    post = Post.objects.get(slug=slug)

    # 取出文章评论
    comments = Comment.objects.filter(slug=slug)

    # 需要传递给模板的对象
    context = { 'post': post, 'comments': comments}
    # 载入模板，并返回context对象
    return render(request, 'post_detail.html', context)

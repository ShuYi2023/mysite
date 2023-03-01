from django.shortcuts import render
from django.views import generic
from .models import Post


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

    # sections = set([obj.section for obj in model.objects.all()])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # 加入自己的参数
        context['sections'] = set([obj.section for obj in Post.objects.all()])
        return context


class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)
        obj.views += 1
        obj.save()
        return obj


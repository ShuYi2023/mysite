"""
下面的代码把 yfilename转换到 imgs 文件夹中，文件夹中包含 yfilename 中的所有图片，以及转换后的 html。
"""
from pathlib import Path
import datetime
from django.utils import timezone
import django
import os
import re
import random
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model, get_user
from blog.models import Post

sections = ["django", 'animation', 'ue', 'u3d', 'tailwind']
sue_or_max=random.choice(['max','ShuYi'])
yauthor = User.objects.get(username=sue_or_max)
# user_instance = get_user_model().objects.get(username=file_meta["author"])

file_meta = {"section": "django", # ue, u3d, tailwind, python, ksp
             "project": "001",
             "chapter": "ch01",
             "title": "",
             "slug": "", # slug field
             "author": yauthor, # Foreign Key
             "updated_on": timezone.now(), # data_time
             # "created_on": timezone.now(),
             "content": "", # text
             "level": "beginner",
             "status": 1,  # integer
             }


# *** 获得 html 文件的绝对路径
html_path = '/Users/maxmacboookpro2019/my_projs/10django_prjs/mysite/static/blog/django/001/output.html'

print("")

# *** 读取html 的内容
text_for_post = ''
with open(html_path, 'r', encoding='UTF-8') as f:
    text_for_post = f.read()


# 在数据库中更新或者创建新的内容
file_meta["content"] = text_for_post
file_meta["title"] = "sue_test_html"
file_meta['slug'] = file_meta["section"] + file_meta["project"] + file_meta["chapter"]

slug = file_meta["slug"]

# ↓ 避免: RuntimeWarning: DateTimeField received a naive datetime 问题
if not Post.objects.get(slug = slug):
    file_meta["created_on"] = timezone.now()

obj, created = Post.objects.update_or_create(
    slug = file_meta["slug"],
    defaults = file_meta
    )

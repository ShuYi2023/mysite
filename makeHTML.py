"""
下面的代码把 yfilename转换到 imgs 文件夹中，文件夹中包含 yfilename 中的所有图片，以及转换后的 html。
"""
from pathlib import Path
import datetime
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
             "project": "002",
             "chapter": "ch01",
             "title": "",
             "slug": "", # slug field
             "author": yauthor, # Foreign Key
             "updated_on": datetime.datetime.now(), # data_time
             "created_on": datetime.datetime.now(),
             "content": "", # text
             "level": "beginner",
             "status": 1,  # integer
             }
file_meta['slug'] = file_meta["section"] + file_meta["project"] + file_meta["chapter"]

# 创建output_path, 用于保存图片
base_dir = Path(__file__).resolve().parent #
output_path = os.path.join(base_dir, 'static', 'blog',
                           file_meta['section'], file_meta['project'],
                           file_meta["chapter"])
if not os.path.exists(output_path):
    os.makedirs(output_path)
    print(f"创建了{output_path}.")
else:
    print(f"已存在{output_path}, 无需创建.")


# *** 获得下载下来的 docx 的文件名和扩展名
downloads_path = '/Users/maxmacboookpro2019/Downloads/'
f_list = os.listdir(downloads_path)
docs_list = []
for each_file in f_list:
    name_each_file, ext = os.path.splitext(each_file)  # name of each file
    if (ext == ".docx") and ("~" not in name_each_file):
        docs_list.append(each_file)

for i in range(len(docs_list)):
    print(f'{i}-{docs_list[i]}')
j = int(input("请选择要处理的文件的序号: "))
ydoc_name_ext = docs_list[j]  # name and ext, 文件名和扩展名

ydoc_name, yfile_extension = os.path.splitext(ydoc_name_ext)  # 文件名+扩展名
# ydoc_path = os.path.join(base_dir, 'toHTML', 'docs', ydoc_name) + yfile_extension
ydoc_path = downloads_path + ydoc_name_ext

# output_path = os.path.join(base_dir, 'toHTML', 'imgs')
os.system(f"mammoth {ydoc_path} --output-dir={output_path}")


# *** 获得 html 文件的绝对路径
html_path = os.path.join(output_path, ydoc_name) + '.html'

print("")

# *** 读取html 的内容
text_for_post = ''
with open(html_path, 'r', encoding='UTF-8') as f:
    text_for_post = f.read()

# *** 查找和替换 √
yseq = 0
old_text = '√'
# old_text = '~~'
new_text_begin = r'<span class="ycb-ysuper"> <span class ="ycb">V</span> <span class ="ysuper" >'
new_text_end = r'</span > </span >'
new_text = ''

while old_text in text_for_post:
    yseq += 1
    y_i = '{0:03d}'.format(yseq)  # 把format中的位置0变量，用0填充到3位数
    new_text = new_text_begin + y_i + new_text_end
    # text_for_post.replace(old_text, new_text, 1)
    text_for_post = text_for_post.replace(old_text, new_text, 1)

# *** 查找和替换图片路径
# <img src="/static/blog/ue/sub001/ch01/1.png" />
img_name_list = re.findall(r'\d+.png', text_for_post)
img_src = os.path.join("/static", "blog", file_meta["section"], file_meta["project"], file_meta["chapter"])
print("")
for img_name in img_name_list:
    old_text = f'"{img_name}"'
    new_text = f'"{img_src}/{img_name}"'
    text_for_post = text_for_post.replace(old_text, new_text, 1)

# text_for_post = re.sub(r'\d+.png', new_text, text_for_post)

# 在数据库中更新或者创建新的内容
file_meta["content"] = text_for_post
file_meta["title"] = ydoc_name

obj, created = Post.objects.update_or_create(
    title = ydoc_name,
    defaults = file_meta
    )

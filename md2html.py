import markdown2
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
from django.utils import timezone


def convert_markdown_to_html(input_file, output_file):
    with open(input_file, 'r') as file:
        markdown_text = file.read()
    html_text = markdown2.markdown(markdown_text)
    with open(output_file, 'w') as file:
        file.write(html_text)


# 设置文件属性
sections = ["django", 'animation', 'ue', 'u3d', 'tailwind']
sue_or_max=random.choice(['max','ShuYi'])
yauthor = User.objects.get(username=sue_or_max)

file_meta = {"section": "django", # ue, u3d, tailwind, python, ksp
             "project": "003",
             "chapter": "ch01",
             "title": "",
             "author": yauthor, # Foreign Key
             "updated_on": timezone.now(),  # data_time
             # "created_on": timezone.now(),
             "content": "", # text
             "level": "beginner",
             "status": 1,  # integer
             }

# 创建或者查找output_path, 用于读取和保存文件
base_dir = Path(__file__).resolve().parent #
output_path = os.path.join(base_dir, 'static', 'blog',
                           file_meta['section'], file_meta['project'],
                           file_meta["chapter"])
if not os.path.exists(output_path):
    os.makedirs(output_path)
    print(f"创建了{output_path}.")
else:
    print(f"已存在{output_path}, 无需创建.")

# *** 获得md的文件名和绝对路径
f_list = os.listdir(output_path)
md_list = []
for each_file in f_list:
    name_each_file, ext = os.path.splitext(each_file)  # name of each file
    if ext == ".md":
        md_list.append(each_file)
if len(md_list) == 0:
    print("请先创建md文件")
    exit(0)

for i in range(len(md_list)):
    print(f'{i}-{md_list[i]}')
j = int(input("请选择要处理的文件的序号: "))

ymd_path = os.path.join(output_path, md_list[i])

# *** 将md文件转化为html文件
html_output_path = os.path.join(output_path, 'output.html')
convert_markdown_to_html(ymd_path, html_output_path)

# *** 读取html 的内容
text_for_post = ''
with open(html_output_path, 'r', encoding='UTF-8') as f:
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
    text_for_post = text_for_post.replace(old_text, new_text, 1)

# *** 查找和替换图片路径
# <img src="/static/blog/ue/sub001/ch01/img_2.png" />
img_name_list = re.findall(r'img_\d+.png', text_for_post)
img_src = os.path.join("/static", "blog", file_meta["section"], file_meta["project"], file_meta["chapter"])
print("")
for img_name in img_name_list:
    old_text = f'"{img_name}"'
    new_text = f'"{img_src}/{img_name}"'
    text_for_post = text_for_post.replace(old_text, new_text, 1)

# 在数据库中更新或者创建新的内容
with open(html_output_path, 'r', encoding='UTF-8') as file:
    ytitle = file.readline().strip('# ')

file_meta["content"] = text_for_post
file_meta["title"] = ytitle

yslug = file_meta["section"] + file_meta["project"] + file_meta["chapter"]

obj, created = Post.objects.update_or_create(
    slug = yslug,
    defaults = file_meta
    )


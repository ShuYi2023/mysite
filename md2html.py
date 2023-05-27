#注意: 在vs code中运行时, 要选择 run Python file 这个选项, 而不是直接点击快捷键.

import markdown2
from pathlib import Path
import django
import os
import re
import random
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()
from django.contrib.auth.models import User
# from blog.models import Post
from article.models import ArticlePost

from django.utils import timezone


def convert_markdown_to_html(input_file, output_file):
    with open(input_file, 'r', encoding='UTF-8') as file:
        markdown_text = file.read()
    html_text = markdown2.markdown(markdown_text)  # 可以添加参数 extras=[...]
    with open(output_file, 'w', encoding='UTF-8') as file:
        file.write(html_text)

def clear_em(raw_code_block):
    new_code_block = raw_code_block
    # <p><code>(.*?)</code></p>
    for dirty_tag in [r'<em>', r'</em>', r'<p>', r'</p>', r'python']:
        new_code_block = new_code_block.replace(dirty_tag, '')
    return new_code_block



# 设置文件属性
sections = ["django", 'animation', 'ue', 'u3d', 'tailwind']
sue_or_max=random.choice(['max','ShuYi'])
yauthor = User.objects.get(username=sue_or_max)

file_meta = {"section": "django", # ue, u3d, tailwind, python, ksp
             "project": "001",
             "chapter": "ch01",
             "title": "",
             "author": yauthor, # Foreign Key
             "updated_on": timezone.now(),  # data_time
             # "created_on": timezone.now(),
             # "content": "", # text
             "body": "", # text
             "level": "beginner",
             # "status": 1,  # integer
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

ymd_path = os.path.join(output_path, md_list[j])

# *** 将md文件转化为html文件
html_output_path = os.path.join(output_path, 'output_stage1.html')
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
img_name_list1 = re.findall(r'img_\d+.png|img.png', text_for_post)  # | 符号前后不要插入空格!
img_name_list2 = re.findall(r'\d+.png', text_for_post)
img_name_list = img_name_list1 + img_name_list2
img_src = os.path.join("/static", "blog", file_meta["section"], file_meta["project"], file_meta["chapter"])
print("")
for img_name in img_name_list:
    old_text = f'"{img_name}"'
    new_text = f'"{img_src}/{img_name}"'
    text_for_post = text_for_post.replace(old_text, new_text, 1)


# *** 查找代码块
# <pre><code class="language-javascript">const variable = "Here's some JavaScript";</code></pre>
ypattern= r'```(.*?)```'
# ypattern = r'<p><code>(.*?)</code></p>'  # 找出的东西不包括<p><code>, </code></p>
code_blocks = re.findall(ypattern, text_for_post, re.DOTALL)
new_text_begin_py = r'<pre><code class="language-python">'  # python是_py, 其他代码请修改
new_text_end = r'</code></pre>'

for code_block in code_blocks:
    if 'python' in code_block:
        new_code_block = clear_em(code_block)
        new_code_block.strip()
        new_text = new_text_begin_py + new_code_block + new_text_end
        text_for_post = text_for_post.replace(code_block, new_text)
        text_for_post = text_for_post.strip()
        # text_for_post = text_for_post.replace(r'<p><code>', '')  # 要去除整个文章中的<p><code>
        # text_for_post = text_for_post.replace(r'</code></p>', '')  # 要去除整个文章中的</code></p>
        text_for_post = text_for_post.replace(r'```', '')  # 去掉三个backtip ```

    # if other language



# ***写入到本地的的 output_for_post.html
html_output_path = os.path.join(output_path, 'output_for_post.html')
with open(html_output_path, "w", encoding='UTF-8') as f:
    f.write(text_for_post)

# 获取文章的标题, 从HTML中删除标题, 删除标题的HTML tag
with open(html_output_path, 'r+', encoding='UTF-8') as f:
    lines = f.readlines()
    ytitle = lines[0].strip()
    pattern = r"<h1>|</h1>" # this matches either <p> or </p>
    replacement = ""
    result = re.sub(pattern, replacement, ytitle) # returns string without the tags
    print(result) # this prints 如何编辑能够发表在blog系统中的md文档
    f.seek(0)
    f.truncate()
    for line in lines[1:]:
        f.write(line)


# text_for_post 重新赋值
with open(html_output_path, 'r', encoding='UTF-8') as f:
    text_for_post = f.read()

# 在数据库中更新或者创建新的内容
# file_meta["content"] = text_for_post
file_meta["body"] = text_for_post
file_meta["title"] = result

yslug = file_meta["section"] + file_meta["project"] + file_meta["chapter"]

slug_exist = True  # 先假设slug存在
try:
    yfind = ArticlePost.objects.get(slug=yslug)
except:
    slug_exist = False  # 如果找不到slug, 设置slug_exist为不存在

if slug_exist:
    yinput = input("要覆盖原来的博文吗(y)?")
    if yinput.lower().strip() != 'y':
        print("你选择了不覆盖, 程序退出")
        exit(0)

obj, created = ArticlePost.objects.update_or_create(
    slug = yslug,
    defaults = file_meta
    )
print("博文更新成功!")

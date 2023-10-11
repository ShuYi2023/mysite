from pygments.formatters import HtmlFormatter
import os

# 创建manni.css, 其他式样可以参考 http://help.farbox.com/pygments.html
formatter = HtmlFormatter(style='manni')

# 指定css文件的存放路径
current_script_path = os.path.abspath(__file__)
current_script_dir = os.path.dirname(current_script_path)
css_path =  current_script_dir + r'/static/md_css/manni.css'

# print(css_path)

# 生成CSS文件, 要查看解析出来的html文件用的是.codehilite, 还是.highlight
with open(css_path, 'w') as f:
    f.write(formatter.get_style_defs('.codehilite'))

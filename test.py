import re

# Markdown text with special image syntax
html_text = """
Here is an image:

<img src="https://maxobsidian.oss-cn-shanghai.aliyuncs.com/imgs/20230925160259.png" alt="image.png|550">

And another image:
<img src="https://maxobsidian.oss-cn-shanghai.aliyuncs.com/imgs/20230925160259.png" alt="image.png|450">

Here's one more:
<img src="https://maxobsidian.oss-cn-shanghai.aliyuncs.com/imgs/20230925160259.png" alt="image.png|350">
"""

# Regular expression pattern to match the HTML image syntax
pattern = r'<img src="(.*?)" alt="(.*?)\|(\d+)">'

# Function to convert the matched pattern to a valid HTML <img> tag
def convert_image(match):
    url = match.group(1)
    alt_text = match.group(2)
    width = match.group(3)
    return f'<img src="{url}" alt="{alt_text}" width="{width}">'

# Perform batch conversion using regular expressions
new_html_text = re.sub(pattern, convert_image, html_text)

print(new_html_text)
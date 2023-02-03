def mgc_reverse(mgc):
    ylen = len(mgc)
    mgc_new = ''
    if ylen<=1:
        return mgc
    for i in range(ylen): # 0, 1
        mgc_new +=  mgc[ylen-i-1]
    return mgc_new

mgc_list = []
with open("mgci.txt", 'r', encoding='UTF-8') as f:
    mgc_text = f.read()

mgc_text.strip()
mgc_text = mgc_text.replace("，", ",")  # 中文逗号替换为英文逗号
mgc_text = mgc_text.replace("\n", "")  # 消除回车符
mgc_text = mgc_text.replace(" ", "")  # 消除空格


# 敏感词倒序
mgc_list = mgc_text.split(",")
reversed_mgc_dict = {}
for mgc in mgc_list:
    key = mgc
    value = mgc_reverse(mgc)
    reversed_mgc_dict[key] = value

# 用词典替换文中的敏感词
# 提取文章内容
with open("post.txt", 'r', encoding='UTF-8') as f:
    text_for_post = f.read()

# 把文章中的敏感词都替换掉
mgc_new=''
for mgc in mgc_list:
    if mgc in text_for_post:
        mgc_new = reversed_mgc_dict[mgc]
        text_for_post = text_for_post.replace(mgc, mgc_new)

print(text_for_post)


# 查询Model的一些操作

## 找到section字段中的所有值

```python
sections = set([obj.section for obj in MyModel.objects.all()])
print(sections)
```

* set是Python的内置函数, 用于生成一个集合(既然是集合, 内部就不会有重复的元素)

## 背诵国风·周南·关雎

---

**关关雎鸠，在河之洲。窈窕淑女，君子好逑。**

参差荇菜，左右流之。窈窕淑女，寤寐求之。背诵√

* 列表一
* 列表二
* 列表3
    * 列表3.1
    * 列表3.2
    * 列表3.3

---

* √检查python代码
```python
def article_detail(request, id):
    article = ArticlePost.objects.get(id=id)
    # 将markdown语法渲染成html样式
    article.body = markdown.markdown(article.body,
        extensions=[
        # 包含 缩写、表格等常用扩展
        'markdown.extensions.extra',
        # 语法高亮扩展
        'markdown.extensions.codehilite',
        ])
    context = { 'article': article }
    return render(request, 'article/detail.html', context)
```

## 二级标题

Ensure that you're not inadvertently introducing any invisible or special characters when creating your markdown text. Now, with this corrected markdown, the `markdown.markdown` function should properly convert your code blocks to HTML using the `pre` and `code` tags√

### 三级标题1
三级标题1的内容

### 三级标题2
标题2的内容

## 结尾
这是文章的最后部分.

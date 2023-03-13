# 查询Model的一些操作

## 找到section字段中的所有值
```python
sections = set([obj.section for obj in MyModel.objects.all()])
```
* set是Python的内置函数, 用于生成一个集合(既然是集合, 内部就不会有重复的元素)


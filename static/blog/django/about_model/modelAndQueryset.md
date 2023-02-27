# 查询Model的一些操作

## 找到section字段中的所有值
```python
sections = set([obj.section for obj in MyModel.objects.all()])
```

# 字典定义
dict1 = {"name": "liqisong", "age": 20}
dict2 = dict()

# 获取值
value1 = dict1["name"]
print(value1)
# 拿不到就返回默认值
value1 = dict1.get("name", "ii")
print(value1)
# 获取字典中所有的键，返回一个列表
value1 = list(dict1)
print(value1)
# 获取键和值
for key, value1 in dict.items(dict1):
    print(f"{key},{value1}")

# 插入值的方法
dict1["sex"] = "nam"
print(dict1)

# 删除某个元素
del dict1["name"]
print(dict1)
# 创建集合
set1 = set([1,2,3,4,5,6])
set3 = set("liqisong")
set2 = {1,1,1,1,2,3,5}
'''集合没有顺序也不能通过索引获取，而且集合不能重复'''


# print(set1)
# print(set2)
# print(set3)

# 集合操作
# 并集
set4 = set1 | set2
print(set4)
# 交集
set4 = set1 & set2
print(set4)
# 差集 前者有，后者没有的
set4 = set1 - set2
print(set4)
# 对称差集， 在前者或者后者中，但是不会同时出现的元素
set4 = set1 ^ set2
print(set4)

# 添加一项
set1.add(7)
print(set1)

# 添加多项
set1.update([7,8,9,0])
print(set1)

# 删除一项
set1.remove(7)
print(set1)


# 创建
list1 = [1,2,3,4,5]
list2 = list()

# 获取一个
list1[0]
# 修改
list1[0] = 2
# 末尾追加
list1.append("xxx")
# 对应位置插入
list1.index(2, "xxxx")
# 列表拼接
list1+list2
# 列表切片
list1[:]
list1[2:3]
list1[::2]

# 翻转列表
list1 = list1[::-1]
print(list1)
# del 可以删除列表中的单个元素，格式为：
# del listname[index]

# del 也可以删除中间一段连续的元素，格式为：
# del listname[start : end]

# Python pop() 方法用来弹出列表中指定索引处的元素，可以用变量来接，不给索引表示弹出最后一个，具体格式如下：
# listname.pop([index])

# remove:用来根据元素值来删除元素，如果列表中有多个相同值，那么只会删除第一次出现的，想要完全删除，可以多次执行
# listname.remove(value)

# clear: 用来清空列表
# listname.clear()

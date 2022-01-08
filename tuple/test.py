# 定义元祖
tuple1 = (1,2,4,"x",[1,2,3,4])
tuple2 = tuple()
tuple3 = 2,3,4,5,
'''元祖定义好以后，不能增删改，只能查，只能用'''

# 元祖连接
tuple4 = tuple1+tuple3
print(tuple4)

# 获取元祖元素
tuple4 = tuple1[1]
print(tuple4)

# 元祖切片
tuple4 = tuple1[1:2]
print(tuple4)
tuple4 = tuple1[:]
print(tuple4)
tuple4 = tuple1[::2]
print(tuple4)
# 元祖翻转
tuple4 = tuple1[::-1]
print(tuple4)


# 通过反射导包
# module = "os"
# so_module = __import__(module)
# import os
# print(os)
# print(so_module)

# eval函数处理字符串
# str1 = '''{"name": "lqs", "age": 10}'''
# dict1 = eval(str1)
# print(dict1)

# str2 = "3*4"
# rst = eval(str2)
# print(rst)

# 反射处理函数
# class Person(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#     def eat(self):
#         print(self.name)
# p = Person("lqs", 12)
# rst = getattr(p, "name")
# print(rst)
# rst2 = getattr(p, "eat")()
# rst3 = hasattr(p, "iii")
# print(rst3)
# setattr(p, "sex", 23)
# print(p.sex)
# delattr(p, "name")
# p.name



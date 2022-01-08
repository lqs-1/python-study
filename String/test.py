# str = 'liqisong'
str1 = "123"
str2 = '''hello'''
str3 = """hello world"""

num = 20

# str方式可读性更高， repr方式描述更多更详细
print(str3.__str__())
print(str3.__repr__())

print(str(num))
print(repr(num))

strrst = str3[:]
print(strrst)
strrst = str3[2::2]
print(strrst)
strrst = str3.startswith("h")
print(strrst)
strrst = str3.endswith("d")
print(strrst)

# 将字符串拆成列表
strrst = str3.split(" ")
print(strrst)

# 字符串替换
strrst = str3.replace("world", "python")
print(strrst)

# 查找某个字符、字符串第一次出现的位置
strrst = str3.index("l")
print(strrst)

# 字符串迭代， 按什么分割
strrst = str3.join("lqisong")
# lhello worldihello worldqhello worldihello worldshello worldohello worldnhello worldg
print(strrst)


# 全部大写：str.upper()
# 全部小写：str.lower()
# 大小写互换：str.swapcase()
# 首字母大写，其余小写：str.capitalize()
# 首字母大写：str.title()

# 去两边空格：str.strip()
# 去左空格：str.lstrip()
# 去右空格：str.rstrip()
# 去两边字符串：str.strip(‘d’)，相应的也有lstrip，rstrip


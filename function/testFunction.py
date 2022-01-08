

def func():
    i = 100
    j = 1000
    return i,j
i, j = func()
pp = func()[0]
print(pp)



# 如果函数的返回值不止一个，也就是说被逗号分隔，那么实际返回的就是多个，包在一个元祖里面的，需要用多个变量来接,列表的应用中也是的
try:
    pass
except Exception as e:
    raise Exception("hehe")
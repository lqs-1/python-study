def func(num):
    for i in range(10):
        yield i
# 生成器，掉yield代替return,在对象调用__next__（）之后，生成下一个，多次执行，可打印多个
# print(func(10).__next__())

# 实现一个协程
yield_list = [func(1), func(2), func(3)]
for i in range(10):
    for fun in yield_list:
        print(fun.__next__())
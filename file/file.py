if __name__ == '__main__':
    file1 = open('test')
    content = file1.readline()
    # read: 读取所有
    # readline： 每次读取一行，程序未关闭之前再次读取就是下一行
    # readlines： 一次性读出所有的行，存储在一个列表中
    # 操作文件，不指定操作动作，默认就是读
    file1.close()
    print(content)

    file2 = open('test2.txt', 'a')
    # 操作文件，r和rb是读， w和wb是写， a是追加
    # w和a的不同在于，w每次重写，a是每次追加
    print("hello", file=file2)
    # 输出重定向，可以格式化

    # 输入语句的原始写法，和接收语句的原始写法
    import sys
    sys.stdout.write("输入名字:")
    name = sys.stdin.readline()
    name = name.split(" ")
    print(name)
    for na in name:
        na = na.replace('\n','')
        print(na)
        if na == "song":
            print(111)

    # 输入和接收的简化写法
    name = input("hallo:")
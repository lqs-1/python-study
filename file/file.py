if __name__ == '__main__':
    file1 = open('test')
    content = file1.read()
    file1.close()
    file2 = open('test2.txt', 'w')
    print("hell", file=file2)

    '''
        重定向输出
    '''
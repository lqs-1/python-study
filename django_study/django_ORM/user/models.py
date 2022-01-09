from django.db import models

# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=255, verbose_name="用户名")
    password = models.CharField(max_length=255, verbose_name="密码")


    '''
    常用字段类型：
        CharField:字符串，大小255字节以内推荐
        TextField:字符串，大于255使用
        EmailField:邮箱类型，也是一个字符串，提供了校验功能
        IntegerField:整数类型
        DateField:日期类型
        TImeField：时间类型
        DateTimeField：日期时间类型
        FIleField:字符串，用于存放文件保存路径的
        ImageField：字符串，用于存放图片保存路劲的
        
    常用的字段属性：
        db_index:索引
        unique:无重复
        default：默认值
        auto_now_add:创建时间
        auto_now:更新时间
    '''

    class Meta:
        db_table = "user"
        verbose_name = "用户"
        verbose_name_plural = verbose_name

        '''说明是一个抽象模型类,别的函数中可以继承'''
        # abstract = True

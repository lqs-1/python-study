from django.db import models

# Create your models here.

class User(models.Model):
    '''
    verbose_name: 单数别名
    verbose_name_plural: 复数别名
    '''
    username = models.CharField(max_length=255, verbose_name="姓名")
    password = models.CharField(max_length=255, verbose_name="密码")

    def __str__(self):
        return self.username

    class Mete:
        '''定义表模型属性'''
        pass



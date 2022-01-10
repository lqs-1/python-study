from django.db import models


class Book(models.Model):
    title = models.CharField(max_length=20, verbose_name='图书名称')
    desc = models.TextField(verbose_name='图书描述')
    publishdate = models.DateField(verbose_name="出版日期")
    publishing = models.ForeignKey(to="Publishing", on_delete=models.CASCADE, verbose_name='出版商')
    author = models.ManyToManyField(to='AuthorInfo', verbose_name='作者')

    class Meta:
        db_table = 'Book'
        verbose_name = '图书信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title + '相关信息'


class Publishing(models.Model):
    name = models.CharField(max_length=20, verbose_name='出版社名称')
    address = models.CharField(max_length=20, verbose_name='出版社地址')

    class Meta:
        db_table = 'Publishing'
        verbose_name = '出版社信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '出版社:' + self.name


class AuthorInfo(models.Model):
    name = models.CharField(max_length=10, verbose_name='姓名')
    email = models.EmailField(verbose_name='邮箱')
    birthday = models.DateField(verbose_name='出生日期')
    header = models.ImageField(upload_to='header', verbose_name='作者头像')

    class Meta:
        db_table = 'Author'
        verbose_name = '作者基本信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '作者:' + self.name




class Author(models.Model):
    pass
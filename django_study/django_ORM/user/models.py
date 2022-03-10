from django.db import models
from django.shortcuts import reverse


class Role(models.Model):
    role_name = models.CharField(max_length=255, verbose_name="身份")

    def __str__(self):
        return self.role_name

    class Meta:
        db_table = 'role'

    # def get_abs


class User(models.Model):
    username = models.CharField(max_length=255, verbose_name="用户名")
    password = models.CharField(max_length=255, verbose_name="密码")
    role = models.ForeignKey(to="Role", default=1,on_delete=models.CASCADE)
    del_mark = models.BooleanField(default=False)

    def __str__(self):
        return self.username

    # 如果模型中的某个字段需要建立url链接，来修改删除等，并且这个字段值唯一，
    # 例如： 在修改某个商品的信息的时候，超链接的地方就会需要一个商品id，如果我们直接用id的话就不是太理想
    # 可以通过get_absolute_url方法来解析出每个商品修改时候的链接，直接拿到前端页面就能进行填充，而不是在业务处理的时候拼接
    # 这种方式需要一个要参数的url映射：  path('index/<int:num>/', index, name='index'), 这种的， 一定要有参数，不然没意义

    # 使用的时候： 先把符合条件的数据查出来，然后传到前端，前端用填充占位符调用里面的方法get_absolute_url, 说白了就是完成了一个url地址拼接的工作
    def get_absolute_url(self):
        # self.pk 等同于 主键
        return reverse("user:index", kwargs={'num': self.pk})



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
        
    操作：
        删除：
            User.objects.get(id=20).delete() : 删除一条
            User.objects.filter(role_id=20).delete() ：删除多条
        更新：
            User.objects.filter(role_id=2).update(username="lixiaodong") : 修改多条
            修改一条
            user = User.objects.get(id=28)
            user.username = "lishangshu"
            user.save()
        插入：
            User.objects.create(xx=xx, xx=xx....)
            如果是外键表，那么在添加的时候，外键字段就是一个表的对象
            
        查询：
            普通查询：
                User.objects.get(id=xx) : 查询单条数据
                User.objects.filter(username="liqosng") : 查询多条数据
                User.objects.exclude(id=xx) : 反向查询，不满足条件的
                
                get():返回满足条件的一条记录
                all():返回所有记录，查询集
                filter():返回满足条件的所有记录，查询集
                exclude():返回不满足条件的所有记录，查询集
                order_by(‘属性名1’,’属性名2'……):升序
                order_by(‘-属性名1’,’-属性名2'……):降序，order_by()是将查出来的数据进行排序，
                    如：BookInfo.objects.all().order_by('id','-btitle')
                    
                说明一下:exclude,filter,get三个都时带条件的--->模型名.objects.查询方式(属性名__条件名=值)
                条件名:
                    exact:判等 ，可以不用直接用 =
                    contains:模糊查询，包含
                    endswith\startswith:模糊查询，结尾\开头
                    isnull:空查询,布尔值, User.objects.filter(xx__isnull=True[False])
                    in:属性名__in = 列表或者元组,列出来的, User.objects.filter(xx__in=[1,2,3])
                    range:不列出来，表示范围，between .. and .., User.objects.filter(xx__range=[1,65])
                    gt,lt,gte,lte:大于，小于，大于等于，小于等于
                    day/month/year:使用方法:日期查询
                    
                    values()：显示哪些字段， 返回一个字典
                    values_list() ： 显示哪些字段， 返回一个元祖
                    
                    
                Q对象:用于查询时候的多个条件的  ’与或非‘  表示
                from django.db.models import Q
                例子:
                    BookInfo.object.filter(Q(id = 2) & ~Q(btitle = 'hello'))   与
                    BookInfo.object.filter(Q(id = 2) | Q(btitle = 'hello'))   或
                    BookInfo.object.filter(~Q(id = 2))                        非
                    
                F对象:条件中用于属性比较,还可以进行算数运算
                from django.db.models import F
                例子:
                    BookInfo.objects.filter(id__gt = F('bid'))
                    BookInfo.objects.filter(id__gt = F('bid')*3)
                
               
          
            聚合函数:sum,count,avg,max,min,在django中通过aggregate来使用
            from django.db.models import Sum,Count,Avg,Max,Min
            例子:
                BookInfo.objects.all().aggregate(Count('id')) : 返回值是字典
                BookInfo.objects.all().aggregate(Sum('bread') : 总和
                
        分组：
            values('is_active')：根据什么分组
            annotate(total=Count('id'))：对什么进行聚合
            例子：
                User.objects.all().values("role").annotate(total_mun=Count("id")).all()
                
                
        关联查询：
            一对多：外键定义在多表中，反向查询就是一表查多表
            
            普通方式：
                先查一个表再查另一个表
                多查一：
                    user = User.objects.get(id=28)
                    user.role_id[.role_name]
                一查多：
                    role = Role.objects.get(id=1)
                    如果外键字段没有定义反向调用related_name，那么就使用  模型类名小写_set.all(), 和下面的方式二选一
                    user_list = role.user_set.all()
                    如果外键字段定义了反向调用related_name，那么就使用  related_name的值.all()
                    user_list = role.user_relation.all()
                    
            模型类方式(还可以夸表查询)：
                一查多：
                    User.objects.filter(role_id=1)
                多查一:
                    如果没定义related_name,那么就只能用 模型类小写__属性=xxx
                    Role.objects.filter(user__username='lishangshu', id=2)
                    如果定义了related_name,那么就只能用 related_name的值__属性=xxx
                    Role.objects.filter(user_relation__username='lishangshu', id=2)
                
                        
        
            
    '''

    class Meta:
        db_table = "user"
        verbose_name = "用户"
        verbose_name_plural = verbose_name
        '''说明是一个抽象模型类,别的函数中可以继承'''
        # abstract = True




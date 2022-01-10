from django.shortcuts import render, reverse, redirect, HttpResponse
from django.http.response import JsonResponse
from .models import User, Role


# 三个基于类的通用视图
from django.views.generic import TemplateView, ListView

# 展示一般数据使用
class My_TemplateView(TemplateView):
    # 设置模板
    template_name = 'register.html'
    # 重写父类方法
    def get_context_data(self, **kwargs):
        # 模板变量必须有父类先生成， 生成之后，自己添加，否则错误
        context = super(My_TemplateView, self).get_context_data()
        # 添加模板变量
        context['username'] = 'liqisong'
        # 返回数据
        return context


# 多用于获取数据库中的记录
class My_ListView(ListView):
    # 设置模板
    template_name = 'register.html'
    # 定义模板变量名称
    context_object_name = 'usernames'
    # 设置数据模型, 这种方式是获取全部
    # model = User
    # 重写get_queryset方法，就可以根据条件查询出对应的数据, 返回值就是模板变量
    def get_queryset(self):
        user_list = User.objects.filter(role__id=1)
        return user_list
    # 如果还需要添加模板变量， 那么就重写父类的get_context_data方法
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(My_ListView, self).get_context_data()
        context['roles'] = Role.objects.all()
        return context



import logging
logger = logging.getLogger('lqs')
# 事务模块
from django.db import transaction


# 局部添加事务
# @transaction.atomic
# 局部关闭事务
# @transaction.non_atomic_requests
def index(request, num):

    if request.method == 'GET':

        '''
        cookie和session:
        '''
        request.COOKIES.get('xxx')  # 获取cookie
        HttpResponse.set_cookie(key='xx', value='xx', max_age='xx')  # 设置cookie
        HttpResponse.delete_cookie(key='xx')  # 删除cookie

        request.session.get('xx')  # 获取session
        request.session.setdefault('xx', 'xx')  # 设置session，存在则不设置
        request.session['xx'] = 'xx'  # 设置session
        del request.session['xx']  # 删除session



        return render(request, 'register.html')
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")

        # 定义事务
        # sid = transaction.savepoint()
        try:
            # User.objects.create(username=username, password=password)

            # with transaction.atomic():
            user = User.objects.get(id=2)
            name = user.role.role_name
                # i = 1/0
            # 提交事务
            # transaction.savepoint_commit(sid)
        except Exception as e:
            logger.error(e)
            # 回滚事务
            # transaction.savepoint_rollback(sid)
            return render(request, 'register.html')

        # 重定向到的时候， 如果是外网url那么就重定向过去，如果是本网络，就写相对路径/开头 ，或者用冒号反向解析， 如果url需要传递参数， 那么就依次写到后面， 还可以以和reverse一起使用
        # reverse只能冒号反向解析，不能使外网字符串， 而redirect两者都可以， reverse还可以用在模型层， 动态的为某些对象产生url
        # return redirect(reverse("user:index"))
        # return redirect("https://www.baidu.com")
        # return redirect("user:index", num=1232, string='lll')

        # render转发数据，渲染模板
        # render(request=request, template_name="register.html", context={})

        # 完整的HttpResponse写法
        return HttpResponse(content=name, content_type='text/html', status=200, reason='HTTP/1.1 200', charset='utf-8')


def test(request):
    user = User.objects.filter(role__id=2)
    for us in user:
        print(us.get_absolute_url())
    return redirect("/user/index/222")

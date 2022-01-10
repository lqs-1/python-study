from django.urls import path, re_path
from .views import index, test, My_TemplateView, My_ListView

app_name = "user"
urlpatterns = [
    # 地址中带有参数的时候，可以使用正则俩接，更好的兼容restful风格，这是第一种方式，接收被命名的正则参数， 视图函数的参数中必须有一个变量并且同名
    # re_path(r'index/(?P<num>\d{1})', index, name='index'),
    # 这是第二种方式，接收没有被命名的正则参数， 视图函数的参数中必须有但名字随意
    # re_path(r'index/(\d{1})', index, name='index')
    # 这是第三种 系统内置的  <类型: 名字>, 视图函数中的参数和这里保持一致, 只有在path中使用
    # path('index/<int:num>/<str:string>', index, name='index')

    path('index/<int:num>/', index, name='index'),
    path('test/', test, name='test'),

    # 基于类的所有视图， 都不能和url配置进行关联， 只能使用as_view()方法将类转换成函数才能使用
    path('templateView', My_TemplateView.as_view(), name='templateView'),
    path('listView', My_ListView.as_view(), name='listView')

    # path('index/', index, name='index')

]
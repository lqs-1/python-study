
'''自定义前端模板模板变量过滤器'''

# 导入模块
from django import template
# 取出注册库，固定写法
register = template.Library()
# 注册这个自定义的过滤器名字为lqs
@register.filter(name='gegege')
# value表示模板变量的值， args表示要设置的参数值
def test(value, args):
    if value == 'liqisong':
        return args
    else:
        return value


# 自定义前端模板变量过滤器，必须定义在应用文件夹下，目录名字必须是templatetags
# 基本自定义写法就上上面那样
# 过滤器使用： {{模板变量|过滤器名字:过滤器参数}}
# 自定义的过滤器，要想使用，必须在前端页面中{%load 定义过滤器的文件%}





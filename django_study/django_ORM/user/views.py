from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import User
# 事务模块
from django.db import transaction

# Create your views here.

# 局部添加事务
# @transaction.atomic
# 局部关闭事务
# @transaction.non_atomic_requests
def index(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")

        # 定义事务
        # sid = transaction.savepoint()
        try:
            with transaction.atomic():
                user = User.objects.create(username=username, password=password)
                i = 1/0
            # 提交事务
            # transaction.savepoint_commit(sid)
        except Exception as e:
            # 回滚事务
            # transaction.savepoint_rollback(sid)
            return render(request, 'register.html')
        return HttpResponse("ok")

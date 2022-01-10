from django.shortcuts import render, reverse, redirect
from django.shortcuts import HttpResponse
from .models import User, Role
import logging
logger = logging.getLogger('lqs')
# 事务模块
from django.db import transaction

# Create your views here.

# 局部添加事务
# @transaction.atomic
# 局部关闭事务
# @transaction.non_atomic_requests
def index(request):
    if request.method == 'GET':
        logger.warning("你好")
        logger.error("你好")
        logger.info("你好")
        logger.debug("你好")
        logger.critical("你好")
        return render(request, 'register.html')
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")

        # 定义事务
        # sid = transaction.savepoint()
        try:
            # User.objects.create(username=username, password=password)
            user = User.objects.get(id=2)
            name = user.role_id.role_name

                # i = 1/0
            # 提交事务
            # transaction.savepoint_commit(sid)
        except Exception as e:
            # 回滚事务
            # transaction.savepoint_rollback(sid)
            return render(request, 'register.html')
        return HttpResponse(name)

from django.urls import re_path
from .views import index
app_name = 'user'
urlpatterns = [
    # 配置应用的路由
    re_path(r"index/", index, name="index")
]
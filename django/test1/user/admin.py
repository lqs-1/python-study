from django.contrib import admin
from .models import User
# Register your models here.

# 自定义后台显示样式
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "password")

# 注册表
admin.site.register(User, UserAdmin)

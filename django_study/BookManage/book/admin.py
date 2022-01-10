from django.contrib import admin

from .models import AuthorInfo, Book, Publishing

# Register your models here.

# 后台页面功能完善
class BookAdmin(admin.ModelAdmin):
    # 将出版日期作为导航查询字段
    date_hierarchy = 'publishdate'
    # 设置字段没有数据时候的默认显示， 只是显示， 不会更改数据库中的数据
    empty_value_display = '--无数据--'
    # 设置author字段的选择方式为水平选择
    filter_horizontal = ('author',)


    # 设置过滤导航字段
    list_filter = ('title', 'publishing', 'author',)
    # 设置查询的字段
    search_fields = ('title', 'publishing__name', 'authorinfo__name',)
    # 列表显示字段
    list_display = ('title', 'publishing', 'publishdate',)
    # 显示查询到的记录数
    show_full_result_count = True
    # 设置每页显示6条记录
    list_per_page = 6
admin.site.register(Book, BookAdmin)
admin.site.register(AuthorInfo)
admin.site.register(Publishing)

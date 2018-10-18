from django.contrib import admin

# Register your models here.
from xauth.models import SystemMenu, SystemHistory, GroupSystemMenu


class SystemMenuAdmin(admin.ModelAdmin):
    list_display = ('name', 'action', 'activate', 'order', 'style', 'parent')
    list_filter = ['name', 'action', 'activate', 'order', 'style', 'parent']
    search_fields = ['name', 'action', 'activate', 'order', 'style', 'parent']


class SystemHistoryAdmin(admin.ModelAdmin):
    list_display = ('class_name', 'user', 'operator_time', 'content', 'ip')
    list_filter = ['class_name', 'user', 'operator_time', 'content', 'ip']
    search_fields = ['class_name', 'user', 'operator_time', 'content', 'ip']


class GroupSystemMenuAdmin(admin.ModelAdmin):
    list_display = ('group', 'menu', 'activate')
    list_filter = ['group', 'menu', 'activate']
    search_fields = ['group', 'menu', 'activate']


admin.site.register(SystemMenu, SystemMenuAdmin)
admin.site.register(SystemHistory, SystemHistoryAdmin)
admin.site.register(GroupSystemMenu, GroupSystemMenuAdmin)
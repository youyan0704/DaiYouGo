from django.contrib.auth.models import User, Group
from django.db import models

# Create your models here.
from django.utils import timezone


# 系统菜单
class SystemMenu(models.Model):
    # 菜单名
    name = models.CharField(max_length=64)
    # 菜单对应的方法,父菜单可以为空
    action = models.CharField(max_length=64, blank=True, help_text='父菜单可以为空')
    # 是否激活
    activate = models.BooleanField(default=False)
    # 排序
    order = models.IntegerField()
    # 菜单样式,子菜单没有图标
    style_choices = (
        ('home', 'icon-home'),
        ('basket', 'icon-basket'),
        ('rocket', 'icon-rocket'),
        ('rocket', 'icon-diamond'),
        ('rocket', 'icon-puzzle'),
        ('paper-plane', 'icon-paper-plane'),
        ('settings', 'icon-settings'),
        ('briefcase', 'icon-briefcase'),
        ('wallet', 'icon-wallet'),
        ('bar-chart', 'icon-bar-chart'),
        ('docs', 'icon-docs'),
        ('present', 'icon-present'),
        ('folder', 'icon-folder'),
        ('user', 'icon-user'),
        ('pointer', 'icon-pointer')
    )
    style = models.CharField(max_length=255, choices=style_choices, blank=True, help_text='子菜单没有图标')
    # 父菜单
    parent = models.ForeignKey('self', blank=True, null=True, related_name='parentMenu', on_delete=models.CASCADE)

    class Meta:
        db_table = 'xauth_system_menu'
        ordering = ['parent_id', 'order']

    def __str__(self):
        return self.name


# 组别跟菜单
class GroupSystemMenu(models.Model):
    # 组别
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    # 菜单
    menu = models.ForeignKey(SystemMenu, on_delete=models.CASCADE)
    # 激活
    activate = models.BooleanField(default=False)

    class Meta:
        db_table = 'xauth_group_system_menu'
        ordering = ['group_id', 'menu_id']


# 系统修改历史记录
class SystemHistory(models.Model):
    # 操作对象
    class_name = models.CharField(max_length=255)
    # 操作人
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # 操作时间
    operator_time = models.DateTimeField(default=timezone.now())
    # 操作内容
    content = models.TextField()
    # 操作IP
    ip = models.CharField(max_length=128)

    class Meta:
        db_table = 'xauth_system_history'

    def __str__(self):
        return '<SystemHistory %s>' % self.user.username

# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# 订单
class Order(models.Model):
    # 订单编号
    no = models.IntegerField(unique=True)
    # 订单名称
    name = models.CharField(max_length=255)
    # 订单描述
    description = models.TextField()
    # 下单时间
    order_datetime = models.DateTimeField(default=timezone.now())
    # 订单状态（接单中， 采购中，已完成等）
    order_status = models.IntegerField(default=1)
    # 已删除标记
    is_deleted = models.BooleanField(default=False)


# 订单跟用户对应关系
class OrderUserRelation(models.Model):
    # 订单
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    # 对应的用户
    userId = models.ForeignKey(User, on_delete=models.CASCADE)
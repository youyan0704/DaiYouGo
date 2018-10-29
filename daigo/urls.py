# -*- coding: utf-8 -*-
# @Time    : 18-10-15 上午10:37
# @Author  : allen.you

from django.contrib import admin
from django.urls import path, include

from daigo.views import *

urlpatterns = [
    path('orders/', orders, name='orders'),
    path('orders/<int:id>', order, name='order')
]

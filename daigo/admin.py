# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.

from daigo.models import Order, OrderUserRelation


class OrderUserRelationInLine(admin.TabularInline):
    model = OrderUserRelation
    extra = 2


class OrderAdmin(admin.ModelAdmin):
    list_display = ('no', 'name', 'description', 'order_datetime', 'order_status')
    list_filter = ['no', 'name', 'description', 'order_datetime', 'order_status']
    search_fields = ['no', 'name', 'description', 'order_datetime', 'order_status']
    inlines = [OrderUserRelationInLine]


admin.site.register(Order, OrderAdmin)

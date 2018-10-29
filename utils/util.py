# -*- coding: utf-8 -*-
# @Time    : 18-10-26 下午1:58
# @Author  : allen.you
from xauth.models import SystemMenu


def get_breadcrumb(action='/'):
    breadcrumbs = {}
    current_menu = SystemMenu.objects.get(action=action)
    if current_menu.parent:
        breadcrumbs['parent'] = current_menu.parent.name

    breadcrumbs['current_menu'] = current_menu.name

    return breadcrumbs

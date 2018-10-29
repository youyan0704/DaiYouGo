# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render


# Create your views here.
from utils.util import get_breadcrumb


def orders(request):

    # request.sessin['breadcrumb'] =

    request.session['breadcrumb'] = get_breadcrumb('/daigo/orders')

    return render(request, 'orders/orders.html')


def order(request, id):
    request.session['breadcrumb'] = get_breadcrumb('/daigo/orders/1')
    return render(request, 'orders/orders.html')
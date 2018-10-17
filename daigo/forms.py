# -*- coding: utf-8 -*-
# @Time    : 18-10-17 下午2:34
# @Author  : allen.you
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=50)
    password = forms.CharField(label='密码')

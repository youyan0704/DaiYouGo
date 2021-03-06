from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User, Group
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views import View

from daigo.forms import LoginForm
from xauth.models import SystemMenu, GroupSystemMenu


class LoginPage(View):
    form_class = LoginForm
    template_name = "xauth/login_origin.html"

    def get(self, request):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                request.session['menu'] = get_user_menu(user)
                return HttpResponseRedirect('/index')
            else:
                user = User.objects.filter(username=username)
                if user:
                    messages.error(request, "密码不匹配")
                else:
                    messages.error(request, "用户不存在")
        return render(request, self.template_name, {'form': form})


def get_user_menu(user):
    user_menus = []
    group_menus = GroupSystemMenu.objects.filter(activate=1,
                                                 group=Group.objects.get(
                                                     user=user)).all()
    for group_menu in group_menus:
        menu = group_menu.menu
        user_menus.append({'id': menu.id,
                           'action': menu.action,
                           'name': menu.name,
                           'style': menu.get_style_display(),
                           'parent': menu.parent_id})
    return user_menus


def logout_view(request):
    logout(request)
    messages.info(request, "已注销")
    return HttpResponseRedirect("/login")


class ExtraLockView(View):
    template_name = "xauth/extra_lock.html"

    def get(self, request):
        # logout(request)
        return render(request, self.template_name)

    def post(self, request):
        pass


class HomePageView(LoginRequiredMixin, View):
    """主页面"""

    template_name = "index_base.html"

    def get(self, request):
        request.session['menu'] = get_user_menu(request.user)
        return render(request, self.template_name)

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
                request.session['menu'] = self.get_user_menu(user)
                return HttpResponseRedirect('/index')
            else:
                user = User.objects.filter(username=username)
                if user:
                    messages.error(request, "密码不匹配")
                else:
                    messages.error(request, "用户不存在")
        return render(request, self.template_name, {'form': form})

    def get_user_menu(self, user):
        user_menus = []
        menus = SystemMenu.objects.filter(activate=1,
                                          id=GroupSystemMenu.objects.get(
                                              group=Group.objects.get(user=user)).group.id).all()
        for menu in menus:
            user_menus.append({'action': menu.action, 'name': menu.name, 'style': menu.style})
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

    template_name = "xauth/index.html"

    def get(self, request):
        return render(request, self.template_name)

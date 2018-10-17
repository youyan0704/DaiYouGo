from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.views import View

from daigo.forms import LoginForm


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
                # user_menu = get_menu(user)
                # request.session['user_menu'] = user_menu
                return HttpResponseRedirect('/index')
            else:
                user = User.objects.filter(username=username)
                if user:
                    messages.error(request, "密码不匹配")
                else:
                    messages.error(request, "用户不存在")
        return render(request, self.template_name, {'form': form})


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

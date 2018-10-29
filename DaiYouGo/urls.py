"""DaiYouGo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from xauth.views import LoginPage, HomePageView, logout_view, ExtraLockView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', LoginPage.as_view(), name='login'),
    path('login/', LoginPage.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('extra_lock/', ExtraLockView.as_view(), name='extra_lock'),
    path('index/', HomePageView.as_view(), name='homePage'),
    # daigo app
    path('daigo/', include('daigo.urls'))
]

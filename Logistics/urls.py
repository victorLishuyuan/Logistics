"""Logistics URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path,include
from django.conf.urls import  url
from sm import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('rm/', include('rm.urls',namespace='rm')),
    path('fm/', include('fm.urls', namespace='fm')),
    path('om/', include('om.urls', namespace='om')),
    path('sm/', include('sm.urls', namespace='sm')),
    url('^$',views.login,name='login') # 默认路由,程序运行的默认页面
]




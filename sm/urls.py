from django.urls import path, re_path

from . import views

from django.conf.urls import url

# 定义一个命名空间，与容器中的urls中的命名空间一致

app_name = 'sm'

urlpatterns = [


    url(r'^errorPage$', views.errorPage, name='errorPage'),

    url(r'^index$', views.index, name='index'),

    # 注册登录

    url(r'^user_exists/$', views.user_exists, name='user_exists'),

    url(r'^login/', views.login, name='login'),

    url(r'^registe$', views.registe, name='registe'),

    url(r'^logout$', views.logout, name='logout'),

    # 用户管理

    url(r'^userManage$', views.userManage, name='userManage'),

    url(r'^getUserInfo/$', views.getUserInfo, name='getUserInfo'),

    url(r'^userEdit$', views.userEdit, name='userEdit'),

    url(r'^userAdd', views.userAdd, name='userAdd'),

    url(r'^userDelById$', views.userDelById, name='userDelById'),

    url(r'^userInfo$', views.userInfo, name='userInfo'),

    url(r'^userPwdUpdate$', views.userPwdUpdate, name='userPwdUpdate'),

    url(r'^userInfoExport$', views.userInfoExport, name='userInfoExport'),

    # 角色管理

    url(r'^roleManage', views.roleManage, name='roleManage'),

    url(r'^roleAdd', views.roleAdd, name='roleAdd'),

    url(r'^roleEdit/(\d+)$', views.roleEdit, name='roleEdit'),

    url(r'^roleDelById/$', views.roleDelById, name='roleDelById'),

    url(r'^getMenu$', views.getMenu),

    # 权限菜单管理

    url(r'^menuManage', views.menuManage, name='menuManage'),

    url(r'^menuAdd/(\S+)$', views.menuAdd, name='menuAdd'),

    url(r'^menuEdit/(\S+)$', views.menuEdit, name='menuEdit'),

    url(r'^menuDelByCode/$', views.menuDelByCode, name='menuDelByCode'),

]

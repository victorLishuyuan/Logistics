from django.db import models

from django.contrib.auth.models import AbstractUser,User

from django.db.models.signals import post_save

from django.dispatch import receiver

# Create your models here.

# system_user（用户信息表）

# 登录用户信息表（注：该表实际上作为django自带的auth.user表的关联信息表）

class user_profile(models.Model):

    # 增加一对一的用户模型，

    user = models.OneToOneField(User,on_delete=models.CASCADE,verbose_name='认证用户') # 用户名为外键，参找表auth.user表

    # 剩下的为自己所定义的数据信息

    u_name = models.CharField(max_length=30,verbose_name='用户名',default='')

    u_pwd  = models.CharField(max_length=30,verbose_name='密码')

    u_status_tsc = models.IntegerField(verbose_name='账号状态')

    apply_date = models.DateTimeField(verbose_name='申请日期',blank=True,null=True)

    approvel_date = models.DateTimeField(verbose_name='审批日期',blank=True,null=True)

    chinese_name = models.CharField(max_length=30,verbose_name='中文名称',null=True,blank=True)

    identity_card = models.CharField(max_length=20,verbose_name="身份证号",null=True,blank=True)

    telephone_number = models.CharField(max_length=11,verbose_name='手机号',null=True)

    landline =models.CharField(max_length=15,verbose_name="固定电话",null=True)

    wechanumber = models.CharField(max_length=30,verbose_name='微信号',null=True,blank=True)

    email = models.CharField(max_length=30,verbose_name='邮箱',default='123456789',null=True)

    appid = models.CharField(max_length=30,verbose_name='微信验证应用标识',null=True,blank=True)

    lastlogin_date = models.DateTimeField(verbose_name='最后登录时间',null=True,blank=True)

    system_role = models.ForeignKey( 'role',to_field='id',on_delete=models.SET_NULL,null=True,verbose_name='角色')

    # system_role_id = models.IntegerField(verbose_name='角色信息',blank=True,null=True)

    class Meta:

        db_table = 't_sys_user'



# system_role（角色信息表）

class role(models.Model):

    name = models.CharField(max_length=30,verbose_name='角色名')

    note = models.CharField(max_length=100,verbose_name='备注',null='true',blank='true')

    menu_info = models.ManyToManyField('menu', through='role_menu',through_fields=('system_role','system_menu'),verbose_name='菜单信息') # 多对多的关系,定义一个

    # 在进行外键查询时候，在前端显示该模型的名字

    def __str__(self):

        return self.name
    class Meta:

        db_table = 't_sys_role'



# system_menu（菜单信息）

class menu(models.Model):

    name = models.CharField(max_length=30, verbose_name='菜单名称')

    code = models.CharField(max_length=30,verbose_name='菜单编号',unique=True,default='1')

    parent_code = models.CharField(max_length=30,verbose_name='父级菜单',blank=True,null=True)

    # parent = models.ForeignKey('self',to_field='code', verbose_name='父级菜单',on_delete=models.CASCADE,null=True)

    url =  models.CharField(max_length=30,verbose_name='URL',blank=True,null=True)

    icon = models.CharField(max_length=100,verbose_name='图标',blank=True,null=True)

    level = models.IntegerField(verbose_name='菜单级别',blank=True,null=True)

    is_Enabled_tsc = models.IntegerField(verbose_name='是否启用')

    def __str__(self):
        return self.name
    class Meta:

        db_table = 't_sys_menu'


# system_code（代码表）

class code(models.Model):

    type = models.CharField(max_length=30,verbose_name='分类')

    code = models.IntegerField(verbose_name='编码')

    value = models.CharField(max_length=30,verbose_name='编码值')

    order_number = models.IntegerField(verbose_name='顺序号，代表显示优先级')

    comment = models.CharField(max_length=30,verbose_name='备注')
    class Meta:

        db_table = 't_sys_code'


# system_role_menu（角色-菜单表）

class role_menu(models.Model):

    system_role= models.ForeignKey('role',to_field='id',on_delete=models.CASCADE,verbose_name='角色id')

    system_menu = models.ForeignKey('menu',to_field='id',on_delete=models.CASCADE,verbose_name='菜单id')
    class Meta:
        db_table = 't_sys_role_menu'



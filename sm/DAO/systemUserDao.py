from sm import models
from django.contrib.auth.models import User
from django.db.models import Q
# 插入用户

def create(user_info):
    try:
        u_name = user_info['u_name']
        email = user_info['email']
        u_pwd = user_info['u_pwd']
        # 在django表中新建立一个用户 作为登录用
        user = User.objects.create_user(u_name, email, u_pwd, )  # 创建用户必须有用户名，邮箱，密码，
        # 在 user_profile表中创建一个用户
        new_user = models.user_profile.objects.create(user=user, **user_info)
    except Exception as e:
        print(e)
        return False

    return True

# 更新菜单

def update(menu_info):

    code = menu_info['code']

    if models.menu.objects.filter(code=code).update(**menu_info):

        return True

    return False



# 根据角色类型 查询所有的用户信息
def queryAllUser():
    all_user = models.user_profile.objects.all().order_by('system_role_id')
    return all_user

# 根据用户 id 冻结账号
def deleteById(id):
    try:
        user_info = models.user_profile.objects.get(id=id)
        if user_info.u_status_tsc == 0:
            return False
        user_info.u_status_tsc = 0
        user_info.save()
    except Exception as e:
        print(e)
        return False
    return True

# 根据 待查询角色id，用户名，中文名 联合查询登录用户信息
def queryUserByRoleIdAndUnameAndCname(role_id,u_name,chinese_name):

    if role_id == '0':
        user_info = models.user_profile.objects.filter(Q(u_name__startswith=u_name)&Q(chinese_name__startswith=chinese_name)).all()
    else:
        user_info = models.user_profile.objects.filter(Q(system_role_id=role_id)&Q(u_name__startswith=u_name) & Q(chinese_name__startswith=chinese_name)).all()
    return user_info

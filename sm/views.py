from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
from sm.models import *
from django.forms.models import model_to_dict
from django.forms import modelformset_factory
import json
from django.contrib.auth.models import User
import datetime
import random
import time
from django.contrib.auth import authenticate, login as dlogin
from django.http import JsonResponse
from sm import common
from sm.DAO import systemMenuDao, systemUserDao, systemRoleDao
import io
from django.views.decorators.clickjacking import xframe_options_exempt
@login_required
def errorPage(request):
    return render(request, 'error.html')
# 验证用户名是否存在
def user_exists(request):
    u_name = request.GET.get('u_name')
    u_name_exist = user_profile.objects.filter(u_name=u_name)  # 查询数据库中是否存在该用户
    if u_name_exist:
        return HttpResponse(json.dumps({'valid': 'false'}))
    return HttpResponse(json.dumps({'valid': 'true'}))


# 用户注册
def registe(request):
    return render(request, 'registe.html')


# 登录验证
def login(request):
    u_name = request.COOKIES.get('u_name')

    ret_code = 0  # 定义状态
    # if u_name:
    #     print('缓存登录。。。。。。。。。。。。。。。')
    #     return redirect('sys:index')
    # 从自定义数据库user中获取登录用户‘用户状态’，‘角色信息’
    if request.method == 'POST':
        ret_code = 0  # 返回状态
        # 从页面输入的值
        login_u_name = request.POST.get('username')
        login_u_pwd = request.POST.get('password')
        # 按照用户名、密码从Django自带的数据库auth_user数据库获取用户信息
        django_user = authenticate(username=login_u_name, password=login_u_pwd)  # 获取django提供的user表信息
        if django_user is not None:
            if django_user.is_active:  # 存在该用户，并且用户名和密码正确，则进行其他信息校验
                # 从自定义数据库user中获取登录用户‘用户状态’，‘角色信息’
                db_user = user_profile.objects.filter(u_name=login_u_name).only('u_status_tsc', 'system_role').first()
                u_status = db_user.u_status_tsc  # 用户状态{1:'在用',2:'冻结',3,'注销'}
                u_name = db_user.u_name
                if u_status == 0:
                    ret_info = '账号已冻结，请联系管理员或者上级部门'
                else:
                    # 用户登录成功，添加最后登录时间并写入数据库、获取用户的角色、根据角色获取用户的菜单权限信息
                    now_time = datetime.datetime.now()
                    u_id = db_user.id
                    u_role_id = db_user.system_role_id
                    u_role = db_user.system_role  # 获取用户角色
                    user_profile.objects.filter(u_name=login_u_name).update(lastlogin_date=now_time,
                                                                            u_status_tsc=1)  # 更待用户登录状态为在线

                    # 将用户名、角色名信息存储到seesion中
                    request.session['u_id'] = str(u_id)  # 将用户的id存储到session中
                    request.session['u_name'] = str(u_name)  # 将用户名存储到session中
                    request.session['u_role'] = str(u_role)  # 将角色名存储到session中
                    request.session['u_role_id'] = str(u_role_id)  # 将角色id存储到session中
                    # 从数据库中按照 角色名、菜单等级查询条件，并且按照菜单编号、父亲菜单编号排序， 查询 ‘菜单编号’，‘父亲菜单编号’，‘菜单名称’，‘是否启用’，‘url’，转换成列表，存到session中
                    menu_level1 = menu.objects.filter(role__name=u_role, level=1).order_by('code',
                                                                                           'parent_code').values_list(
                        'code', 'parent_code', 'name', 'is_Enabled_tsc', 'url')  # 根据角色名查询一级菜单信息

                    menu_level2 = menu.objects.filter(role__name=u_role, level=2).order_by('code',
                                                                                           'parent_code').values_list(
                        'code', 'parent_code', 'name', 'is_Enabled_tsc', 'url')  # 根据角色名查询二级菜单信息
                    menu_level3 = menu.objects.filter(role__name=u_role, level=3).order_by('code',
                                                                                           'parent_code').values_list(
                        'code', 'parent_code', 'name', 'is_Enabled_tsc', 'url')  # 根据角色名查询三级菜单信息
                    # 转成真正的列表，按照0，1，2，3，4索引取‘菜单编号’，‘父亲菜单编号’，‘菜单名称’，‘是否启用’，‘url’对应的值
                    print(menu_level1)

                    ml1 = list(menu_level1)
                    ml2 = list(menu_level2)
                    ml3 = list(menu_level3)

                    request.session['ml1'] = ml1
                    request.session['ml2'] = ml2
                    request.session['ml3'] = ml3
                    # 将用户名写到cookie中
                    response = redirect('sm:index')
                    response.set_cookie('u_name', u_name)
                    dlogin(request, django_user)  # 登录成功，用django自带的用户认证,并且跳转首页
                    # return response  # 登录成功，跳转首页
                    ret_info = '登录成功'
                    ret_code = 1

        else:
            ret_info = '账号或密码错误'

        return HttpResponse(json.dumps({'ret_info': ret_info, 'ret_code': ret_code}))
    else:  # 否则为get方法
        next_to = request.GET.get('next', False)
        if request.user:  # 判断用户是否登录成功
            if next_to:
                return redirect(next_to)

    return render(request, 'login.html')  # 为登录成功，跳转到登录界面


# 注销
def logout(request):
    # u_name = request.session['u_name']
    # user_profile.objects.filter(u_name=u_name).update(u_status_tsc=2)  # 更新用户状态为注销
    # now_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
    request.session.flush()  # 删除所有的session信息
    response = redirect('sm:login')  # 重定向到登录页面
    response.delete_cookie('u_name')
    # del request.session["u_name"]  # 删除u_name
    return response
def index(request):
    return render(request, 'index.html')


###########################################################################################################
# 用户管理
@xframe_options_exempt
def userManage(request):
    menu_info = systemRoleDao.queryAllRole()
    return  render(request, 'sm/user/userManage.html', {'menu_info':menu_info})

# 获取用户数据
def getUserInfo(request):
    pageSize = request.GET.get('pageSize')
    pageNumber = request.GET.get('pageNumber')
    pageSize = int(pageSize)
    pageNumber = int(pageNumber)

    role_id = request.GET.get('role_id')  # 根据 用户 角色 id 筛选
    u_name = request.GET.get('u_name') #　根据用户名筛选
    chinese_name = request.GET.get('chinese_name') #根据中文名筛选

    print(u_name)

    user_info = systemUserDao.queryUserByRoleIdAndUnameAndCname(role_id,u_name,chinese_name) # 根据筛选条件来显示

    if user_info:
        all_list_len = user_info.__len__()  # 总的列表长度
        user_info_page = user_info[(pageNumber - 1) * pageSize:(pageNumber) * pageSize]  # 进行分页显示
        row_info_list = []
        for rs in user_info_page:
            row_info_dic = {}
            row_info_dic['id'] = rs.id
            row_info_dic['u_name'] = rs.u_name

            if rs.u_status_tsc == 1:
                row_info_dic['u_status_tsc'] = '在用'
            else:
                row_info_dic['u_status_tsc'] = '冻结'


            row_info_dic['chinese_name'] = rs.chinese_name
            row_info_dic['identity_card'] = rs.identity_card  # 身份证号
            row_info_dic['telephone_number'] = rs.telephone_number  # 手机号
            row_info_dic['wechanumber'] = rs.wechanumber
            row_info_dic['email'] = rs.email
            row_info_dic['lastlogin_date'] = common.datetimeToString(rs.lastlogin_date)  # 最后登录时间
            row_info_dic['system_role'] = rs.system_role.name
            row_info_list.append(row_info_dic)
    else:
        all_list_len = 0
        row_info_list = []
    return HttpResponse(json.dumps({'total': all_list_len, 'rows': row_info_list}),
                        content_type='application/json')

# 用户添加
@xframe_options_exempt
def userAdd(request):
    if request.method == 'POST':
        user_info = {}
        user_info['u_name'] = request.POST.get('u_name')  # 用户名不允许该
        user_info['u_pwd'] = request.POST.get('u_pwd')  # 密码
        user_info['u_status_tsc'] = request.POST.get('u_status_tsc')  # 账号状态
        user_info['chinese_name'] = request.POST.get('chinese_name')  # 中文名称
        user_info['identity_card'] = request.POST.get('identity_card')  # 身份证号
        user_info['telephone_number'] = request.POST.get('telephone_number')  # 手机号
        user_info['wechanumber'] = request.POST.get('wechanumber')  # 微信
        user_info['email'] = request.POST.get('email')  # 邮箱
        user_info['system_role_id'] = request.POST.get('system_role_id')  # 所属角色
        systemUserDao.create(user_info)
        return redirect('sm:userManage')
    else:
        role_info = role.objects.all()  # 查询角色表
        code_info = code.objects.filter(type='用户状态')
    return render(request, 'sm/user/userAdd.html', {'role_info': role_info, 'code_info': code_info})


# 用户编辑
@xframe_options_exempt
@login_required
def userEdit(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        user_info = user_profile.objects.filter(id=id).first()  # 按照id查询
        user_id = user_info.user_id
        # u_name = request.POST.get('u_name') # 用户名不允许该
        u_pwd = request.POST.get('u_pwd')
        u_status_tsc = request.POST.get('u_status_tsc')
        chinese_name = request.POST.get('chinese_name')
        telephone_number = request.POST.get('telephone_number')
        wechanumber = request.POST.get('wechanumber')
        email = request.POST.get('email')
        # appid = request.POST.get('appid')
        # lastlogin_date = request.POST.get('lastlogin_date')
        system_role_id = request.POST.get('system_role_id')
        # 更改密码，首先要更新Django自带的User表中的密码
        user = User.objects.get(id=user_id)
        user.set_password(u_pwd)
        # user.check_password(u_pwd)
        user.save()
        user_profile.objects.filter(user_id=user_id).update(u_pwd=u_pwd, u_status_tsc=u_status_tsc,
                                                            chinese_name=chinese_name,
                                                            telephone_number=telephone_number,
                                                            wechanumber=wechanumber, email=email,
                                                            system_role_id=system_role_id)
        return redirect('sm:userManage')
    else:
        id = request.GET.get('id')
        user_info = user_profile.objects.filter(id=id).first()  # 按照id查询
        role_info = role.objects.all()  # 查询角色表
        code_info = code.objects.filter(type='用户状态')
    return render(request, 'sm/user/userEdit.html',
                  {'user_info': user_info, 'role_info': role_info, 'code_info': code_info})


# 用户信息查询（用户个人信息）0
@xframe_options_exempt
@login_required
def userInfo(request):
    u_name = request.session.get('u_name')  # 从session中获取用户名
    if request.method == 'POST':
        chinese_name = request.POST.get('chinese_name')
        telephone_number = request.POST.get('telephone_number')
        wechanumber = request.POST.get('wechanumber')
        email = request.POST.get('email')
        user_profile.objects.filter(u_name=u_name).update(chinese_name=chinese_name, telephone_number=telephone_number,
                                                          wechanumber=wechanumber, email=email)
        return redirect('sm:index')
    else:
        user_info = user_profile.objects.get(u_name=u_name)  # 查询用户的个人信息
    return render(request, 'sm/user/userInfo.html', {'u_name': u_name, 'user_info': user_info})


# 用户密码修改（用户个人信息）
@xframe_options_exempt
@login_required
def userPwdUpdate(request):
    u_name = request.session.get('u_name')
    error_message = ''
    if request.method == 'POST':
        ori_pwd = request.POST.get('ori_pwd')
        new_pwd = request.POST.get('new_pwd')
        user = User.objects.get(username=u_name)  # 根据用户名获取django中的user信息
        if user.check_password(ori_pwd):  # 如果输入的原密码正确
            user.set_password(new_pwd)  # 更新新的密码
            user.save()
            user_profile.objects.filter(u_name=u_name).update(u_pwd=new_pwd)
            error_message = '修改成功'
            print('修改成功')
            return redirect('sm:login')
        else:
            error_message = '原密码不正确'
    return render(request, 'sm/user/userPwdUpdate.html', {'error_message': error_message})


# 用户删除 实际上为冻结
@login_required
def userDelById(request):
    id = request.GET.get('id')
    if systemUserDao.deleteById(id):
        ret_code = '1'
        ret_info = '冻结成功！'
    else:
        ret_code = '0'
        ret_info = '冻结失败！该用户已经冻结！'

    print(id)

    return HttpResponse(json.dumps({'ret_info': ret_info, 'ret_code': ret_code}))


# 用户信息导出
def userInfoExport(request):
    filename = '用户信息导出'
    # 设置HTTPResponse的类型
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment;filename=systemUserInfo.xls'
    ############################################################################从数据库查询
    list_obj = systemUserDao.queryAllUser()  # 获取所有的用户
    print(list_obj)
    # 定义待写入的标题列表
    headline_list = ['序号', '用户名', '状态', '中文名', '身份证号', '手机号',
                     '微信号', '邮箱', '最后登录时间', '角色']

    content_list = []  # 定义待写入的内容--列表
    i = 1
    for lo in list_obj:
        one_content = []  # 定义一条记录列表
        one_content.append(i)  # 序号
        i = i + 1
        one_content.append(lo.u_name)  # 用户名
        if lo.u_status_tsc == 1:
            one_content.append('在用')  # 状态
        else:
            one_content.append('冻结')  # 状态
        one_content.append(lo.chinese_name)  # 中文名
        one_content.append(lo.identity_card)  # 身份证号
        one_content.append(lo.telephone_number)  # 手机号
        one_content.append(lo.wechanumber)  # 微信号
        one_content.append(lo.email)  # 邮箱
        one_content.append(lo.lastlogin_date)  # 最后登录时间
        one_content.append(lo.system_role.name)  # 角色
        content_list.append(one_content)  # 添加到内容列表中
    #######################################
    wb = common.downExcel(headline_list, content_list)
    # 写出到IO
    output = io.BytesIO()
    wb.save(output)
    # 重新定位到开始
    output.seek(0)
    response.write(output.getvalue())
    return response


##########################################################################################################
# 角色管理
@login_required
@xframe_options_exempt
def roleManage(request):
    role_list = role.objects.all()
    return render(request, 'sm/role/roleManage.html', {'role_list': role_list})


# 角色添加
@login_required
@xframe_options_exempt
def roleAdd(request):
    if request.method == 'POST':
        r_name = request.POST.get('r_name')
        note = request.POST.get('note')
        menuCodeListStr = request.POST.get('menuCodeList')  # 获取权限菜单编号字符串 用逗号隔开
        role_info = role.objects.create(name=r_name, note=note)  # 先创建角色信息
        if menuCodeListStr:
            menuCodeList = menuCodeListStr.split(",")
            for menu_code in menuCodeList:
                menu_info = menu.objects.get(code=menu_code)  # 根据菜单的编号获取菜单记录
                role_info.menu_info.add(menu_info)  # 将角色和菜单的对应关系插入
        return redirect('sm:roleManage')
    return render(request, 'sm/role/roleAdd.html')


# 角色编辑（详情）
@login_required
@xframe_options_exempt
def roleEdit(request, id):
    if request.method == 'POST':
        r_name = request.POST.get('r_name')
        note = request.POST.get('note')
        menuCodeListStr = request.POST.get('menuCodeList')  # 获取权限菜单编号字符串 用逗号隔开
        menuCodeList = []  # 定义一个空list
        if menuCodeListStr != '':  # 如果从前段页面获取的menuCodeListStr为非空
            menuCodeList = menuCodeListStr.split(",")
        role_info = role.objects.get(id=id)  # 先更新母表的信息
        role_info.name = r_name
        role_info.note = note
        role_info.save()
        role_info.menu_info.clear()  # 先清空表关系
        if menuCodeList != '':
            for menu_code in menuCodeList:
                menu_info = menu.objects.get(code=menu_code)  # 根据菜单的编号获取菜单记录
                role_info.menu_info.add(menu_info)
        return redirect('sm:roleManage')
    else:
        role_info = role.objects.filter(id=id).first()  # 按照id查询,将信息回显到前段页面
    return render(request, 'sm/role/roleEdit.html', {'role_info': role_info, 'rid': id})  # 将角色的 表单信息、角色id 传到编辑页面


# 角色按照ID删除
@login_required
def roleDelById(request):
    id = request.GET.get('id')

    if systemRoleDao.deleteById(id):
        ret_code = '1'
        ret_info = '删除角色成功！'
    else:
        ret_code = '0'
        ret_info = '删除角色失败！'
    return HttpResponse(json.dumps({'ret_info': ret_info, 'ret_code': ret_code}))


# 查询和角色相关的菜单权限信息(ajax发送的异步请求)用户角色添加和角色编辑
def getMenu(request):
    menu_list = []
    if request.method == 'POST':
        menu_info = menu.objects.all()  # 查询全部的菜单信息
        rid = request.POST.get('rid')
        if rid:
            menu_info_rid = role.objects.get(id=rid).menu_info.all()  # 查询属于该角色的所有id信息
            for m in menu_info:
                menu_dict = {}
                menu_dict['id'] = int(m.code)
                menu_dict['pId'] = int(m.parent_code)
                menu_dict['name'] = m.name
                menu_dict['open'] = 'true'
                if m.level == 2:  # 如果为三级菜单，默认不展开
                    menu_dict['open'] = 'false'
                menu_dict['checked'] = 'false'
                for mr in menu_info_rid:
                    if m.code == mr.code:
                        menu_dict['checked'] = 'true'
                        break
                menu_list.append(menu_dict)
        else:
            for m in menu_info:
                menu_dict = {}
                menu_dict['id'] = int(m.code)
                menu_dict['pId'] = int(m.parent_code)
                menu_dict['name'] = m.name
                menu_dict['open'] = 'true'
                if m.level == 2:  # 如果为三级菜单，默认不展开
                    menu_dict['open'] = 'false'
                menu_dict['checked'] = 'false'
                menu_list.append(menu_dict)
        # print(menu_list)
    return HttpResponse(json.dumps(menu_list))


##########################################################################################################
# 菜单管理
@login_required
@xframe_options_exempt
def menuManage(request):
    # 查询system_menu的集合
    menu_list = menu.objects.order_by('code', 'parent_code')
    return render(request, 'sm/menu/menuManage.html', {'menu_list': menu_list})


# 按照code删除菜单
@login_required
def menuDelByCode(request):
    code = request.GET.get('code')
    if systemMenuDao.menuDelByCode(code):
        ret_code = '1'
        ret_info = '删除菜单成功！'
    else:
        ret_code = '0'
        ret_info = '删除菜单失败！'
    return HttpResponse(json.dumps({'ret_info': ret_info, 'ret_code': ret_code}))


# 编辑菜单并保存
@login_required
@xframe_options_exempt
def menuEdit(request, code):
    if request.method == 'POST':
        # menu_info = menu.objects.filter(code=code).first()  # 不先查询的话，执行save方法时，为保存操作，而非更新
        # menu_form = menuForm(request.POST, instance=menu_info)  # 没有request.FILES会报错
        # if menu_form.is_valid():
        #     menu_form.save()
        #     return redirect('sys:menuManage')
        menu_info = {}  # 定义一个菜单字典
        menu_info['code'] = request.POST.get('code')
        menu_info['name'] = request.POST.get('name')
        menu_info['parent_code'] = request.POST.get('parent_code')
        menu_info['url'] = request.POST.get('url')
        menu_info['level'] = request.POST.get('level')
        menu_info['is_Enabled_tsc'] = request.POST.get('is_Enabled_tsc')
        print(menu_info)
        systemMenuDao.update(menu_info)
        return redirect('sm:menuManage')
    else:  # 否则为get方法，根据id获取菜单信息
        menu_info = systemMenuDao.queryMenuByCode(code)
        # menu_form = menuForm(instance=menu_info)  # 创建一个新的表单,并初始化值
    return render(request, 'sm/menu/menuEdit.html', {'mcode': code, 'menu_info': menu_info})


# 添加菜单并保存
@login_required
@xframe_options_exempt
def menuAdd(request, code):
    if request.method == 'POST':
        menu_info = {}  # 定义一个菜单字典
        menu_info['code'] = request.POST.get('code')
        menu_info['name'] = request.POST.get('name')
        menu_info['parent_code'] = request.POST.get('parent_code')
        menu_info['url'] = request.POST.get('url')
        menu_info['level'] = request.POST.get('level')
        menu_info['is_Enabled_tsc'] = request.POST.get('is_Enabled_tsc')
        systemMenuDao.create(menu_info)
        return redirect('sm:menuManage')
    else:
        # 先查询当前菜单的子菜单code+0，查询到最后一个子菜单，新增的菜单再次基础上+1
        last_child = menu.objects.filter(code__startswith=code, parent_code=code).only('code').last()
        if last_child:  # 如果该菜单下存在子菜单
            new_code = str(int(last_child.code) + 1)  # 先把last_child.code 转成int 加一后再转成str,作为新增的菜单的code（菜单编码）
        else:  # 如果不存在子菜单，就新创建一个,创建规则（在当前菜单编号的后面加上‘01’）
            new_code = code + '01'
        parent_level = menu.objects.filter(code=code).only('level').first().level  # 查询当前菜单的菜单级别
        parent_code = code  # 当前菜单的code作为新增菜单的parent_code
    return render(request, 'sm/menu/menuAdd.html',
                  {'code': new_code, 'parent_code': parent_code, 'level': parent_level + 1})

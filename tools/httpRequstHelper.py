#!/usr/bin/env python
# -*- coding:utf-8 -*-

import json
import os
import time
import logging
import uuid
import hashlib
import random
from datetime import datetime, date
from decimal import Decimal
from tools.shareMethodHelper import DateEncoder
from django.http import Http404, HttpResponse
from django.utils.timezone import is_aware
from django.db.models.query import QuerySet
from django.core.cache import cache
from django.db import models
from django.db import connection
from django.core.serializers import serialize
from django.conf import settings
from tools.tokenHelper import *
from  django_redis import get_redis_connection
import requests

def callBackSucc(dict=None):
    """
    数据正常保存（删除）成功，向前端返回参数
    :param dict: 需要向前端传递的参数 封装成的字典
    :return:
    """
    try:
        if dict:
            json_str = '{"success": "True",'
            for k, v in dict.items():
                json_str += '"' + k + '":"' + str(v) + '",'
            # 为了兼容ie8，需要将json最后一个逗号去掉
            if len(json_str) > 1:
                json_str = json_str[0:len(json_str) - 1]
            json_str += '}'
        else:
            json_str = '{"success": "True", "msg": "' + Const.SAVESUCCESS + '"}'
        print("返回结果是：%s" % json_str)
        return HttpResponse(json_str, content_type="application/json")
    except Exception as e:
        logger.error(e)
        print("AOP error log in fun[callBackSucc] of tools[%s]:%s" % (appname, e))


def callBackSuccbyUseTextHtml(dict=None):
    """
    数据正常保存（删除）成功，向前端返回参数
    :param dict: 需要向前端传递的参数 封装成的字典
    :return:
    """
    try:
        if dict:
            json_str = '{"success": "True",'
            for k, v in dict.items():
                json_str += '"' + k + '":"' + str(v) + '",'
            # 为了兼容ie8，需要将json最后一个逗号去掉
            if len(json_str) > 1:
                json_str = json_str[0:len(json_str) - 1]
            json_str += '}'
        else:
            json_str = '{"success": "True", "msg": "' + Const.SAVESUCCESS + '"}'
        print("返回结果是：%s" % json_str)
        return HttpResponse(json_str, content_type="text/html")
    except Exception as e:
        logger.error(e)
        print("AOP error log in fun[callBackSucc] of tools[%s]:%s" % (appname, e))


# OK = {'success': True, 'msg': 'OK'}

# def errCallBack(msg='Error'):
#     return {'success': False, 'msg': msg}


def callBackErrUseTextHtml(dict=None):
    """
    数据保存（删除）失败时，向前端返回参数
    :param dict:
    :return:
    """
    try:
        if dict:
            json_str = '{"failure": "True",'
            for k, v in dict.items():
                json_str += '"' + k + '":"' + str(v) + '",'
            # 为了兼容ie8，需要将json最后一个逗号去掉
            if len(json_str) > 1:
                json_str = json_str[0:len(json_str) - 1]
            json_str += '}'
        else:
            json_str = '{"failure": "True", "msg": "' + Const.SAVEFAILURE + '"}'
        print("返回结果是：%s" % json_str)
        return HttpResponse(json_str, content_type="text/html")
    except Exception as e:
        logger.error(e)
        print("AOP error log in fun[callBackErr] of tools[%s]:%s" % (appname, e))


def callBackErr(dict=None):
    """
    数据保存（删除）失败时，向前端返回参数
    :param dict:
    :return:
    """
    try:
        if dict:
            json_str = '{"failure": "True",'
            for k, v in dict.items():
                json_str += '"' + k + '":"' + str(v) + '",'
            # 为了兼容ie8，需要将json最后一个逗号去掉
            if len(json_str) > 1:
                json_str = json_str[0:len(json_str) - 1]
            json_str += '}'
        else:
            json_str = '{"failure": "True", "msg": "' + Const.SAVEFAILURE + '"}'
        print("返回结果是：%s" % json_str)
        return HttpResponse(json_str, content_type="application/json")
    except Exception as e:
        logger.error(e)
        print("AOP error log in fun[callBackErr] of tools[%s]:%s" % (appname, e))


def intVal(x, default=0):
    """
    返回指定字符串的int值，如果不能正常返回其int值，则返回默认值0
    :param x:
    :param default:
    :return:
    """
    try:
        if not x:
            return default
        if not str(x).isdigit():
            return default
        return int(x)
    except Exception as e:
        logger.error(e)
        print("传入的变量值x = [%s] default = [%s]" % (x, default))
        print("AOP error log in fun[intVal] of tools[%s]:%s" % (appname, e))


def curPage(total, root):
    """
    返回json串
    :param total:
    :param root:
    :return:
    """
    try:
        json_str = {'TOTALCOUNT': total, 'ROOT': root}
        print(u"封装成的json串是：%s" % json_str)
        return json_str
    except Exception as e:
        logger.error(e)
        print("AOP error log in fun[curPage] of tools[%s]:%s" % (appname, e))
# 将返回结果转换成字典
def dictfetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]

def generate_code(code_len):
    all_char = '0123456789qazws456xedcrfvH456NUtgbyhnuAZWSjmikolpQAZWSXOLPEDCR456FVTGBYH456NUJIKOLP'
    code = ''
    for _ in range(code_len):
        num = random.randint(0,80)
        code += all_char[num]
    return code

def generate_codeNum(code_len):
    all_char = '012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789'
    code = ''
    for _ in range(code_len):
        num = random.randint(0,80)
        code += all_char[num]
    return code

def returnSuccess():
    """
    将json数据封装到HttoResponse对象并返回
    :param total:
    :param root:
    :return:
    """
    try:

        return HttpResponse(json.dumps({"code": 200,"msg": "成功","data": 1}),content_type='application/json')
    except Exception as e:
        print(e)
        print("AOP error log in fun[response4GridStore] of tools")

def returnError(msg):
    try:
        return HttpResponse(json.dumps({"code": 301,"msg": msg,"data": ""}),content_type='application/json')
    except Exception as e:
        print(e)

def returnLoginJson(code,msg,data):
    """
    将json数据封装到HttoResponse对象并返回
    :param total:
    :param root:
    :return:
    """
    try:
        return HttpResponse(json.dumps({"code": code,"msg": msg,"data": data}),content_type='application/json')
    except Exception as e:
        print(e)
        print("AOP error log in fun[response4GridStore] of tools")

def response4GridStore(total, root):
    """
    将json数据封装到HttoResponse对象并返回
    :param total:
    :param root:
    :return:
    """
    try:
        data={}
        data['totalSize']=total
        data['content']=list(root)
        return HttpResponse(json.dumps({"code": 200,"msg":None ,"data": data}, cls=DateEncoder),content_type='application/json')
    except Exception as e:
        print(e)
        print("AOP error log in fun[response4GridStore] of tools")

def response4Json(data):
    """
    将json数据封装到HttoResponse对象并返回
    :param total:
    :param root:
    :return:
    """
    try:
        return HttpResponse(json.dumps({"code": 200,"msg":None ,"data": data}, cls=DateEncoder),content_type='application/json')
    except Exception as e:
        print(e)
        print("AOP error log in fun[response4GridStore] of tools")
def createUUId():
    code = hash(str(uuid.uuid1()))
    return abs(code)

def getToken(request):
    token =get_token(request.META.get('HTTP_TOKEN'))
    return token
def createConditions(request):
    token =get_token(request.META.get('HTTP_TOKEN'))
    conditions = {}
    conditions['del_flag'] = '0'
    if 1!=token['c']:
        conditions['company_id'] =token['c']
    return conditions
def createParam(bean,request):
    token =get_token(request.META.get('HTTP_TOKEN'))
    bean.company_id=token['c']
    bean.dept_id=token['d']
    bean.create_by=token['u']
    bean.create_time=nowDateTime()
    bean.last_update_by=token['u']
    bean.last_update_time=nowDateTime()
    bean.del_flag=0
    return bean
def updateParam(bean,request):
    token =get_token(request.META.get('HTTP_TOKEN'))
    bean.last_update_by=token['u']
    bean.last_update_time=nowDateTime()
    return bean

def get_subMenus(id, menu2, menus):
    """
    :param id: 父id
    :param subMenu:子菜单列表
    :return: 没有子菜单返回None 有子菜单返回子菜单列表
    """
    try:
        _subMenus = []

        for menu in menus:
            if menu.get("parent_id") == id:
                _subMenus.append(menu)
        for sub in _subMenus:
            # menu2 = SysDept.objects.all().filter(parent_id=sub.get("id")).values().order_by("parent_id")
            menu2=[]
            for item in menus:
                if item.get("parent_id") == sub.get("id"):
                    item['parentId']=sub.get("id")
                    item['parentName']=sub.get("name")
                    menu2.append(item)
            if len(menus):
                sub['children']=get_subMenus(sub.get("id"), menu2,menus)
        # 子菜单列表不为空
        if len(_subMenus):
            return _subMenus
        else:  # 没有子菜单了
            return None
    except Exception as e:
        raise e

def response4formload(data):
    """
    将对象转成json，用于加载form表单数据
    :param object:
    :return:
    """
    try:
        ouput = '{success:true,data:' + data + '}'
        print(u'封装成的json串:%s' % ouput)
        return HttpResponse(ouput, content_type="application/json")
    except Exception as e:
        print(":%s" % (e))


def items(value):
    return {'items': list(value)}


def startLimit(jsons):
    """
    获取前端传递的查询记录起止位置字符串，返回对应的int值
    :param request:
    :return:
    """
    try:
        pageNum=0
        pageSize=10
        if ('pageNum' in jsons) :
            pageNum = jsons['pageNum']
        if ('pageSize' in jsons) :
            pageSize = jsons['pageSize']
        start, limit = intVal((pageNum-1)*pageSize, 0), intVal(pageSize, 10)
        return start, start + limit
    except Exception as e:
        print(":%s" % (e))


def getParams(request, *params):
    """
    获取前端传递的参数值，封装成字典对象
    :param request:
    :param params:
    :return:
    """
    try:
        kv = {}
        for p in params:
            if request.GET.has_key(p):
                kv[p] = smart_unicode(request.GET[p])
            elif request.POST.has_key(p):
                kv[p] = smart_unicode(request.POST[p])
            else:
                print(u"参数[%s]丢失" % str(p))
        print(u"获取的参数字典：%s" % kv)
        return kv
    except Exception as e:
        logger.error(e)
        print("AOP error log in fun[getParams] of tools[%s]:%s" % (appname, e))


def getParamByPostOrGet(request, params):
    """
    获取通过POST或GET方法传过来的参数
    :param request:
    :param params:
    :return:
    """
    try:
        if request.GET.has_key(params):
            if Const.DEBUG:
                print(u"通过GET方式传递的参数%s=%s" % (params, smart_unicode(request.GET[params])))
            return smart_unicode(request.GET[params])
        elif request.POST.has_key(params):
            if Const.DEBUG:
                print(u"通过POST方式传递的参数%s=%s" % (params, smart_unicode(request.POST[params])))
            return smart_unicode(request.POST[params])
        else:
            if Const.DEBUG:
                print(u"参数[%s]没有上传成功。" % params)
            raise Http404
    except Exception as e:
        logger.error(e)
        print("AOP error log in fun[getParamByPostOrGet] of tools[%s]:%s" % (appname, e))


def getArrayParams(reques, *params):
    kv = {}
    # 分组param
    group_kv = {}

    def filliparam(k, v):
        if k.startswith('g__'):
            arry = k.split('__')
            gname, attr, index = arry[1], arry[2], arry[3]
            if not gname in group_kv:
                group_kv[gname] = {}
            if not index in group_kv[gname]:
                group_kv[gname][index] = {}

            group_kv[gname][index][attr] = smart_unicode(v, strings_only=True)
        else:
            kv[k] = smart_unicode(v, strings_only=True)

    def checkParam(p):
        if p.startswith('g__'):
            arry = p.split('__')
            gname, attr = arry[1], arry[2]
            for g in group_kv[gname].values():
                if not attr in g:
                    raise Http404
        else:

            if not p in kv:
                raise Http404

    for k, v in reques.GET.iteritems():
        filliparam(k, v)

    for k, v in reques.POST.iteritems():
        filliparam(k, v)

    for p in params:
        checkParam(p)

    return kv, group_kv


def intStr2Array(ids):
    """
    将前端传递过来的id串（格式:1,13,14,20)转换成列表（格式:[1,13,14,20]）
    :pm ids:
    :retuararn:
    """
    try:
        if any(not i.isdigit() for i in ids.split(',')):
            raise Http404
        return [int(i) for i in ids.split(',')]
    except Exception as e:
        logger.error(e)
        print("AOP error log in fun[intStr2Array] of tools[%s]:%s" % (appname, e))


def str2Array(ids):
    """
    将前端传递过来的id串转换成列表（格式:['1','13','14','20']）
    :param ids:
    :return:
    """
    try:
        list = []
        for i in ids.split(','):
            if i.isdigit():
                list.append('"' + i + '"')
            else:
                list.append(i)
        return list
    except Exception as e:
        logger.error(e)
        print("AOP error log in fun[str2Array] of tools[%s]:%s" % (appname, e))


def obj2Json(obj, *params):
    """
    将单个对象 序列号后 转换成json格式  {id:'1',code:'001'}
    :param obj:
    :param params:
    :return:
    """
    try:
        json = '{'
        for p in params:
            if hasattr(obj, p):
                col, val = p, getattr(obj, p)
                if val:
                    print(u"属性[%s]类型为%s，属性值为[%s]" % (col, type(col), val))
                    json += p + ':' + encoder.default(val) + ','
                else:
                    print(u"属性[%s]的属性值为空[%s]" % (col, val))
                    json += p + ':"",'
            else:
                print(u"发现对象[%s]不存在的属性[%s]" % (obj, p))
                json += p + ':"",'
        # 为了兼容ie8，需要将json最后一个逗号去掉
        if len(json) > 1:
            json = json[0:len(json) - 1]
        json += '}'
        print('')  # 空一行
        return json
    except Exception as e:
        logger.error(e)
        print("AOP error log in fun[obj2Json] of tools[%s]:%s" % (appname, e))


def queryset2Json(qs, *params):
    """
    将queryset 序列化成json
    :param qs:
    :param params:
    :return:
    """
    try:
        json = '['
        for obj in qs:
            json += '{'
            for p in params:
                if hasattr(obj, p):
                    col, val = p, getattr(obj, p)
                    if val:
                        json += p + ':' + encoder.default(val) + ','
                    else:
                        json += p + ':"",'
                else:
                    json += p + ':"",'
            # 为了兼容ie8，需要将json最后一个逗号去掉
            if len(json) > 1:
                json = json[0:len(json) - 1]
            json += '},'
            print('')  # 空一行
        # 为了兼容ie8，需要将json最后一个逗号去掉
        if len(json) > 1:
            json = json[0:len(json) - 1]
        json += ']'
        return json
    except Exception as e:
        logger.error(e)
        print("AOP error log in fun[queryset2Json] of tools[%s]:%s" % (appname, e))


def idsToStr4Sql(obj):
    """
    将id组成的列表或元组串转成sql需要的形式 [1,2,3] ——> (1,2,3)
    :param obj:
    :return:
    """
    try:
        s = "('')"
        if not obj:
            return s
        elif isinstance(obj, list):
            if len(obj) == 1:
                # 将一个元素的元组特殊处理，否则会转成类似('1',)这种格式
                s = "(" + str(obj[0]) + ")"
            else:
                s = str(tuple(obj))
        elif isinstance(obj, tuple):
            if len(obj) == 1:
                # 将一个元素的元组特殊处理，否则会转成类似('1',)这种格式
                s = "(" + str(obj[0]) + ")"
            else:
                s = str(obj)
        elif isinstance(obj, str):
            s = obj
        else:
            print("不能将类型为%s的对象%s转换成字符串." % (type(obj), obj))
            return s

        return s
    except Exception as e:
        logger.error(e)
        print("AOP error log in fun[idsToStr4Sql] of tools[%s]:%s" % (appname, e))


def fillModel(kv, object, exclude=None):
    """
    将字典kv中的键值对，填充到对象object中，如果k在exclude中则此k列的值不填充
    :param kv:
    :param object:
    :param exclude:
    :return:
    """
    try:
        if not exclude: exclude = []
        for k, v in kv.iteritems():
            if k in exclude:
                continue
            if Const.DEBUG:
                print("调试模式：开始设置属性[%s]" % k)
            if not v:
                print("不存在属性[%s]的属性值" % k)
            if not hasattr(object, k):
                print("不存在名为[%s]的属性" % k)
                continue
            value, attr = v, getattr(object, k)
            if isinstance(attr, int):
                value = int(value)
            elif isinstance(attr, date):
                value = datetime.strptime(value, '%Y-%m-%d').date()  # 要求value格式为'%Y-%m-%d'
            elif isinstance(attr, datetime):
                value = datetime.fromtimestamp(
                    time.mktime(time.strptime(value, '%Y-%m-%d %H:%M:%S')))  # 要求value格式为'%Y-%m-%d %H:%M:%S'

            setattr(object, k, value)
        return object
    except Exception as e:
        logger.error(e)
        print("AOP error log in fun[fillModel] of tools[%s]:%s" % (appname, e))


def md5(str):
    """
    将传入的字符串按照MD5算法加密
    :param str:
    :return:
    """
    try:
        import hashlib
        import types
        m = hashlib.md5()
        m.update(str.encode("utf-8"))
        dm5_str = m.hexdigest()
        print(u"原字符串[%s]成功加密成MD5字符串[%s]" % (str, dm5_str))
        return dm5_str
    except Exception as e:
        print(e)


def getClientIP(request):
    """
    获取客户端ip地址
    :param request:
    :return:
    """
    try:
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
        remote_addr = request.META.get('REMOTE_ADDR')
        if x_forwarded_for:
            ip = x_forwarded_for.split(',')[0]
        elif remote_addr:
            ip = remote_addr
        else:
            ip = ''
        return ip
    except Exception as e:
        logger.error(e)
        print("AOP   error log in fun[getClientIP] of tools[%s]:%s" % (appname, e))


def executeQuery(sql):
    """
    执行django原始sql语句  并返回执行结果数据集
    :param sql:
    :return:
    """
    try:
        # 获得一个游标(cursor)对象
        cursor = connection.cursor()
        cursor.execute(sql)
        row_all = cursor.fetchall()
        col_names = [desc[0] for desc in cursor.description]
        # print("col_names===%s" % col_names)
    except Exception as e:
        logger.error(e)
        print("AOP error log in fun[executeQuery] of tools[%s]:%s" % (appname, e))
    finally:
        cursor.close()
        connection.close()
        if Const.DEBUG:
            print("正常关闭数据库连接。")
    return row_all


def getJson4Combox(rows):
    """
    将数据序列化成json，为下拉框提供数据源
    :param rows:
    :return:
    """
    try:
        json_str = '['
        for obj in rows:
            json_str += '{code:' + encoder.default(obj[0]) + ',name:' + encoder.default(obj[1]) + '},'
        # 为了兼容ie8，需要将json最后一个逗号去掉
        if len(json_str) > 1:
            json_str = json_str[0:len(json_str) - 1]
        json_str += ']'
        return json_str
    except Exception as e:
        logger.error(e)
        print("AOP error log in fun[getJson4Combox] of tools[%s]:%s" % (appname, e))


class tryGetParamResult:
    def __init__(self):
        self.value = None

    def __nonzero__(self):
        return self.value is not None

    def __init__(self):
        self.value = None


def tryGetParam(request, key):
    r = tryGetParamResult()
    if request.GET.has_key(key):
        r.value = request.GET.get(key)
    elif request.POST.has_key(key):
        r.value = request.POST.get(key)
    return r


def fileExt(filename):
    return os.path.splitext(filename)[-1].lower()


def GuidFileName(filename):
    return Guid() + fileExt(filename)


def YMD(date):
    # 封装成类似 XXXX年XX月XX日的字符串
    return str(date.year) + "年" + str(date.month) + "月" + str(date.day) + "日"


def dateTime2Str(dt):
    """
    日期时间类型格式化成字符串
    :param dt:
    :return:
    """
    try:
        if isinstance(dt, datetime):
            return dt.strftime('%Y-%m-%d %H:%M:%S')
        else:
            print("datetime转成字符串异常,[%s]类型为%s" % (dt, type(dt)))
            return dt
    except Exception as e:
        logger.error(e)
        print("AOP error log in fun[dateTime2Str] of tools[%s]:%s" % (appname, e))


def date2Str(date):
    """
    日期类型格式化成字符串
    :param date:
    :return:
    """
    try:
        if isinstance(date, date):
            return date.strftime('%Y-%m-%d')
        else:
            print("date转成字符串异常,[%s]类型为%s" % (date, type(date)))
            return date
    except Exception as e:
        logger.error(e)
        print("AOP error log in fun[date2Str] of tools[%s]:%s" % (appname, e))


def str2Date(string):
    """
    将字符串（格式必须是 yyyy-mm-dd）转换成 date 日期型，转换后的格式也是yyyy-mm-dd
    :param string:
    :return:
    """
    # string = string.decode('utf-8')
    return date.fromtimestamp(time.mktime(time.strptime(string, "%Y-%m-%d")))


def str2DateTime(string):
    """
    将字符串（格式必须是yyyy-mm-dd hh24:mi:ss）转换成 datetime 日期时间型
    :param string:
    :return:
    """
    return datetime.fromtimestamp(time.mktime(time.strptime(string, "%Y-%m-%d %H:%M:%S")))


def nowDateStr():
    """
    获取系统当前日期字符串 格式为 yyyy-mm-dd
    :return:
    """
    return time.strftime('%Y-%m-%d', time.localtime(time.time()))


def nowDateTimeStr():
    """
    获取系统当前时间字符串 格式为 yyyy-mm-dd hh24:mi:ss
    :return:
    """
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))


def nowDate():
    """
    获取系统当前日期的date类型 ，格式为 yyyy-mm-dd
    :return:
    """
    return str2Date(nowDateStr())


def nowDateTime():
    """
    获取系统当前日期时间的datetime类型 ，格式为 yyyy-mm-dd hh24:mi:ss
    :return:
    """
    return str2DateTime(nowDateTimeStr())


def Guid():
    return str(uuid.uuid4()).replace('-', '')


def Sex(val):
    return '男' if val else '女'


def RawDoc(filecode):
    code = Const.HERE + '/media/project/' + filecode
    if os.path.exists(code + '.doc'):
        code += '.doc'
    elif os.path.exists(code + '.docx'):
        code += '.docx'
    else:
        code = None
    return code


def setRedisValue(k,v):
    conn=get_redis_connection("default")
    conn.set(k,v,3600)

def getRedisValue(k):
    conn=get_redis_connection("default")
    return conn.get(k)

class ExcelRender:
    def __init__(self, title, key, width, render=None):
        self.title = title
        self.key = key
        self.width = width
        self.render = render

def gaodCoordsApi(add):
    url = 'https://restapi.amap.com/v3/geocode/geo'   # 输入API问号前固定不变的部分
    params = { 'key': 'eac1be30c468df6842eec32e9a0a8e5d',
                'address': add}                # 将两个参数放入字典
    res = requests.get(url, params)
    jd =  json.loads(res.text)
    return jd['geocodes'][0]['location']
# excel convert pdf file
if __name__ == '__main__':
    code = hash(str(uuid.uuid1()))
    print(abs(code))

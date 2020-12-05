from django.shortcuts import render,HttpResponse, redirect
import json
from fm.dao import evaluateDao
from tools import shareMethodHelper
from django.forms.models import model_to_dict
from datetime import datetime
from django.views.decorators.clickjacking import xframe_options_exempt
# Create your views here.

# 查看结算表
@xframe_options_exempt  # 必须啊添加这句话，要不然不能显示在iframe中
def fmEvaluateEntry(request):
    return render(request, 'fm/evaluate/fmEvaluateEntry.html')
# 按照查询信息
def findFmEvaluate(request):
    roleId = 1  # 1 为管理员，需要查询所有的数据
    pageSize = request.GET.get('pageSize')
    pageNumber = request.GET.get('pageNumber')
    pageSize = int(pageSize)
    pageNumber = int(pageNumber)
    applyNum = request.GET.get('applyNum')  # 申请结算单号
    evaluateState = request.GET.get('evaluateState') # 申请状态
    evaluateList = evaluateDao.queryFmEvaluate(applyNum,evaluateState)#查询结果为queryset

    # 分页
    totalLength = len(evaluateList)  # 查询结果的总长度
    evaluateListPage = evaluateList[(pageNumber - 1) * pageSize:(pageNumber) * pageSize] #一页显示的数据

    datas = []  # 存储查询结果的列表
    for eval in evaluateListPage:
        data = model_to_dict(eval)  # 将查询结果转成字典格式
        data['applyDate'] = shareMethodHelper.dateToStr(data['applyDate'])  # 注意：时间需要转换下
        data['evaluateFinishTime'] = shareMethodHelper.dateToStr(data['evaluateFinishTime']) # 时间需要转换下
        data['createTime'] = shareMethodHelper.dateTimeToStr(data['createTime']) # 时间需要转换下
        data['updateTime'] = shareMethodHelper.dateTimeToStr(data['updateTime']) # 时间需要转换下
        datas.append(data)  # 将字典添加到list中
    return HttpResponse(json.dumps({'total':totalLength,'rows':datas}),content_type='application/json') # total rows 必须叫这个名字
# 新增结算单
@xframe_options_exempt  # 必须啊添加这句话，要不然不能显示在iframe中
def addFmEvaluate(request):
    data = {}
    if request.method == 'POST':
        data = request.POST.dict()
        del data['csrfmiddlewaretoken']  # 需要删除请求参数中的token验证，其它的作为数据插入
        print(data)
        flag = evaluateDao.addFmEvaluate(data)
        return render(request, 'fm/evaluate/fmEvaluateEntry.html') # 插入成功后，跳转查询页面
    else:
        data['evaluateId'] = evaluateDao.createEvaluateId() # 创建id
        data['applyNum'] = evaluateDao.createApplyNum()  # 创建申请编号
        data['applyDate'] = shareMethodHelper.dateToStr(datetime.now()) # 转换一下日期
        data['evaluatePeopleId'] = '1111'  # 结算人id，当前登录人的（此处为测试，到时候获取）
        data['evaluatePeople'] = '李李'  # 当前登录人,此处未测试，到时候获取
        data['evaluateFinishTime'] = shareMethodHelper.dateToStr(datetime.now()) # 结算时间
        data['evaluateState'] = 0  # 结算状态( 结算完整后 修改为 2-完成 )

        data['companyId'] = 1  # 公司id （再session中获取，此处为示例）
        data['deptId'] = 2  # 机构id （再session中获取，此处为示例）
        data['createUserId'] = 1001  # 创建人id （再session中获取，此处为示例）
        data['createTime'] = shareMethodHelper.dateTimeToStr(datetime.now()) #创建时间为当前时间
        data['updateUserId'] = 1001  # 更新人id （再session中获取，此处为示例）
        data['updateTime'] = shareMethodHelper.dateTimeToStr(datetime.now()) #更新时间为当前时间
        data['delFlag'] = 2  # 1-已删除，2-未删除

        return render(request,'fm/evaluate/addFmEvaluate.html',{'data':data})
# 查看结算单信息
@xframe_options_exempt  # 必须啊添加这句话，要不然不能显示在iframe中
def viewFmEvaluate(request):
    evaluateId = request.GET.get('evaluateId')
    evaluateInfo = evaluateDao.queryFmEvaluateById(evaluateId) # 根据evaluateId去对应的纪录
    data = model_to_dict(evaluateInfo) # 将查询结果转成字典格式
    data['applyDate'] = shareMethodHelper.dateToStr(data['applyDate'])  # 时间需要转换下
    data['evaluateFinishTime'] = shareMethodHelper.dateToStr(data['evaluateFinishTime'])
    data['createTime'] = shareMethodHelper.dateTimeToStr(data['createTime'])
    data['updateTime'] = shareMethodHelper.dateTimeToStr(data['updateTime'])
    return render(request, 'fm/evaluate/viewFmEvaluate.html', {'data':data})
# 编辑结算单信息
@xframe_options_exempt  # 必须啊添加这句话，要不然不能显示在iframe中
def editFmEvaluate(request):
    if request.method == "POST":
        # 从前端获取所有的请求参数
        data = request.POST.dict()
        del data['csrfmiddlewaretoken'] # 需要删除请求参数中的token验证，其它的作为数据插入
        #如果为POST请求，则将修改之后的表单信息进行保存
        flag = evaluateDao.updateFmEvaluate(data) # 更新数据
        return render(request, 'fm/evaluate/viewFmEvaluate.html', {'data': data})
    else:
        # 如果为GET请求，跳转到编辑页面
        evaluateId = request.GET.get('evaluateId')
        evaluateInfo = evaluateDao.queryFmEvaluateById(evaluateId) # 根据evaluateId去对应的纪录
        return render(request, 'fm/evaluate/editFmEvaluate.html', {'data':evaluateInfo})
# 删除结算单信息
def delFmEvaluate(request):
    evaluateId = request.GET.get('evaluateId')
    flag = evaluateDao.delFmEvaluate(evaluateId) # 根据id删除数据
    if flag:
        code = 200  # 删除成功
    else:
        code = 500  # 删除错误
    return HttpResponse(json.dumps({"code":code,"msg":None}))



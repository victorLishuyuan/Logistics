from django.db.models import Q
from fm import models

# 增加数据
def addFmEvaluate(data):
    try:
        models.fmEvaluate.objects.create(**data)
        return True
    except Exception as e:
        print(e)
    return False

# 根据条件模糊查询
def queryFmEvaluate(applyNum,evaluateState):
    try:
        evaluateList = models.fmEvaluate.objects.filter(Q(applyNum__startswith=applyNum) & Q(evaluateState=evaluateState))
    except Exception as e:
        print(e)
    return evaluateList
# 根据id查询数据
def queryFmEvaluateById(evaluateId):
    try:
        evaluateInfo = models.fmEvaluate.objects.filter(evaluateId=evaluateId).first()
    except Exception as e:
        print(e)
    return evaluateInfo

# 查询最后一条数据
def queryLastFmEvaluate():
    try:
        evaluateInfo = models.fmEvaluate.objects.filter().last()
    except Exception as e:
        print(e)
    return evaluateInfo

# 生成主键
def createEvaluateId():
    evaluateInfo = queryLastFmEvaluate() # 查询最后一条数据
    if evaluateInfo:
        evaluateId = evaluateInfo.evaluateId # 获取id
        evaluateId = int(evaluateId) # 先转成int型
        evaluateId += 1
        evaluateId = str(evaluateId) # 再转成str
    else:
        evaluateId = '1'
    return evaluateId

# 生成申请编号
def createApplyNum():
    evaluateInfo = queryLastFmEvaluate() # 查询最后一条数据
    if evaluateInfo:
        applyNum = evaluateInfo.applyNum # 获取申请编号
        applyNum = int(applyNum) # 先转成int型
        applyNum += 1
        applyNum = str(applyNum) # 再转成str
    else:
        applyNum = '37800001'
    return applyNum

# 编辑后更新数据
def updateFmEvaluate(data):
    evaluateId = data['evaluateId'] # 根据id更新数据

    if models.fmEvaluate.objects.filter(evaluateId=evaluateId).update(**data):
        return True
    return False
# 删除数据
def delFmEvaluate(evaluateId):
    try:
        models.fmEvaluate.objects.filter(evaluateId=evaluateId).delete()
    except Exception as e:
        print(e)
        return False
    return True;


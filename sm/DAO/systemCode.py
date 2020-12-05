from sm.models import code as system_code



# 根据编码类型，查询编码信息
def queryCodeInfoByType(type):
    code_info = system_code.objects.filter(type=type)
    if code_info:
        return code_info
    return None


# 根据编码类型，返回编码的字典
def queryCodeDicInfoByType(type):
    code_info = system_code.objects.filter(type=type)
    if code_info:
        code_dic = {}
        for ci in code_info:
            code_dic[ci.code] = ci.value
        return code_dic
    return None
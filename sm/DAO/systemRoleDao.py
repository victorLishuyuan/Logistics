from sm import models



def queryAllRole():

    try:
        role_info = models.role.objects.all()
    except Exception as e:
        print(e)
        return False
    return role_info
# 根据用户 id 删除菜单
def deleteById(id):
    try:
        models.role.objects.filter(id=id).delete()
    except Exception as e:
        print(e)
        return False
    return True
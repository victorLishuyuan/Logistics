from django.db import models

# Create your models here.


# 1“企业部门信息”表
class rmOrg(models.Model):
    orgId = models.CharField(db_column = 'org_id', max_length = 32, verbose_name = '企业部门信息主键', primary_key = True)
    orgNum = models.CharField(db_column = 'org_num', max_length = 12, verbose_name = '企业部门编号')
    orgName = models.CharField(db_column = 'org_name', max_length = 50, verbose_name = '企业部门名称')
    fatherId = models.CharField(db_column = 'father_id', max_length = 32, verbose_name = '父主键id')
    orgType = models.IntegerField(db_column = 'org_type', verbose_name = '类型：1公司，2部门，3个体（个人运输车），4车队（多人团体）')
    registerTime = models.DateTimeField(db_column = 'register_time', max_length = 6, verbose_name = '注册日期',  blank = True, null = True)
    creditCode = models.CharField(db_column = 'credit_code', max_length = 32, verbose_name = '统一社会信用代码', null = True)
    deadline = models.DateTimeField(db_column = 'deadline', max_length = 6, verbose_name = '营业执照有效期',  blank = True, null = True)
    legalPersonName = models.CharField(db_column = 'legal_person_name', max_length = 20, verbose_name = '法人名称', null = True)
    legalPersonIdcard = models.CharField(db_column = 'legal_person_idcard', max_length = 18, verbose_name = '法人身份证', null = True)
    enterpriseNature = models.IntegerField(db_column = 'enterprise_nature', verbose_name = '企业性质', null = True)
    registeredCapital = models.FloatField(db_column = 'registered_capital', verbose_name = '注册资本', null = True)
    businessScope = models.CharField(db_column = 'business_scope', max_length = 300, verbose_name = '经营范围', null = True)
    enterpriseAddr = models.CharField(db_column = 'enterprise_addr', max_length = 300, verbose_name = '企业地址', null = True)
    orgTel = models.CharField(db_column = 'org_tel', max_length = 20, verbose_name = '联系电话', null = True)
    desc = models.CharField(db_column = 'desc', max_length = 2000, verbose_name = '说明', null = True)
    orgStatus = models.IntegerField(db_column = 'org_status', verbose_name = '状态：1激活，2禁用')
    companyId = models.CharField(db_column = 'company_id', max_length = 32, verbose_name = '公司ID', null = True)
    deptId = models.CharField(db_column = 'dept_id', max_length = 32, verbose_name = '机构ID', null = True)
    createUserId = models.CharField(db_column = 'create_user_id', max_length = 32, verbose_name = '创建人ID', null = True)
    createTime = models.DateTimeField(db_column = 'create_time', max_length = 6, verbose_name = '创建时间', null = True)
    updateUserId = models.CharField(db_column = 'update_user_id', max_length = 32, verbose_name = '更新人ID', null = True)
    updateTime = models.DateTimeField(db_column = 'update_time', max_length = 6, verbose_name = '更新时间', null = True)
    delFlag = models.IntegerField(db_column = 'del_flag', verbose_name = '是否删除：1已删除，2未删除', null = True)

    class Meta:
        db_table = 't_rm_org'


# 2“客户信息”表
class rmUser(models.Model):
    userId = models.CharField(db_column = 'user_id', max_length = 32, verbose_name = '企业部门信息主键', primary_key = True)
    userNum = models.CharField(db_column = 'user_num', max_length = 12, verbose_name = '编号')
    userLoginName = models.CharField(db_column = 'user_login_name', max_length = 20, verbose_name = '登录名')
    orgId = models.CharField(db_column = 'org_id', max_length = 32, verbose_name = '组织机构主键(id)')
    userPassword = models.CharField(db_column = 'user_password', max_length = 45, verbose_name = '密码')
    saltValue = models.CharField(db_column = 'salt_value', max_length = 20, verbose_name = '盐值')
    userStatus = models.IntegerField(db_column = 'user_status', verbose_name = '状态：1激活,2禁用')
    userName = models.CharField(db_column = 'user_name', max_length = 20, verbose_name = '姓名', null = True)
    userSex = models.IntegerField(db_column = 'user_sex', verbose_name = '性别：1男，2女', null = True)
    userAge = models.IntegerField(db_column = 'user_age', verbose_name = '年龄', null = True)
    userIdcard = models.CharField(db_column = 'user_idcard', max_length = 18, verbose_name = '身份证号', null = True)
    idcardDeadline = models.DateTimeField(db_column = 'idcard_deadline', max_length = 6, verbose_name = '身份证有效期',  blank = True, null = True)
    userAddr = models.CharField(db_column = 'user_addr', max_length = 200, verbose_name = '住址', null = True)
    userTel = models.CharField(db_column = 'user_tel', max_length = 20, verbose_name = '电话', null = True)
    idcardUrl = models.CharField(db_column = 'idcard_url', max_length = 28, verbose_name = '身份证url', null = True)
    userType = models.IntegerField(db_column = 'user_type', verbose_name = '用户类型：1托运人，2司机（个人），3系统用户，4车队（多人团体）', null = True)
    companyId = models.CharField(db_column = 'company_id', max_length = 32, verbose_name = '公司ID', null = True)
    deptId = models.CharField(db_column = 'dept_id', max_length = 32, verbose_name = '机构ID', null = True)
    createUserId = models.CharField(db_column = 'create_user_id', max_length = 32, verbose_name = '创建人ID', null = True)
    createTime = models.DateTimeField(db_column = 'create_time', max_length = 6, verbose_name = '创建时间', null = True)
    updateUserId = models.CharField(db_column = 'update_user_id', max_length = 32, verbose_name = '更新人ID', null = True)
    updateTime = models.DateTimeField(db_column = 'update_time', max_length = 6, verbose_name = '更新时间', null = True)
    delFlag = models.IntegerField(db_column = 'del_flag', verbose_name = '是否删除：1已删除，2未删除', null = True)

    class Meta:
        db_table = 't_rm_user'


# 3“车辆信息”表
class rmVehicle(models.Model):
    vehicleId = models.CharField(db_column = 'vehicle_id', max_length = 32, verbose_name = '主键', primary_key = True)
    userId = models.CharField(db_column = 'user_id', max_length = 32, verbose_name = '用户主键(id)')
    vehicleNum = models.CharField(db_column = 'vehicle_num', max_length = 12, verbose_name = '编号')
    buyDate = models.DateTimeField(db_column = 'buy_date', max_length = 6, verbose_name = '购买日期')
    license = models.CharField(db_column = 'license', max_length = 10, verbose_name = '牌照')
    factory = models.CharField(db_column = 'factory', max_length = 22, verbose_name = '厂家')
    brand = models.CharField(db_column = 'brand', max_length = 16, verbose_name = '品牌')
    model = models.CharField(db_column = 'model', max_length = 12, verbose_name = '型号')
    level = models.IntegerField(db_column = 'level', verbose_name = '级别：1重卡，2轻卡')
    energyType = models.IntegerField(db_column = 'energy_type', verbose_name = '能源类型：1汽油，2柴油，3电动')
    environmentalStandards = models.IntegerField(db_column = 'environmental_standards', verbose_name = '环保标准')
    vehicleLong = models.FloatField(db_column = 'vehicle_long', verbose_name = '长')
    vehicleWidth = models.FloatField(db_column = 'vehicle_width', verbose_name = '宽')
    vehicleHigh = models.FloatField(db_column = 'vehicle_high', verbose_name = '高')
    engineId = models.CharField(db_column = 'engine_id', max_length = 32, verbose_name = '发动机号', null = True)
    frameNum = models.CharField(db_column = 'frame_num', max_length = 32, verbose_name = '车架号')
    vehicleColor = models.IntegerField(db_column = 'vehicle_color', verbose_name = '颜色：红，黄，蓝，绿', null = True)
    vehicleWeight = models.FloatField(db_column = 'vehicle_weight', verbose_name = '吨位', null = True)
    vehicleType = models.CharField(db_column = 'vehicle_type', max_length = 10, verbose_name = '车辆类别：特种车辆，普通车辆', null = True)
    vehicleBody = models.CharField(db_column = 'vehicle_body', max_length = 10, verbose_name = '车厢种类：平板、厢式、栏式、罐式等', null = True)
    vehicleImagePath = models.CharField(db_column = 'vehicle_image_path', max_length = 100, verbose_name = '车辆照片路径', null = True)
    companyId = models.CharField(db_column = 'company_id', max_length = 32, verbose_name = '公司ID', null = True)
    deptId = models.CharField(db_column = 'dept_id', max_length = 32, verbose_name = '机构ID', null = True)
    createUserId = models.CharField(db_column = 'create_user_id', max_length = 32, verbose_name = '创建人ID', null = True)
    createTime = models.DateTimeField(db_column = 'create_time', max_length = 6, verbose_name = '创建时间', null = True)
    updateUserId = models.CharField(db_column = 'update_user_id', max_length = 32, verbose_name = '更新人ID', null = True)
    updateTime = models.DateTimeField(db_column = 'update_time', max_length = 6, verbose_name = '更新时间', null = True)
    delFlag = models.IntegerField(db_column = 'del_flag', verbose_name = '是否删除：1已删除，2未删除', null = True)

    class Meta:
        db_table = 't_rm_vehicle'


# 4“保险信息”表
class rmInsurance(models.Model):
    insuranceId = models.CharField(db_column = 'insurance_id', max_length = 32, verbose_name = '主键', primary_key = True)
    vehicleId = models.CharField(db_column = 'vehicle_id', max_length = 32, verbose_name = '车辆主键(id)')
    insuranceCompany = models.CharField(db_column = 'insurance_company', max_length = 32, verbose_name = '保险公司')
    insuranceType = models.IntegerField(db_column = 'insurance_type', verbose_name = '保险种类：1交强险，2商业险-三者，3商业险-车损')
    insuranceAmount = models.CharField(db_column = 'insurance_amount', max_length = 32, verbose_name = '保险金额')
    insuranceYear = models.DateTimeField(db_column = 'insurance_year', max_length = 6, verbose_name='保险年度', blank = True, null = True)
    insuranceDeadline = models.CharField(db_column = 'insurance_deadline', max_length = 32, verbose_name = '失效日期')
    insuranceImagePath1 = models.CharField(db_column = 'insurance_image_path1', max_length = 60, verbose_name = '保险图片地址1', null = True)
    insuranceImagePath2 = models.CharField(db_column = 'insurance_image_path2', max_length = 60, verbose_name = '保险图片地址2', null = True)
    insuranceImagePath3 = models.CharField(db_column = 'insurance_image_path3', max_length = 60, verbose_name = '保险图片地址3', null = True)
    companyId = models.CharField(db_column = 'company_id', max_length = 32, verbose_name = '公司ID', null = True)
    deptId = models.CharField(db_column = 'dept_id', max_length = 32, verbose_name = '机构ID', null = True)
    createUserId = models.CharField(db_column = 'create_user_id', max_length = 32, verbose_name = '创建人ID', null = True)
    createTime = models.DateTimeField(db_column = 'create_time', max_length = 6, verbose_name = '创建时间', null = True)
    updateUserId = models.CharField(db_column = 'update_user_id', max_length = 32, verbose_name = '更新人ID', null = True)
    updateTime = models.DateTimeField(db_column = 'update_time', max_length = 6, verbose_name = '更新时间', null = True)
    delFlag = models.IntegerField(db_column = 'del_flag', verbose_name = '是否删除：1已删除，2未删除', null = True)

    class Meta:
        db_table = 't_rm_insurance'


# 5“违章信息”表
class rmRegulations(models.Model):
    regulationsId = models.CharField(db_column = 'regulations_id', max_length = 32, verbose_name = '主键', primary_key = True)
    vehicleId = models.CharField(db_column = 'vehicle_id', max_length = 32, verbose_name = '车辆主键')
    regulationsTime = models.DateTimeField(db_column = 'regulations_time', max_length = 6, verbose_name = '违章时间', blank = True, null = True)
    regulationsContent = models.CharField(db_column = 'regulations_content', max_length = 200, verbose_name = '违章内容', null = True)
    result = models.IntegerField(db_column = 'result', verbose_name = '处理结果：1已处理，2未处理', null = True)
    companyId = models.CharField(db_column = 'company_id', max_length = 32, verbose_name = '公司ID')
    companyId = models.CharField(db_column = 'company_id', max_length = 32, verbose_name = '公司ID', null = True)
    deptId = models.CharField(db_column = 'dept_id', max_length = 32, verbose_name = '机构ID', null = True)
    createUserId = models.CharField(db_column = 'create_user_id', max_length = 32, verbose_name = '创建人ID', null = True)
    createTime = models.DateTimeField(db_column = 'create_time', max_length = 6, verbose_name = '创建时间', null = True)
    updateUserId = models.CharField(db_column = 'update_user_id', max_length = 32, verbose_name = '更新人ID', null = True)
    updateTime = models.DateTimeField(db_column = 'update_time', max_length = 6, verbose_name = '更新时间', null = True)
    delFlag = models.IntegerField(db_column = 'del_flag', verbose_name = '是否删除：1已删除，2未删除', null = True)

    class Meta:
        db_table = 't_rm_regulations'


# 6“资格证书”表
class rmCertificate(models.Model):
    certificateId = models.CharField(db_column = 'certificate_id', max_length = 32, verbose_name = '主键', primary_key = True)
    vehicleId = models.CharField(db_column = 'vehicle_id', max_length = 32, verbose_name = '车辆主键')
    certificateType = models.IntegerField(db_column = 'certificate_type', verbose_name = '资质类型：1营业资格证，2驾照，3危险品运输证', null = True)
    certificateNum = models.CharField(db_column = 'certificate_num', max_length = 32, verbose_name = '资质编号')
    certificateName = models.CharField(db_column = 'certificate_name', max_length = 30, verbose_name = '资质名称')
    certificateStartTime = models.DateTimeField(db_column = 'certificate_start_time', max_length = 6, verbose_name = '起始日期', blank =True, null = True)
    certificateEndTime = models.DateTimeField(db_column = 'certificate_end_time', max_length = 6, verbose_name = '终止日期', blank = True, null = True)
    certificateImagePath1 = models.CharField(db_column = 'certificate_image_path1', max_length = 30, verbose_name = '图片地址1', null = True)
    certificateImagePath2 = models.CharField(db_column = 'certificate_image_path2', max_length = 30, verbose_name = '图片地址2', null = True)
    certificateImagePath3 = models.CharField(db_column = 'certificate_image_path3', max_length = 30, verbose_name = '图片地址3', null = True)
    companyId = models.CharField(db_column = 'company_id', max_length = 32, verbose_name = '公司ID', null = True)
    deptId = models.CharField(db_column = 'dept_id', max_length = 32, verbose_name = '机构ID', null = True)
    createUserId = models.CharField(db_column = 'create_user_id', max_length = 32, verbose_name = '创建人ID', null = True)
    createTime = models.DateTimeField(db_column = 'create_time', max_length = 6, verbose_name = '创建时间', null = True)
    updateUserId = models.CharField(db_column = 'update_user_id', max_length = 32, verbose_name = '更新人ID', null = True)
    updateTime = models.DateTimeField(db_column = 'update_time', max_length = 6, verbose_name = '更新时间', null = True)
    delFlag = models.IntegerField(db_column = 'del_flag', verbose_name = '是否删除：1已删除，2未删除', null = True)

    class Meta:
        db_table = 't_rm_certificate'




















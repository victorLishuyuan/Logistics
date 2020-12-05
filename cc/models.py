from django.db import models

# Create your models here.
#表16“咨询信息”表（t_cc_advice）
class ccAdvice(models.Model):
    adviceId = models.CharField(db_column='advice_id',max_length=32, primary_key=True,)
    adviceNum = models.CharField(db_column='advice_num',max_length=20, verbose_name='系统生产编号', null=True)
    advicer = models.CharField(db_column='advicer',max_length=20, verbose_name='咨询人', null=True)
    adviceTime = models.DateField(db_column='advice_time',max_length=6, null=True, verbose_name='咨询时间为系统时间')
    adviceTel = models.CharField(db_column='advice_tel',max_length=25,verbose_name='咨询人电话', null=True)
    adviceContent = models.CharField(db_column='advice_content',max_length=500, verbose_name='咨询内容', null=True)
    handlerId=models.CharField(db_column='handler_id',max_length=32,null=True,verbose_name='处理人主键：当前登录人，外键')
    handler=models.CharField(db_column='handler',max_length=20,null=True,verbose_name='处理人为当前登录人')
    handleEndTime = models.DateField(db_column='handle_end_time',max_length=6, null=True, verbose_name='处理结束时间为系统时间')
    handleResult=models.CharField(db_column='handle_result',max_length=200, verbose_name='处理结果', null=True,)
    revisterId=models.CharField(db_column='revister_id',max_length=32,null=True,verbose_name='当前登录回访人主键，外键')
    revister=models.CharField(db_column='revister',max_length=20,null=True,verbose_name='当前登录回访人')
    returnVisitTime= models.DateField(db_column='return_visit_time',max_length=6, null=True, verbose_name='回访时间为系统时间')
    returnVisitResult=models.CharField(db_column='return_visit_result',max_length=200, verbose_name='回访结果', null=True,)
    companyId = models.CharField(db_column='company_id', max_length=32, verbose_name='公司ID', null=True)
    deptId = models.CharField(db_column='dept_id', max_length=32, verbose_name='机构ID', null=True)
    createUserId = models.CharField(db_column='create_user_id', max_length=32, verbose_name='创建人ID', null=True)
    createTime = models.DateTimeField(db_column='create_time', max_length=6, verbose_name='创建时间', null=True)
    updateUserId = models.CharField(db_column='update_user_id', max_length=32, verbose_name='更新人ID', null=True)
    updateTime = models.DateTimeField(db_column='update_time', max_length=6, verbose_name='更新时间', null=True)
    delFlag = models.IntegerField(db_column='del_flag', verbose_name='是否删除：1已删除，2未删除', null=True)
    class Meta:
        db_table = 't_cc_advice'

#表17“投诉信息”表（t_cc_complaint）
class ccComplaint(models.Model):
    complaintId=models.CharField(db_column='complaint_id',max_length=32, primary_key=True,)
    complaintNum=models.CharField(db_column='complaint_num',max_length=20,verbose_name='系统生产编号', null=True)
    complainantPeople=models.CharField(db_column='complainant_people',max_length=20,verbose_name='投诉人', null=True)
    complainantTime=models.DateField(db_column='complainant_time',max_length=6, null=True,verbose_name='投诉时间为系统时间')
    complainantTel=models.CharField(db_column='complainant_tel',max_length=25,verbose_name='投诉人电话', null=True)
    complainantContent = models.CharField(db_column='complainant_content',max_length=500, verbose_name='投诉内容', null=True)
    orderId = models.CharField(db_column='order_id',max_length=32, null=True, verbose_name='订单主键，外键')
    handlerId=models.CharField(db_column='handler_id',max_length=20,null=True,verbose_name='处理人主键：当前登录人，外键')
    handler = models.CharField(db_column='handler',max_length=20, null=True, verbose_name='处理人为当前登录人')
    handleEndTime = models.DateField(db_column='handle_end_time',max_length=6, null=True, verbose_name='处理结束时间为系统时间')
    handleResult = models.CharField(db_column='handle_result',max_length=200, verbose_name='处理结果', null=True,)
    revisterId = models.CharField(db_column='revister_id',max_length=32, null=True, verbose_name='当前登录回访人主键，外键')
    revister = models.CharField(db_column='revister',max_length=20, null=True, verbose_name='当前登录回访人')
    returnVisitTime = models.DateField(db_column='return_visit_time',max_length=6, null=True, verbose_name='回访时间为系统时间')
    returnVisitResult = models.CharField(db_column='return_visit_result',max_length=200, verbose_name='回访结果', null=True)
    companyId = models.CharField(db_column='company_id', max_length=32, verbose_name='公司ID', null=True)
    deptId = models.CharField(db_column='dept_id', max_length=32, verbose_name='机构ID', null=True)
    createUserId = models.CharField(db_column='create_user_id', max_length=32, verbose_name='创建人ID', null=True)
    createTime = models.DateTimeField(db_column='create_time', max_length=6, verbose_name='创建时间', null=True)
    updateUserId = models.CharField(db_column='update_user_id', max_length=32, verbose_name='更新人ID', null=True)
    updateTime = models.DateTimeField(db_column='update_time', max_length=6, verbose_name='更新时间', null=True)
    delFlag = models.IntegerField(db_column='del_flag', verbose_name='是否删除：1已删除，2未删除', null=True)
    class Meta:
        db_table = 't_cc_complaint'


from django.db import models
# Create your models here.
from django.db import models

# Create your models here.
# 结算表
class fmEvaluate(models.Model):
    evaluateId = models.CharField(db_column='evaluate_id',max_length=32,primary_key=True)
    userId=models.CharField(db_column='user_id',max_length=32,verbose_name='用户主键')
    applyNum=models.CharField(db_column='apply_num',max_length=12,verbose_name='申请单号')
    applyDate=models.DateField(db_column='apply_date',max_length=6,verbose_name='申请日期')
    evaluateType=models.IntegerField(db_column='evaluate_type',verbose_name='结算类型：1、货款，2、运费',null=True)
    actualEvaluateAmount=models.FloatField(db_column='actual_evaluate_amount',verbose_name='本次实结算金额',null=True)
    paymentAmount=models.FloatField(db_column='payment_amount',verbose_name='贷款金额',null=True)
    freightAmount = models.FloatField(db_column='freight_amount',verbose_name='运费金额',null=True)
    fineAmount = models.FloatField(db_column='fine_amount',verbose_name='罚款金额',null=True)
    liquidatedDamagesAmount = models.FloatField(db_column='liquidated_damages_amount',verbose_name='违约金',null=True)
    evaluateExplain= models.CharField(db_column='evaluate_explain',max_length=300, verbose_name='说明',null=True)
    evaluatePeopleId = models.CharField(db_column='evaluate_people_id',max_length=32, verbose_name='结算人主键,当前登录人',null=True)
    evaluatePeople = models.CharField(db_column='evaluate_people',max_length=20, verbose_name='结算人主键,当前登录人',null=True)
    evaluateFinishTime = models.DateField(db_column='evaluate_finish_time',max_length=6, verbose_name='结算完成时间',null=True)
    evaluateState = models.IntegerField(db_column='evaluate_state', verbose_name='状态：1、新建，2、流转，3、完成',null=True)

    companyId = models.CharField(db_column='company_id', max_length=32, verbose_name='公司ID', null=True)
    deptId = models.CharField(db_column='dept_id', max_length=32, verbose_name='机构ID', null=True)
    createUserId = models.CharField(db_column='create_user_id', max_length=32, verbose_name='创建人ID', null=True)
    createTime = models.DateTimeField(db_column='create_time', max_length=6, verbose_name='创建时间', null=True)
    updateUserId = models.CharField(db_column='update_user_id', max_length=32, verbose_name='更新人ID', null=True)
    updateTime = models.DateTimeField(db_column='update_time', max_length=6, verbose_name='更新时间', null=True)
    delFlag = models.IntegerField(db_column='del_flag', verbose_name='是否删除·：1已删除，2未删除', null=True)
    class Meta:
        db_table = 't_fm_evaluate'


class fmEvaluateInfo(models.Model):
    evaluateInfoId = models.CharField(db_column='evaluate_info_id',max_length=32, primary_key=True,)
    evaluateId = models.CharField(db_column='evaluate_id',max_length=32,verbose_name='结算申请单主键')
    orderId = models.CharField(db_column='order_id',max_length=32, verbose_name='订单主键：关联已完成未结算的订单')
    companyId = models.CharField(db_column='company_id', max_length=32, verbose_name='公司ID', null=True)
    deptId = models.CharField(db_column='dept_id', max_length=32, verbose_name='机构ID', null=True)
    createUserId = models.CharField(db_column='create_user_id', max_length=32, verbose_name='创建人ID', null=True)
    createTime = models.DateTimeField(db_column='create_time', max_length=6, verbose_name='创建时间', null=True)
    updateUserId = models.CharField(db_column='update_user_id', max_length=32, verbose_name='更新人ID', null=True)
    updateTime = models.DateTimeField(db_column='update_time', max_length=6, verbose_name='更新时间', null=True)
    delFlag = models.IntegerField(db_column='del_flag', verbose_name='是否删除：1已删除，2未删除', null=True)
    class Meta:
        db_table = 't_fm_evaluateInfo'

from django.db import models

# Create your models here.
# 表18
class wfWorkflowType(models.Model):
    WorkflowTypeId = models.CharField(db_column='workflow_type_id',max_length=32,primary_key=True,verbose_name="主键")
    orderType = models.CharField(db_column='order_type',max_length=2, verbose_name="订单类型",null=False)
    workflowId = models.ForeignKey('wf.wfWorkflow',null=False, to_field='workflowId', on_delete=models.CASCADE,
                             verbose_name="工作流外键",db_column='workflow_id')

    # 默认添加字段
    companyId = models.CharField(db_column='company_id',max_length=32, verbose_name='公司ID')
    deptId = models.CharField(db_column='dept_id',max_length=32, verbose_name='机构ID')
    createUserId = models.CharField(db_column='create_user_id',max_length=32, verbose_name='创建人ID')
    createTime = models.DateTimeField(db_column='create_time',max_length=6, verbose_name='创建时间')
    updateUserId = models.CharField(db_column='update_user_id',max_length=32, verbose_name='更新人ID')
    updateTime = models.DateTimeField(db_column='update_time',max_length=6, verbose_name='更新时间')
    delFlag = models.IntegerField(db_column='del_flag',max_length=2, verbose_name="是否删除，1为删除，0为未删除")
    class Meta:
        db_table='t_wf_workflow_type'

# 表19
class wfWorkflow(models.Model):
    WorkflowId = models.CharField(db_column='workflow_id',max_length=32,primary_key=True,verbose_name="主键")
    wfNumber = models.CharField(db_column='wf_number',max_length=12, verbose_name="工作流编号")
    wfName = models.CharField(db_column='wf_name',max_length=20, verbose_name="工作流名名称")
    wfStatus = models.IntegerField(db_column='wf_status',max_length=2,verbose_name="状态")

    # 默认添加字段
    companyId = models.CharField(db_column='company_id', max_length=32, verbose_name='公司ID')
    deptId = models.CharField(db_column='dept_id', max_length=32, verbose_name='机构ID')
    createUserId = models.CharField(db_column='create_user_id', max_length=32, verbose_name='创建人ID')
    createTime = models.DateTimeField(db_column='create_time', max_length=6, verbose_name='创建时间')
    updateUserId = models.CharField(db_column='update_user_id', max_length=32, verbose_name='更新人ID')
    updateTime = models.DateTimeField(db_column='update_time', max_length=6, verbose_name='更新时间')
    delFlag = models.IntegerField(db_column='del_flag', max_length=2, verbose_name="是否删除，1为删除，0为未删除")
    class Meta:
        db_table='t_wf_workflow'

# 表20
class wfWorkflowStep(models.Model):
    WorkflowStepId = models.CharField(db_column='workflow_step_id',max_length=32,primary_key=True,verbose_name="主键")
    workflowId = models.ForeignKey('wf.wfWorkflow',null=False, to_field='WorkflowId', on_delete=models.CASCADE,
                             verbose_name="工作流外键",db_column='workflow_id')
    stepNumber = models.CharField(db_column='step_number',max_length=12, verbose_name="步骤编号",null=False)
    stepName = models.CharField(db_column='step_name',max_length=20, verbose_name="步骤名称")
    examParty = models.IntegerField(db_column='exam_party',max_length=2, verbose_name="审批方", null=False)
    nextStep = models.CharField(db_column='next_step',max_length=300, verbose_name="下一步")
    backStep = models.CharField(db_column='back_step',max_length=300, verbose_name="回退")
    acceptPeople = models.CharField(db_column='accept_people',max_length=300, verbose_name="审批人")

    # 默认添加字段
    companyId = models.CharField(db_column='company_id', max_length=32, verbose_name='公司ID')
    deptId = models.CharField(db_column='dept_id', max_length=32, verbose_name='机构ID')
    createUserId = models.CharField(db_column='create_user_id', max_length=32, verbose_name='创建人ID')
    createTime = models.DateTimeField(db_column='create_time', max_length=6, verbose_name='创建时间')
    updateUserId = models.CharField(db_column='update_user_id', max_length=32, verbose_name='更新人ID')
    updateTime = models.DateTimeField(db_column='update_time', max_length=6, verbose_name='更新时间')
    delFlag = models.IntegerField(db_column='del_flag', max_length=2, verbose_name="是否删除，1为删除，0为未删除")
    class Meta:
        db_table='t_wf_workflow_step'

# 表21
class wfReplace(models.Model):
    ReplaceId = models.CharField(db_column='replace_id',max_length=32,primary_key=True,verbose_name="主键")
    workflowStepId = models.ForeignKey('wf.wfWorkflowStep',null=False, to_field='workflowStepId', on_delete=models.CASCADE,
                             verbose_name="流转步骤外键",db_column='workflow_step_id')
    number = models.CharField(db_column='number',max_length=12, verbose_name="编码",null=False)
    field = models.CharField(db_column='filed',max_length=20, verbose_name="字段",null=False)
    name = models.CharField(db_column='name',max_length=20, verbose_name="名称")
    isDisplay= models.IntegerField(db_column='is_display',max_length=2, verbose_name="是否显示")
    isChange = models.IntegerField(db_column='is_change',max_length=2, verbose_name="是否可编辑")
    isNecessary = models.IntegerField(db_column='is_necessary',max_length=2, verbose_name="是否必填")

    # 默认添加字段
    companyId = models.CharField(db_column='company_id', max_length=32, verbose_name='公司ID')
    deptId = models.CharField(db_column='dept_id', max_length=32, verbose_name='机构ID')
    createUserId = models.CharField(db_column='create_user_id', max_length=32, verbose_name='创建人ID')
    createTime = models.DateTimeField(db_column='create_time', max_length=6, verbose_name='创建时间')
    updateUserId = models.CharField(db_column='update_user_id', max_length=32, verbose_name='更新人ID')
    updateTime = models.DateTimeField(db_column='update_time', max_length=6, verbose_name='更新时间')
    delFlag = models.IntegerField(db_column='del_flag', max_length=2, verbose_name="是否删除，1为删除，0为未删除")
    class Meta:
        db_table='t_wf_replace'

# 表22
class wfLog(models.Model):
    logId = models.CharField(db_column='log_id',max_length=32,primary_key=True,verbose_name="主键")
    workflowId = models.ForeignKey('wf.wfWorkflow',null=False, to_field='workflowId', on_delete=models.CASCADE,
                             verbose_name="工作流外键",db_column='workflow_id')
    workflowStepId = models.ForeignKey('wf.wfWorkflowStep', null=False, to_field='workflowStepId',
                                    on_delete=models.CASCADE,verbose_name="流转步骤外键",db_column='workflow_step_id')
    peopleNumber = models.CharField(db_column='people_number',max_length=12, verbose_name="处理人编码",null=False,auto_created=True)
    peopleName = models.CharField(db_column='people_name',max_length=20, verbose_name="处理人名称",null=False,auto_created=True)
    startTime = models.DateField(db_column='start_time',max_length=6, verbose_name="处理开始时间")
    endTime= models.DateField(db_column='end_time',max_length=6, verbose_name="处理结束时间")
    comment = models.CharField(db_column='comment',max_length=200, verbose_name="是否可编辑",null=False)

    # 默认添加字段
    companyId = models.CharField(db_column='company_id', max_length=32, verbose_name='公司ID')
    deptId = models.CharField(db_column='dept_id', max_length=32, verbose_name='机构ID')
    createUserId = models.CharField(db_column='create_user_id', max_length=32, verbose_name='创建人ID')
    createTime = models.DateTimeField(db_column='create_time', max_length=6, verbose_name='创建时间')
    updateUserId = models.CharField(db_column='update_user_id', max_length=32, verbose_name='更新人ID')
    updateTime = models.DateTimeField(db_column='update_time', max_length=6, verbose_name='更新时间')
    delFlag = models.IntegerField(db_column='del_flag', max_length=2, verbose_name="是否删除，1为删除，0为未删除")
    class Meta:
        db_table='t_wf_log'



from django.db import models


# Create your models here.
# 表7：订单基本信息
class omOrder(models.Model):
    orderId = models.AutoField(db_column='order_id',max_length=32,primary_key=True)
    transporterId = models.CharField(db_column='transporter_id',max_length=32,verbose_name='托运人主键(外键)')
    contractId = models.CharField(db_column='contract_id',max_length=32,verbose_name='电子合同主键(外键)')
    transporter = models.CharField(db_column='transporter',max_length=20, verbose_name='托运人')
    transporterTel = models.CharField(db_column='transporter_tel',max_length=30, verbose_name='托运人电话')
    getAddr = models.CharField(db_column='get_addr',max_length=150, verbose_name='取货地址')
    receiver = models.CharField(db_column='receiver',max_length=20, verbose_name='收货人')
    receiverTel = models.CharField(db_column='receiver_tel',max_length=30, verbose_name='收货人电话')
    unloadAddr = models.CharField(db_column='unload_addr',max_length=150, verbose_name='卸货地址')
    transporterMethod = models.IntegerField(db_column='transporter_method',verbose_name='运输方式：1-汽运，2-火车，3-海运')
    getGoodsTime = models.DateTimeField(db_column='get_goods_time',verbose_name='取货时间',null=True)
    carStartTime = models.DateTimeField(db_column='car_start_time',verbose_name='发车时间',null=True)
    arriveGoodsTime = models.DateTimeField(verbose_name='到货时间',null=True)
    transform = models.IntegerField(db_column='transform',verbose_name='是否中转运输：1-是，2-否', null=True)
    ordinaryTicket = models.IntegerField(db_column='ordinary_ticket',verbose_name='是否开票：1-是，2-否', null=True)
    specialTicket = models.IntegerField(db_column='special_ticket',verbose_name='是否专票：1-是，2-否', null=True)
    taxpayerName = models.CharField(db_column='taxpayer_name',max_length=50, verbose_name='纳税人名称', null=True)
    taxpayerNum = models.CharField(db_column='taxpayer_num',max_length=30, verbose_name='纳税人识别号', null=True)
    taxpayerAddr = models.CharField(db_column='taxpayer_addr',max_length=280, verbose_name='纳税人地址', null=True)
    taxpayerTel = models.CharField(db_column='taxpayer_tel',max_length=20, verbose_name='纳税人电话', null=True)
    taxpayerBank = models.CharField(db_column='taxpayer_bank',max_length=280, verbose_name='纳税人开户行', null=True)
    taxpayerBannkNum = models.CharField(db_column='taxpayer_bannk_num',max_length=24, verbose_name='纳税人识账号', null=True)
    sendOrder = models.IntegerField(db_column='send_order',verbose_name='是否发货单：1-是，2-否', null=True)
    transportOrder = models.IntegerField(db_column='transport_order',verbose_name='是否托运单：1-是，2-否', null=True)
    backOrder = models.IntegerField(db_column='back_order',verbose_name='是否回单：1-是，2-否', null=True)
    orderAmount = models.FloatField(db_column='order_amount',verbose_name='订单金额',null=True)
    evaluateMethod = models.IntegerField(db_column='evaluate_method',verbose_name='结算方式：1-是，2-否', null=True)
    payMethod = models.IntegerField(db_column='pay_method',verbose_name='付款方式：1-是，2-否', null=True)
    payStatus = models.IntegerField(db_column='pay_status',verbose_name='付款状态：1-是，2-否', null=True)
    orderStatus = models.IntegerField(db_column='order_status',verbose_name='订单状态：0-订单成功未付款，1-用户已付，2-已派单，3-已完成', null=True)
    carDemand = models.CharField(db_column='car_demand',max_length=280, verbose_name='车辆要求', null=True)
    goodsDemand = models.CharField(db_column='goods_demand',max_length=280, verbose_name='货物要求', null=True)
    otherDemand = models.CharField(db_column='other_demand',max_length=280, verbose_name='其他要求', null=True)

    companyId = models.CharField(db_column='company_id', max_length=32, verbose_name='公司ID', null=True)
    deptId = models.CharField(db_column='dept_id', max_length=32, verbose_name='机构ID', null=True)
    createUserId = models.CharField(db_column='create_user_id', max_length=32, verbose_name='创建人ID', null=True)
    createTime = models.DateTimeField(db_column='create_time', verbose_name='创建时间', null=True)
    updateUserId = models.CharField(db_column='update_user_id', max_length=32, verbose_name='更新人ID', null=True)
    updateTime = models.DateTimeField(db_column='update_time', verbose_name='更新时间', null=True)
    delFlag = models.IntegerField(db_column='del_flag', verbose_name='是否删除：1已删除，2未删除', null=True)

    class Meta:
        db_table = 't_om_order'


# 表8：订单货物信息
class omDetail(models.Model):
    detailId = models.AutoField(db_column='detail_id',max_length=32,primary_key=True)
    orderId = models.CharField(db_column='order_id',max_length=32, verbose_name='订单主键(外键)')
    goodsNum = models.CharField(db_column='goods_num',max_length=12, verbose_name='货物编号')
    goodsName = models.CharField(db_column='goods_name',max_length=50, verbose_name='货物名称')
    goodsType = models.CharField(db_column='goods_type',max_length=20, verbose_name='货物种类')
    goodsWeight = models.FloatField(db_column='goods_weight',verbose_name='货物重量',null=True)
    goodsVolume = models.FloatField(db_column='goods_volume',verbose_name='货物体积', null=True)
    goodsQuantity = models.IntegerField(db_column='goods_quantity',verbose_name='货物数量')
    goodsPrice = models.FloatField(db_column='goods_price',verbose_name='货物价格')
    goodsTotalPrice = models.FloatField(db_column='goods_total_price',verbose_name='货物总价')

    companyId = models.CharField(db_column='company_id', max_length = 32, verbose_name = '公司ID', null = True)
    deptId = models.CharField(db_column='dept_id', max_length = 32, verbose_name = '机构ID', null = True)
    createUserId = models.CharField(db_column='create_user_id', max_length = 32, verbose_name = '创建人ID', null = True)
    createTime = models.DateTimeField(db_column='create_time', verbose_name = '创建时间', null = True)
    updateUserId = models.CharField(db_column='update_user_id', max_length = 32, verbose_name = '更新人ID', null = True)
    updateTime = models.DateTimeField(db_column='update_time', verbose_name = '更新时间', null = True)
    delFlag = models.IntegerField(db_column='del_flag', verbose_name = '是否删除：1已删除，2未删除', null = True)

    class Meta:
        db_table = 't_om_detail'


# 表8：仓库货物信息
class omDetailWarehouse(models.Model):
    warehouseId = models.AutoField(db_column='warehouse_id',max_length=32, primary_key=True)
    time = models.DateTimeField(db_column='time',verbose_name='当前系统时间')
    detailId = models.CharField(db_column='detail_id',max_length=32, verbose_name='订单货物信息主键(外键)')
    warehouseLocal = models.CharField(db_column='warehouse_local',max_length=32, verbose_name='仓库系统中位置主键(外键)')

    companyId = models.CharField(db_column='company_id', max_length = 32, verbose_name = '公司ID', null = True)
    deptId = models.CharField(db_column='dept_id', max_length = 32, verbose_name = '机构ID', null = True)
    createUserId = models.CharField(db_column='create_user_id', max_length = 32, verbose_name = '创建人ID', null = True)
    createTime = models.DateTimeField(db_column='create_time', verbose_name = '创建时间', null = True)
    updateUserId = models.CharField(db_column='update_user_id', max_length = 32, verbose_name = '更新人ID', null = True)
    updateTime = models.DateTimeField(db_column='update_time', verbose_name = '更新时间', null = True)
    delFlag = models.IntegerField(db_column='del_flag', verbose_name = '是否删除：1已删除，2未删除', null = True)

    class Meta:
        db_table = 't_om_detail_warehouse'


# 表9：电子合同信息表
class omConcract(models.Model):
    contractId = models.AutoField(db_column='contract_id',max_length=32, primary_key=True)
    contractNum = models.CharField(db_column='contract_num',max_length=32, verbose_name='合同编号')
    contractName = models.CharField(db_column='contract_name',max_length=100,verbose_name='合同名称')
    signTime = models.DateTimeField(db_column='sign_time',verbose_name='签订时间')
    contractStartTime = models.DateTimeField(db_column='contract_start_time',verbose_name='合同生效时间', null=True)
    contractEndTime = models.DateTimeField(db_column='contract_end_time',verbose_name='合同结束时间', null=True)
    contractAddr = models.CharField(db_column='contract_addr',max_length=280,verbose_name='合同签订地点')
    firstCompanyName = models.CharField(db_column='first_company_name',max_length=50, verbose_name='甲方单位名称')
    firstPersonName = models.CharField(db_column='first_person_name',max_length=20, verbose_name='甲方联系人')
    firstPersonTel = models.CharField(db_column='first_person_tel',max_length=20, verbose_name='甲方联系人电话')
    secondCompanyName = models.CharField(db_column='second_company_name',max_length=50, verbose_name='乙方单位名称')
    secondPersonName = models.CharField(db_column='second_person_name',max_length=20, verbose_name='乙方联系人')
    secondPersonTel = models.CharField(db_column='second_person_tel',max_length=20, verbose_name='乙方联系人电话')
    contractAttachment = models.CharField(db_column='contract_attachment',max_length=30, verbose_name='合同附件',null=True)

    companyId = models.CharField(db_column='company_id', max_length=32, verbose_name='公司ID', null=True)
    deptId = models.CharField(db_column='dept_id', max_length=32, verbose_name='机构ID', null=True)
    createUserId = models.CharField(db_column='create_user_id', max_length=32, verbose_name='创建人ID', null=True)
    createTime = models.DateTimeField(db_column='create_time', verbose_name='创建时间', null=True)
    updateUserId = models.CharField(db_column='update_user_id', max_length=32, verbose_name='更新人ID', null=True)
    updateTime = models.DateTimeField(db_column='update_time', verbose_name='更新时间', null=True)
    delFlag = models.IntegerField(db_column='del_flag', verbose_name='是否删除：1已删除，2未删除', null=True)

    class Meta:
        db_table = 't_om_concract'


# 表10：电子提货单信息
class omBl(models.Model):
    blId = models.AutoField(db_column='bl_id', max_length=32, primary_key=True)
    orderId = models.CharField(db_column='order_id', max_length=32, verbose_name='订单主键(外键)')
    blPerson = models.CharField(db_column='bl_person', max_length=32, verbose_name='提货人')
    blTime = models.DateTimeField(db_column='bl_time', verbose_name='提货时间')
    blStatus = models.IntegerField(db_column='bl_status', verbose_name='状态：1-完成，2-否')

    companyId = models.CharField(db_column = 'company_id', max_length = 32, verbose_name = '公司ID', null = True)
    deptId = models.CharField(db_column = 'dept_id', max_length = 32, verbose_name = '机构ID', null = True)
    createUserId = models.CharField(db_column = 'create_user_id', max_length = 32, verbose_name = '创建人ID', null = True)
    createTime = models.DateTimeField(db_column = 'create_time', verbose_name = '创建时间', null = True)
    updateUserId = models.CharField(db_column = 'update_user_id', max_length = 32, verbose_name = '更新人ID', null = True)
    updateTime = models.DateTimeField(db_column = 'update_time', verbose_name = '更新时间', null = True)
    delFlag = models.IntegerField(db_column = 'del_flag', verbose_name = '是否删除：1已删除，2未删除', null = True)

    class Meta:
        db_table = 't_om_bl'


# 表11：电子回单信息表
class omBackOrder(models.Model):
    backOrderId = models.AutoField(db_column='back_order_id', max_length=32, primary_key=True)
    orderId = models.CharField(db_column='order_id', max_length=32, verbose_name='订单主键(外键)')
    signer = models.CharField(db_column='signer',max_length=20, verbose_name='签收人',null=True)
    signerTime = models.DateTimeField(db_column='signer_time', verbose_name='签收时间', null=True)
    signerOpinion = models.CharField(db_column='signer_opinion', max_length=320, verbose_name='签收意见', null=True)
    backOrderStatus = models.IntegerField(db_column='back_order_status', verbose_name='签收状态：1-完成，2-未回单', null=True)
    backOrderImagePath1 = models.CharField(db_column='back_order_Image_path1', max_length=60, verbose_name='照片1', null=True)
    backOrderImagePath2 = models.CharField(db_column='back_order_Image_path2', max_length=60, verbose_name='照片2', null=True)
    backOrderImagePath3 = models.CharField(db_column='back_order_Image_path3', max_length=60, verbose_name='照片3', null=True)

    companyId = models.CharField(db_column = 'company_id', max_length = 32, verbose_name = '公司ID', null = True)
    deptId = models.CharField(db_column = 'dept_id', max_length = 32, verbose_name = '机构ID', null = True)
    createUserId = models.CharField(db_column = 'create_user_id', max_length = 32, verbose_name = '创建人ID', null = True)
    createTime = models.DateTimeField(db_column = 'create_time', verbose_name = '创建时间', null = True)
    updateUserId = models.CharField(db_column = 'update_user_id', max_length = 32, verbose_name = '更新人ID', null = True)
    updateTime = models.DateTimeField(db_column = 'update_time', verbose_name = '更新时间', null = True)
    delFlag = models.IntegerField(db_column = 'del_flag', verbose_name = '是否删除：1已删除，2未删除', null = True)
    class Meta:
        db_table = 't_om_back_order'


# 表12“车辆轨迹信息”表（t_om_vehicle_trajectory）
class omVehicleTrajectory(models.Model):
    vehicleTrajectoryId=models.CharField(db_column='vehicle_trajectory_id',max_length=32,primary_key=True,)
    carId=models.CharField(db_column='car_id',max_length=32,verbose_name='车辆主键，外键', null=True)
    orderId=models.CharField(db_column='order_id',max_length=32,verbose_name='订单主键，外键', null=True)
    trajectoryTime=models.DateField(db_column='trajectory_time',max_length=6,verbose_name='车辆轨迹信息时间',null=True)
    longitude=models.FloatField(db_column='longitude',verbose_name='经度',null=True)
    latitude = models.FloatField(db_column='latitude',verbose_name='纬度', null=True)
    companyId = models.CharField(db_column='company_id', max_length=32, verbose_name='公司ID', null=True)
    deptId = models.CharField(db_column='dept_id', max_length=32, verbose_name='机构ID', null=True)
    createUserId = models.CharField(db_column='create_user_id', max_length=32, verbose_name='创建人ID', null=True)
    createTime = models.DateTimeField(db_column='create_time', max_length=6, verbose_name='创建时间', null=True)
    updateUserId = models.CharField(db_column='update_user_id', max_length=32, verbose_name='更新人ID', null=True)
    updateTime = models.DateTimeField(db_column='update_time', max_length=6, verbose_name='更新时间', null=True)
    delFlag = models.IntegerField(db_column='del_flag', verbose_name='是否删除：1已删除，2未删除', null=True)

    class Meta:
        db_table = 't_om_vehicle_trajectory'


# 表13“订单评价信息”表（t_om_appraise）
class omAppraise(models.Model):
    appraiseId = models.CharField(db_column='appraise_id',max_length=32, primary_key=True,)
    orderId = models.CharField(db_column='order_id',max_length=32, verbose_name='订单主键，外键', null=True)
    vehicleRating = models.IntegerField(db_column='vehicle_rating',verbose_name='车辆评分', null=True)
    cargoRating = models.IntegerField(db_column='cargo_rating', verbose_name='货物评分', null=True)
    transporterRating = models.IntegerField(db_column='transporter_rating', verbose_name='托运人评分', null=True)
    appraiseContent = models.CharField(db_column='appraise_content',max_length=320, verbose_name='评价内容', null=True )
    companyId = models.CharField(db_column='company_id', max_length=32, verbose_name='公司ID', null=True)
    deptId = models.CharField(db_column='dept_id', max_length=32, verbose_name='机构ID', null=True)
    createUserId = models.CharField(db_column='create_user_id', max_length=32, verbose_name='创建人ID', null=True)
    createTime = models.DateTimeField(db_column='create_time',max_length=6, verbose_name='创建时间', null=True)
    updateUserId = models.CharField(db_column='update_user_id', max_length=32, verbose_name='更新人ID', null=True)
    updateTime = models.DateTimeField(db_column='update_time',max_length=6,verbose_name='更新时间', null=True)
    delFlag = models.IntegerField(db_column='del_flag', verbose_name='是否删除：1已删除，2未删除', null=True)
    companyId = models.CharField(db_column='company_id', max_length=32, verbose_name='公司ID', null=True)
    deptId = models.CharField(db_column='dept_id', max_length=32, verbose_name='机构ID', null=True)
    createUserId = models.CharField(db_column='create_user_id', max_length=32, verbose_name='创建人ID', null=True)
    createTime = models.DateTimeField(db_column='create_time', max_length=6, verbose_name='创建时间', null=True)
    updateUserId = models.CharField(db_column='update_user_id', max_length=32, verbose_name='更新人ID', null=True)
    updateTime = models.DateTimeField(db_column='update_time', max_length=6, verbose_name='更新时间', null=True)
    delFlag = models.IntegerField(db_column='del_flag', verbose_name='是否删除：1已删除，2未删除', null=True)

    class Meta:
        db_table = 't_om_appraise'





















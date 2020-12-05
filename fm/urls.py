from django.conf.urls import url
from fm.view import fm_evaluate_views
app_name = 'fm'
urlpatterns = [
    url(r'^fmEvaluateEntry/$', fm_evaluate_views.fmEvaluateEntry, name='fmEvaluateEntry'), # 总览信息
    url(r'^addFmEvaluate/$', fm_evaluate_views.addFmEvaluate, name='addFmEvaluate'),
    url(r'^findFmEvaluate/$', fm_evaluate_views.findFmEvaluate, name='findFmEvaluate'),#查询结算表信息
    url(r'^viewFmEvaluate/$', fm_evaluate_views.viewFmEvaluate, name='viewFmEvaluate'), # 查询某条结算表信息
    url(r'^editFmEvaluate/$', fm_evaluate_views.editFmEvaluate, name='editFmEvaluate'), # 编辑某条结算表信息
    url(r'^delFmEvaluate/$', fm_evaluate_views.delFmEvaluate, name='delFmEvaluate')  # 删除某条结算表信息


]
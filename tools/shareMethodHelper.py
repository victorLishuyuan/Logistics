import datetime
import json

# 将data转成str
def dateToStr(date):
	str = date.strftime('%Y-%m-%d')
	return str
# 将datatime转成str
def dateTimeToStr(datetime):
	str = datetime.strftime('%Y-%m-%d %H:%M:%S')
	return str
# json序列化重写
class DateEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime.datetime):
            return obj.strftime("%Y-%m-%d %H:%M:%S")
        else:
            return json.JSONEncoder.default(self, obj)



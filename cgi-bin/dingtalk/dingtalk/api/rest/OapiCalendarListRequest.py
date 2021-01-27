'''
Created by auto_sdk on 2020.01.21
'''
from dingtalk.api.base import RestApi
class OapiCalendarListRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.calendar_folder_id = None
		self.i_cal_uid = None
		self.max_results = None
		self.page_token = None
		self.single_events = None
		self.time_max = None
		self.time_min = None
		self.user_id = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.calendar.list'

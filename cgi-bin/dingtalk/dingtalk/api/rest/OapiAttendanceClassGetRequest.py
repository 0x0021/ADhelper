'''
Created by auto_sdk on 2020.12.25
'''
from dingtalk.api.base import RestApi
class OapiAttendanceClassGetRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.class_id = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.attendance.class.get'

'''
Created by auto_sdk on 2020.10.27
'''
from dingtalk.api.base import RestApi
class OapiAttendanceGroupScheduleClearRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.op_userid = None
		self.param = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.attendance.group.schedule.clear'

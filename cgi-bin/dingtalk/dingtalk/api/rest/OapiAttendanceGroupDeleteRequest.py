'''
Created by auto_sdk on 2020.08.26
'''
from dingtalk.api.base import RestApi
class OapiAttendanceGroupDeleteRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.group_key = None
		self.op_userid = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.attendance.group.delete'

'''
Created by auto_sdk on 2019.07.01
'''
from dingtalk.api.base import RestApi
class OapiAttendanceCorpConfirmRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.corp_id = None
		self.corp_list = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.attendance.corp.confirm'

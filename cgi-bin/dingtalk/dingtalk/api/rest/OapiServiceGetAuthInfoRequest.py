'''
Created by auto_sdk on 2020.02.26
'''
from dingtalk.api.base import RestApi
class OapiServiceGetAuthInfoRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.auth_corpid = None
		self.suite_key = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.service.get_auth_info'

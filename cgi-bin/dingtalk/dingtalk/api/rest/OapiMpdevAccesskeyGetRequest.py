'''
Created by auto_sdk on 2020.10.15
'''
from dingtalk.api.base import RestApi
class OapiMpdevAccesskeyGetRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.miniapp_id = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.mpdev.accesskey.get'

'''
Created by auto_sdk on 2020.10.20
'''
from dingtalk.api.base import RestApi
class OapiV2SafeSetdisableRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.reason = None
		self.userid = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.v2.safe.setdisable'

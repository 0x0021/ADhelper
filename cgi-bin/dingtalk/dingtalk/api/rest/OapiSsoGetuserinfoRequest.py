'''
Created by auto_sdk on 2018.07.25
'''
from dingtalk.api.base import RestApi
class OapiSsoGetuserinfoRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.access_token = None
		self.code = None

	def getHttpMethod(self):
		return 'GET'

	def getapiname(self):
		return 'dingtalk.oapi.sso.getuserinfo'

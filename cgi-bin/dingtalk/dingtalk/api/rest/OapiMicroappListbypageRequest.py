'''
Created by auto_sdk on 2019.07.01
'''
from dingtalk.api.base import RestApi
class OapiMicroappListbypageRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.agentId = None
		self.offset = None
		self.size = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.microapp.listbypage'

'''
Created by auto_sdk on 2018.07.25
'''
from dingtalk.api.base import RestApi
class OapiMicroappUpdateRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.agentId = None
		self.appDesc = None
		self.appIcon = None
		self.appName = None
		self.homepageUrl = None
		self.ompLink = None
		self.pcHomepageUrl = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.microapp.update'

'''
Created by auto_sdk on 2020.12.29
'''
from dingtalk.api.base import RestApi
class OapiSmartworkHrmRosterMetaGetRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.agentid = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.smartwork.hrm.roster.meta.get'

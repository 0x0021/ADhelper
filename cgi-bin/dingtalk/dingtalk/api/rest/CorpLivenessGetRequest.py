'''
Created by auto_sdk on 2019.07.03
'''
from dingtalk.api.base import RestApi
class CorpLivenessGetRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.corp.liveness.get'

'''
Created by auto_sdk on 2020.09.24
'''
from dingtalk.api.base import RestApi
class OapiImpaasConversationOpencidGetRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.model = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.impaas.conversation.opencid.get'

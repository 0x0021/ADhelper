'''
Created by auto_sdk on 2019.07.03
'''
from dingtalk.api.base import RestApi
class OapiImpaasConversaionChangegroupownerRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.channel = None
		self.chatid = None
		self.userid = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.impaas.conversaion.changegroupowner'

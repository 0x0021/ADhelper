'''
Created by auto_sdk on 2018.07.25
'''
from dingtalk.api.base import RestApi
class CorpChatbotListorgbotRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.agent_id = None
		self.type = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.corp.chatbot.listorgbot'

'''
Created by auto_sdk on 2019.07.01
'''
from dingtalk.api.base import RestApi
class OapiImChatbotDeleteRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.chatbot_user_id = None
		self.open_conversation_id = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.im.chatbot.delete'

'''
Created by auto_sdk on 2019.07.03
'''
from dingtalk.api.base import RestApi
class CorpMessageCorpconversationAsyncsendRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.agent_id = None
		self.dept_id_list = None
		self.msgcontent = None
		self.msgtype = None
		self.to_all_user = None
		self.userid_list = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.corp.message.corpconversation.asyncsend'

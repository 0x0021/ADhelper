'''
Created by auto_sdk on 2018.07.25
'''
from dingtalk.api.base import RestApi
class CorpExtcontactDeleteRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.userid = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.corp.extcontact.delete'

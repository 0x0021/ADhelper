'''
Created by auto_sdk on 2020.02.27
'''
from dingtalk.api.base import RestApi
class OapiExtcontactListRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.offset = None
		self.size = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.extcontact.list'

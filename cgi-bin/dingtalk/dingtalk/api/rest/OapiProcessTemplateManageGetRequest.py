'''
Created by auto_sdk on 2020.09.18
'''
from dingtalk.api.base import RestApi
class OapiProcessTemplateManageGetRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.userid = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.process.template.manage.get'

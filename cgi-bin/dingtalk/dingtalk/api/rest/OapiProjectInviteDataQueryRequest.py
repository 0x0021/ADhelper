'''
Created by auto_sdk on 2020.07.28
'''
from dingtalk.api.base import RestApi
class OapiProjectInviteDataQueryRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.invite_data_query = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.project.invite.data.query'

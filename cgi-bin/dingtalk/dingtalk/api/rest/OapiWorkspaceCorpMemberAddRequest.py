'''
Created by auto_sdk on 2020.03.15
'''
from dingtalk.api.base import RestApi
class OapiWorkspaceCorpMemberAddRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.member_add_dto_list = None
		self.target_corp_id = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.workspace.corp.member.add'

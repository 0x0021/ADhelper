'''
Created by auto_sdk on 2021.01.07
'''
from dingtalk.api.base import RestApi
class OapiWorkspaceProjectMemberRemoveRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.operator_staff_id = None
		self.project_source_id = None
		self.source = None
		self.staff_id = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.workspace.project.member.remove'

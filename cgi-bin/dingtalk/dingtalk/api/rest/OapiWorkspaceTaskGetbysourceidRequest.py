'''
Created by auto_sdk on 2020.12.23
'''
from dingtalk.api.base import RestApi
class OapiWorkspaceTaskGetbysourceidRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.agent_id = None
		self.source = None
		self.source_id = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.workspace.task.getbysourceid'

'''
Created by auto_sdk on 2020.01.03
'''
from dingtalk.api.base import RestApi
class OapiProcessinstanceFileDownloadRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.agent_id = None
		self.file_id = None
		self.process_instance_id = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.processinstance.file.download'

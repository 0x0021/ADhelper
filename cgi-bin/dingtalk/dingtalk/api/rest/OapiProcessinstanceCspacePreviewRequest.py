'''
Created by auto_sdk on 2020.02.05
'''
from dingtalk.api.base import RestApi
class OapiProcessinstanceCspacePreviewRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.request = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.processinstance.cspace.preview'

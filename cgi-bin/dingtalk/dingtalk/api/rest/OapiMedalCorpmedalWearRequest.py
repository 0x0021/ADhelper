'''
Created by auto_sdk on 2019.10.31
'''
from dingtalk.api.base import RestApi
class OapiMedalCorpmedalWearRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.operation = None
		self.template_id = None
		self.userid = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.medal.corpmedal.wear'

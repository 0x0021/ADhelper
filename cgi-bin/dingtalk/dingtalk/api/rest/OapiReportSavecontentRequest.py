'''
Created by auto_sdk on 2020.09.17
'''
from dingtalk.api.base import RestApi
class OapiReportSavecontentRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.create_report_param = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.report.savecontent'

'''
Created by auto_sdk on 2020.10.15
'''
from dingtalk.api.base import RestApi
class OapiEduSubjectGetRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.operator_userid = None
		self.period_code = None
		self.subject_code = None
		self.subject_name = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.edu.subject.get'

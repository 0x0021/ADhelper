'''
Created by auto_sdk on 2020.06.09
'''
from dingtalk.api.base import RestApi
class OapiEduGuardianGetRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.class_id = None
		self.guardian_userid = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.edu.guardian.get'

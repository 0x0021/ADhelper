'''
Created by auto_sdk on 2020.08.17
'''
from dingtalk.api.base import RestApi
class OapiHireNavigationGetRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.userid = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.hire.navigation.get'

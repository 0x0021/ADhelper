'''
Created by auto_sdk on 2021.01.12
'''
from dingtalk.api.base import RestApi
class OapiEduFamilyChildGetRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.child_userid = None
		self.op_userid = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.edu.family.child.get'

'''
Created by auto_sdk on 2020.07.09
'''
from dingtalk.api.base import RestApi
class OapiEduHomeworkUserRoleQueryRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.biz_code = None
		self.class_id = None
		self.userid = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.edu.homework.user.role.query'

'''
Created by auto_sdk on 2020.06.23
'''
from dingtalk.api.base import RestApi
class OapiEduUserRelationListRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.class_id = None
		self.page_no = None
		self.page_size = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.edu.user.relation.list'

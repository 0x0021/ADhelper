'''
Created by auto_sdk on 2019.08.05
'''
from dingtalk.api.base import RestApi
class OapiEnterpriseFamilydrListRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.corp_id = None
		self.order_by = None
		self.page_size = None
		self.page_start = None
		self.return_fields = None
		self.stat_date = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.enterprise.familydr.list'

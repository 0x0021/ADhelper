'''
Created by auto_sdk on 2019.10.31
'''
from dingtalk.api.base import RestApi
class OapiRetailSellerOrgCheckRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.userid = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.retail.seller.org.check'

'''
Created by auto_sdk on 2021.01.19
'''
from dingtalk.api.base import RestApi
class OapiCrmObjectdataCustomobjectUpdateRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.instance = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.crm.objectdata.customobject.update'

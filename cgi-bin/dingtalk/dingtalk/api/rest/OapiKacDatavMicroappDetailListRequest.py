'''
Created by auto_sdk on 2020.05.26
'''
from dingtalk.api.base import RestApi
class OapiKacDatavMicroappDetailListRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.request = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.kac.datav.microapp.detail.list'

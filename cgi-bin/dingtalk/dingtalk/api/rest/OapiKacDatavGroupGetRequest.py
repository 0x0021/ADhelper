'''
Created by auto_sdk on 2020.08.13
'''
from dingtalk.api.base import RestApi
class OapiKacDatavGroupGetRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.request = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.kac.datav.group.get'

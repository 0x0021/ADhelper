'''
Created by auto_sdk on 2020.07.01
'''
from dingtalk.api.base import RestApi
class OapiSmartdeviceAtmachineUserUpdateRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.param = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.smartdevice.atmachine.user.update'

'''
Created by auto_sdk on 2019.07.01
'''
from dingtalk.api.base import RestApi
class OapiSmartdeviceFacegroupMemberListRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.biz_id = None
		self.cursor = None
		self.size = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.smartdevice.facegroup.member.list'

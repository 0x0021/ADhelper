'''
Created by auto_sdk on 2021.01.13
'''
from dingtalk.api.base import RestApi
class OapiUnionCooperateJoinedListRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.status = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.union.cooperate.joined.list'

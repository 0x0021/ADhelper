'''
Created by auto_sdk on 2018.08.07
'''
from dingtalk.api.base import RestApi
class OapiAlitripBtripCostCenterEntityDeleteRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.rq = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.alitrip.btrip.cost.center.entity.delete'

'''
Created by auto_sdk on 2021.01.13
'''
from dingtalk.api.base import RestApi
class OapiDingpayRedenvelopeGetRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.corp_biz_no = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.dingpay.redenvelope.get'

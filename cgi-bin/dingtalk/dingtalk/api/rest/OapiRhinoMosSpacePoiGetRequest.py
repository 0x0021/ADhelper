'''
Created by auto_sdk on 2020.03.07
'''
from dingtalk.api.base import RestApi
class OapiRhinoMosSpacePoiGetRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.request = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.rhino.mos.space.poi.get'

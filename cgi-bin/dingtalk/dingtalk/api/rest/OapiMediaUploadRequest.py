'''
Created by auto_sdk on 2018.07.25
'''
from dingtalk.api.base import RestApi
class OapiMediaUploadRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.media = None
		self.type = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.media.upload'

	def getMultipartParas(self):
		return ['media']

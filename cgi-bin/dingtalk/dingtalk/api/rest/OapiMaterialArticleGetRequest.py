'''
Created by auto_sdk on 2019.06.28
'''
from dingtalk.api.base import RestApi
class OapiMaterialArticleGetRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.article_id = None
		self.unionid = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.material.article.get'

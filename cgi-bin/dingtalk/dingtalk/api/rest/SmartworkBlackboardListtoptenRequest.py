'''
Created by auto_sdk on 2019.07.03
'''
from dingtalk.api.base import RestApi
class SmartworkBlackboardListtoptenRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.userid = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.smartwork.blackboard.listtopten'

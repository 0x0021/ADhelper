'''
Created by auto_sdk on 2020.07.16
'''
from dingtalk.api.base import RestApi
class OapiCalendarV2EventCancelRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.agentid = None
		self.calendar_id = None
		self.event_id = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.calendar.v2.event.cancel'

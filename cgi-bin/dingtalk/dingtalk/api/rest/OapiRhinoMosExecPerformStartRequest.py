'''
Created by auto_sdk on 2020.07.03
'''
from dingtalk.api.base import RestApi
class OapiRhinoMosExecPerformStartRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.device_ids = None
		self.operation_perform_record_ids = None
		self.order_id = None
		self.tenant_id = None
		self.userid = None
		self.work_nos = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.rhino.mos.exec.perform.start'

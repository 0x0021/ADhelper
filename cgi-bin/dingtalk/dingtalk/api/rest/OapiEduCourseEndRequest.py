'''
Created by auto_sdk on 2020.08.04
'''
from dingtalk.api.base import RestApi
class OapiEduCourseEndRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.course_code = None
		self.op_user_id = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.edu.course.end'

'''
Created by auto_sdk on 2020.08.10
'''
from dingtalk.api.base import RestApi
class OapiEduCourseDeleteRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.course_code = None
		self.op_userid = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.edu.course.delete'

'''
Created by auto_sdk on 2020.04.29
'''
from dingtalk.api.base import RestApi
class OapiEduHomeworkStudentCommentDeleteRequest(RestApi):
	def __init__(self,url=None):
		RestApi.__init__(self,url)
		self.biz_code = None
		self.class_id = None
		self.comment_id = None
		self.hw_id = None
		self.student_id = None
		self.teacher_userid = None

	def getHttpMethod(self):
		return 'POST'

	def getapiname(self):
		return 'dingtalk.oapi.edu.homework.student.comment.delete'

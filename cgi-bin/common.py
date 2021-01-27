import sys
sys.path.append(".\\dingtalk")
import dingtalk.api
import winrm
import time

#应用凭证
agent_id=1068346698
appkey="dinga13xhv6expzbcj1a"
appsecret="jUtIY6nLUJEQp5259ksVohlluko9TcXdGgDCcTFffgcN97Ra03K0LSAb3hryO3Ru"
#审批流代码
process_code="PROC-8BE46E7C-745A-44B5-9465-F9C9A7401724"
#默认操作为解锁


#获取access token
def gettoken(appkey,appsecret):
    req=dingtalk.api.OapiGettokenRequest("https://oapi.dingtalk.com/gettoken")
    req.appkey= appkey
    req.appsecret= appsecret
    try:
        access_token= req.getResponse()['access_token']
        return access_token
    except Exception as e:
        print(e)
        print("false")
        
#获取用户id
def getuserid(permissioncode,access_token):
    req=dingtalk.api.OapiUserGetuserinfoRequest("https://oapi.dingtalk.com/user/getuserinfo")
    req.code=permissioncode
    try:
        user_id= req.getResponse(access_token)["userid"]
        return user_id
    except Exception as e:
        print(e)
        print("false")
        
#获取部门id以及邮箱
def getuserinfo(user_id,access_token):
    req=dingtalk.api.OapiV2UserGetRequest("https://oapi.dingtalk.com/topapi/v2/user/get")
    req.userid=user_id
    try:
        dept_id=req.getResponse(access_token)["result"]["dept_id_list"][0]
        #员工可能同时属于多个部门,但只能取其中一个id
        email = req.getResponse(access_token)["result"]["email"]
        return {'dept_id':dept_id,'email':email }
    except Exception as e:
        print(e)
        print("false")
        
#生成审批流
def process_create(agent_id,process_code,user_id,dept_id,access_token,flag):
    req=dingtalk.api.OapiProcessinstanceCreateRequest("https://oapi.dingtalk.com/topapi/processinstance/create")
    req.agent_id=agent_id
    req.process_code=process_code
    req.originator_user_id=user_id
    req.dept_id=dept_id
    #根据操作类型构建审批内容,默认为解锁
    if (flag == 'resetpassowrd'):
        req.form_component_values=[
                {
                "name":"请选择需要的业务",
                "value":"重置密码"
            },
                {
                "name":"重置密码",
                "value":"mkgz18//"
            }
        ]
    else :
        req.form_component_values={
                "name":"请选择需要的业务",
                "value":"解锁账号"
	         }
    try:
        instanceid= req.getResponse(access_token)["process_instance_id"]
        #return(instanceid)
    except Exception as e:
        print(e)
        print("false")
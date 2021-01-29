# coding=utf-8
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
        print('get access_token error:',e)
        print("false")
        
#获取用户id
def getuserid(permissioncode,access_token):
    req=dingtalk.api.OapiUserGetuserinfoRequest("https://oapi.dingtalk.com/user/getuserinfo")
    req.code=permissioncode
    try:
        user_id= req.getResponse(access_token)["userid"]
        return user_id
    except Exception as e:
        print('get userid error:',e)
        print("false")
        
#获取员工信息
def getuserinfo(user_id,access_token):
    req=dingtalk.api.OapiV2UserGetRequest("https://oapi.dingtalk.com/topapi/v2/user/get")
    req.userid=user_id
    try:
        #员工可能同时属于多个部门,但只能取其中一个id
        dept_id=req.getResponse(access_token)["result"]["dept_id_list"][0]
        #禁止员工自行更改的情况下可用邮箱来获取账号
        #email = req.getResponse(access_token)["result"]["email"].split('@')[0]
        #获取账号信息,如果用户没有填写扩展字段,则扩展字段值返回"{}"
        if (req.getResponse(access_token)["result"]["extension"] == "{}" ):
          ad_account = ''
          return { 'dept_id':dept_id, 'ad_account':ad_account }
        else :
          ad_account = req.getResponse(access_token)["result"]["extension"].split('"')[3]
          return { 'dept_id':dept_id, 'ad_account':ad_account }
    except Exception as e:
        print('get userinfo error:',e)
        print("false")
        
#生成审批流
def process_create(process_code,user_id,dept_id,access_token,flag,ad_account):
    req=dingtalk.api.OapiProcessinstanceCreateRequest("https://oapi.dingtalk.com/topapi/processinstance/create")
    #req.agent_id=agent_id
    req.process_code=process_code
    req.originator_user_id=user_id
    req.dept_id=dept_id
    #根据操作类型构建审批内容,默认为解锁
    if (flag == 'resetpassowrd'):
        req.form_component_values=[
            {
                "name":"所需业务",
                "value":"重置密码"
            },
            {
                "name":"AD账号",
                "value":ad_account
            }
        ]
    else :
        req.form_component_values=[
            {
                "name":"所需业务",
                "value":"解锁账号"
	        },
            {
                "name":"AD账号",
                "value":ad_account
            }
        ]
    try:
        instanceid= req.getResponse(access_token)["process_instance_id"]
        #return(instanceid)
    except Exception as e:
        print('create process error:',e)
        print("false")
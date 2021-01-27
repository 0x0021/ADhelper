from common import *

#免登码,通过前端获取
permissioncode=sys.argv[1]
        
#主函数
if __name__ == "__main__":

    #构建用户相关信息
    access_token = gettoken(appkey,appsecret)
    user_id = getuserid(permissioncode,access_token)
    dept_id = getuserinfo(user_id,access_token)['dept_id']
    account = getuserinfo(user_id,access_token)['email'].split('@')[0]
    password = 'mkgz18//'
    #account = 'raimouse.che'
    #password = sys.argv[2]
    
    #操作类型标志
    flag = 'resetpassowrd'
    
    #生成powershell命令
    cmd =" Set-ADAccountPassword -Reset {0} -NewPassword (ConvertTo-SecureString -AsPlainText '{1}' -Force)".format(account,password)
    changetime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

    #连接AD并执行命令
    try:
        s = winrm.Session('10.61.0.102',auth=('Administrator','mkgz18//'))
        r = s.run_ps(cmd)
        if ( r.status_code == 0 ) :
        #生成日志以及审批流
            log = '"{0} {1} 更改密码成功" | Out-File -Append C:\\it\\ADPasschangelog.txt'.format(changetime,account)
            s.run_ps(log)
            process_create(agent_id,process_code,user_id,dept_id,access_token,flag)
            #输出用户信息
            #print(user_id)
            #print(dept_id)
            #print('true')
        else :
        #只生成日志
            result=r.std_err.decode().splitlines()[0]
            log = '"{0} {1} 更改密码失败,{2}" | Out-File -Append C:\\it\\ADPasschangelog.txt'.format(changetime,account,result)
            s.run_ps(log)
            #输出错误信息
            #print(user_id)
            #print(dept_id)
            #print('账号:',account)
            print(result)
            #用false来区分php调用python脚本成功但脚本调用powershell执行失败的情况
            print("false")
    except Exception as e:
        print(e)
        print("false")


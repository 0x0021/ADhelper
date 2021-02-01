# coding=utf-8
from common import *

#免登码,通过前端获取
permissioncode=sys.argv[1]
     
#主函数
if __name__ == "__main__":

    #获取相关信息
    if (permissioncode == 'login'):
        #print(permissioncode)
        access_token = gettoken(appkey,appsecret)
        user_id = sys.argv[2]
        dept_id = sys.argv[3]
        account = sys.argv[4]
    else :
        access_token = gettoken(appkey,appsecret)
        user_id = getuserid(permissioncode,access_token)
        dept_id = getuserinfo(user_id,access_token)['dept_id']
        account = getuserinfo(user_id,access_token)['ad_account']
    
    if (account != ''):
        #操作类型标志
        flag = 'unlock'
        
        #构建powershell命令
        cmd = ' Unlock-ADAccount {0} '.format(account)
        unlocktime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
        
        #解锁账号
        try:
            s = winrm.Session('10.61.0.102',auth=('Administrator','mkgz18//'))

            r = s.run_ps(cmd)
            if ( r.status_code == 0 ):
                 log = '"{0} {1} 账号解锁成功" | Out-File -Append C:\\it\\ADunlocklog.txt'.format(unlocktime,account)
                 s.run_ps(log)
                 process_create(process_code,user_id,dept_id,access_token,flag,account)
                 print(user_id)
                 print(dept_id)
                 print(account)
            else :
                 result=r.std_err.decode().splitlines()[0]
                 log = '"{0} 账号解锁失败,{1}" | Out-File -Append C:\\it\\ADunlocklog.txt'.format(unlocktime,result)
                 s.run_ps(log)
                 print(result)
                 print("false")

        except Exception as e:
                print(e)
                print("false")
    else :
        print("empty ADAccount info")
        print("false")
# -*- coding: utf-8  -*-
import os
import time
import random
'广告文件列表'
adlist=[]
'腾讯'
Tencent='C:\\Users\\asd\\AppData\\Roaming\\Tencent\\'
adlist.append(Tencent+"QQMicroGameBox\\Launch.exe")
adlist.append(Tencent+'QQMicroGameBox\\1.1.4.5\\QQMGameBoxUpdater.exe')
adlist.append(Tencent+"QQMicroGameBox\\1.1.4.5\\QQMicroGameBox.exe")
adlist.append(Tencent+"QQMicroGameBox\\1.1.4.5\\QQMicroGameBoxTray.exe")
adlist.append(Tencent+'QQMicroGameBox\\1.1.4.5\\Toolkit.exe')
adlist.append(Tencent+'QQMicroGameBox\\1.1.4.5\\WebBrowserProcess.exe')
adlist.append(Tencent+'QQMicroGameBox\\1.1.4.5\\WebServer.exe')


adlist.append(Tencent+'QQMicroGameBox\\1.1.4.5\\Toolkit.exe')
adlist.append(Tencent+'QQMicroGameBox\\1.1.4.5\\Toolkit.exe')
adlist.append(Tencent+'QQMicroGameBox\\1.1.4.5\\Toolkit.exe')


















t= time.localtime(time.time())
时间标签="_"+str(t[0])+'年'+str(t[1])+'月'+str(t[2])+'日'+str(t[3])+'时'+str(t[4])+'分'+str(t[5])+'秒'#+random.randint(0,9)


print('总共有',len(adlist),'个exe文件')

for ad in adlist:
    if os.path.exists(ad):
        try: 
            os.rename(ad, ad[:len(ad)-4]+时间标签)
            print (ad+ "  已重命名为："+ ad[:len(ad)-4]+时间标签)
        except:
            print (ad[:len(ad)-4]+时间标签+'已存在，未重新创建')
        #os.fdopen(ad)
        try:
            exe=open(ad,'a')
        except:
            print('创建新文件出错！！！')
            print('新文件'+ad +'未创建')
        exe.close
        print ("空文件"+ ad+'已创建')
    else:
        print (ad+"不存在")


print("")
print ('广告文件修改完毕')
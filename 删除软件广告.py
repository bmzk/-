# -*- coding: utf-8  -*-
import os
import time

adlist=[]
adlist.append("C:\\Users\\asd\\AppData\\Roaming\\Tencent\\QQMicroGameBox\\1.1.4.5\\QQMicroGameBoxTray.exe")
adlist.append("C:\\Users\\asd\\AppData\\Roaming\\Tencent\\QQMicroGameBox\\Launch.exe")
adlist.append("C:\\Users\\asd\\AppData\\Roaming\\Tencent\\QQMicroGameBox\\1.1.4.5\\QQMicroGameBox.exe")

t= time.localtime(time.time())
文件拓展名=str(t[0])+'年'+str(t[1])+'月'+str(t[2])+'日'+str(t[3])+'时'+str(t[4])+'分'+str(t[5])+'秒'



print('总共有',adlist.count(adlist),'个文件夹')

for ad in adlist:
    if os.path.exists(ad):
        os.rename(ad, ad+文件拓展名)
        print (ad+ "  已重命名为："+ ad+文件拓展名)
        os.fdopen(ad)
        print ("空文件"+ ad+'已创建')
    else:
        print (ad+"不存在")



print ('广告文件修改完毕')
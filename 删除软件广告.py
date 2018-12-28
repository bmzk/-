# -*- coding: utf-8  -*-
import os
import random
import time

#q
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


Tencent2='C:\\Program Files (x86)\\Tencent\\QQMicroGameBoxService\\1.0.5.2\\'
adlist.append(Tencent2+'plugin.exe')
adlist.append(Tencent2+'QQMGBWebserver.exe')
adlist.append(Tencent2+'QQMicroGameBoxService.exe')
adlist.append(Tencent2+'QQMicroGameBoxServiceUpdate.exe')
adlist.append(Tencent2+'QQMicroGameBoxServiceUpdate.exe')

adlist.append(Tencent+'QQMicroGameBox\\1.1.4.5\\Toolkit.exe')
adlist.append(Tencent+'QQMicroGameBox\\1.1.4.5\\Toolkit.exe')
adlist.append(Tencent+'QQMicroGameBox\\1.1.4.5\\Toolkit.exe')
adlist.append(Tencent+'QQMicroGameBox\\1.1.4.5\\Toolkit.exe')
adlist.append(Tencent+'QQMicroGameBox\\1.1.4.5\\Toolkit.exe')
adlist.append(Tencent+'QQMicroGameBox\\1.1.4.5\\Toolkit.exe')
adlist.append(Tencent+'QQMicroGameBox\\1.1.4.5\\Toolkit.exe')
adlist.append(Tencent+'QQMicroGameBox\\1.1.4.5\\Toolkit.exe')
adlist.append(Tencent+'QQMicroGameBox\\1.1.4.5\\Toolkit.exe')

errorlist=[]
def delete(adList:list):
    n=len(adList)
    for i in adList:
        print("要删除文件：",i)
    for i in adList:
        if os.path.exists(i):
            renameFile(i)
    print('---'*9)
    checkResult(adList)
    for i in errorlist:
        print('删除过程中出现错误:',i)

def renameFile(file):
    '''对文件进行重命名'''
    fileId=0
    t_current=time.time()
    while os.path.exists(file[:-4]+getTime(t_current,0,1)+'-'+str(fileId)):
        fileId+=1
    try:
        os.rename(file, file[:-4]+getTime(t_current,0,1)+'-'+str(fileId))
    except PermissionError:
        print('文件被占用:',file)
        errorlist.append(file)
    except:
        print('删除文件出现错误:',file)
    print(getTime(),'已执行删除文件:',file)    
def getTime(t_current=0.0,n=5,mode=0):      
    t=time.localtime(t_current)
    ms=int((t_current-int(t_current))*1000)
    if mode==0:
        returnValue=time.strftime('%Y/%m/%d %H:%M:%S',t)+'::'+str(ms)+' '*n
    elif mode==1:
        returnValue=time.strftime('%Y/%m/%d',t)+' '*n
    elif mode==2:
        returnValue=time.strftime('%H:%M:%S',t)+' '*n
    elif mode==3:
        returnValue=time.strftime('%H:%M:%S',t)+'::'+str(ms)+' '*n
    elif mode==4:
        returnValue=time.strftime('%Y/%m/%d %H:%M:%S',t)+'::'+str(ms)+' '*n
    elif mode==5:
        returnValue=time.strftime('%Y%m%d%H%M%S',t)+' '*n
    elif mode==6:
        returnValue=time.strftime('%Y/%m/%d %H:%M:%S',t)+'::'+str(ms)+' '*n
    else:
        returnValue=time.strftime('%Y/%m/%d %H:%M:%S',t)+'::'+str(ms)+' '*n
    return returnValue
def checkResult(adList):
    deleted=[]
    noDeleted=[]
    for ad in adList:
        if os.path.exists(ad):
            noDeleted.append(ad)
        else:
            deleted.append(ad)
    print('---'*9)
    print('总共',len(adList),'个文件.')  
    print('---'*9)
    print(len(deleted),'个文件已经删除.')
    for i in deleted:
        print('成功删除: ',i)
    print('---'*9)
    print(len(noDeleted),'个文件未能够删除.')
    for i in noDeleted:
        print('未删除: ',i)
    pass  



delete(adlist)

input("按任意键结束")

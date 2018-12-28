# -*- coding: utf-8  -*-
import os
import random
import time

#q
'广告文件列表'
adlist={''}
'腾讯'
adlist.add
Tencent='C:\\Users\\asd\\AppData\\Roaming\\Tencent\\'
adlist.add(Tencent+"QQMicroGameBox\\Launch.exe")
adlist.add(Tencent+'QQMicroGameBox\\1.1.4.5\\QQMGameBoxUpdater.exe')
adlist.add(Tencent+"QQMicroGameBox\\1.1.4.5\\QQMicroGameBox.exe")
adlist.add(Tencent+"QQMicroGameBox\\1.1.4.5\\QQMicroGameBoxTray.exe")
adlist.add(Tencent+'QQMicroGameBox\\1.1.4.5\\Toolkit.exe')
adlist.add(Tencent+'QQMicroGameBox\\1.1.4.5\\WebBrowserProcess.exe')
adlist.add(Tencent+'QQMicroGameBox\\1.1.4.5\\WebServer.exe')


Tencent2='C:\\Program Files (x86)\\Tencent\\QQMicroGameBoxService\\1.0.5.2\\'
adlist.add(Tencent2+'plugin.exe')
adlist.add(Tencent2+'QQMGBWebserver.exe')
adlist.add(Tencent2+'QQMicroGameBoxService.exe')
adlist.add(Tencent2+'QQMicroGameBoxServiceUpdate.exe')
adlist.add(Tencent2+'QQMicroGameBoxServiceUpdate.exe')
'wps'
wps='C:\\Program Files (x86)\\WPS Office\\'
adlist.add(wps+'10.1.0.6747\\wtoolex\\desktoptip.exe')
adlist.add(wps+'10.1.0.6747\\wtoolex\\wpsnotify.exe')
adlist.add(wps+'10.1.0.6747\\wtoolex\\wpsupdate.exe')
adlist.add(wps+'10.1.0.6747\\wtoolex\\updateself.exe')
adlist.add(wps+'QQMicroGameBox\\1.1.4.5\\Toolkit.exe')
adlist.add(wps+'QQMicroGameBox\\1.1.4.5\\Toolkit.exe')
adlist.add(wps+'QQMicroGameBox\\1.1.4.5\\Toolkit.exe')
adlist.add(wps+'QQMicroGameBox\\1.1.4.5\\Toolkit.exe')
adlist.add(wps+'QQMicroGameBox\\1.1.4.5\\Toolkit.exe')
adlist.add(wps+'QQMicroGameBox\\1.1.4.5\\Toolkit.exe')
adlist.add(wps+'QQMicroGameBox\\1.1.4.5\\Toolkit.exe')
adlist.add(wps+'QQMicroGameBox\\1.1.4.5\\Toolkit.exe')

errorlist=[]
noFind=[]
existAd=[]
def delete(adList:list):
    for i in adList:
        print("要删除文件：",i)
    fgx()
    for i in adList:
        if os.path.exists(i):
            existAd.append(i)
            renameFile(i)
        else:
            print(getTime(time.time()),'文件未找到:',i)
            noFind.append(i)
    fgx()
    checkResult(existAd)
    fgx()




def renameFile(file):
    '''对文件进行重命名'''
    fileId=0
    t_current=time.time()
    while os.path.exists(file[:-4]+getTime(t_current,0,1)+'-'+str(fileId)):
        fileId+=1
    try:
        os.rename(file, file[:-4]+getTime(t_current,0,1)+'-'+str(fileId))
        print(getTime(time.time()),'已删除:',file)
    except PermissionError:
        print(getTime(time.time()),'文件被占用或权限不足:',file)
        errorlist.append(file)
    except:
        print(getTime(time.time()),'删除文件出现错误:',file)
    
      
def getTime(t_current=0.0,mode=3,n=3):      
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
    fgx()
    fgx()
    print('要删除',len(adList)+len(noFind),'个文件,其中',len(deleted),'个文件已经删除.',len(noFind),'个文件未找到,',len(errorlist),'个文件被占用或权限不足.')
    fgx()
    print(getTime(time.time()),'已经删除文件:')
    for i in deleted:
        print('成功删除: ',i)
    fgx()
    print(getTime(time.time()),'未找到文件:')
    for i in noFind:
        print('未找到: ',i)
    fgx()
    print(getTime(time.time()),'未能删除文件:')
    for i in noDeleted:
        print('未删除: ',i)


def fgx(n=22,tips=""):
    print(tips,'--'*22)

delete(adlist)

input("按任意键结束")

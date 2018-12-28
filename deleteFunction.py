import time
import os
def delete(adList:list):
    n=len(adList)
    for i in range(n):
        print("要删除文件：",adList(i))
    fileIsExit=isExist(adList)
    for i in range(n):
        if fileIsExit[i]==true:
            renameFile(adList[i])
    checkResult(adList)

def isExist(adList:list,mystr :str):
    '''检查列表中的文件是否存在,存在为True,返回False'''
    returnValue=[]
    for ad in adlist:
        returnValue.append("值:" :os.path.exist(ad),'描述':mystr)
    return returnValue
def renameFile(file):
    '''对文件进行重命名'''
    fileId=0
    t_current=time.time()
    while os.path.exist(file[:-4]+getTime(t_current,0,1)+'-'+str(fileId))==True
        fileId+=1
    os.rename(file, file[:-4]+getTime(t_current,0,1)+'-'+str(fileId))
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

def checkResult(adlist):
    deleted=[]
    noDeleted=[]
    for ad in adlist:
        if os.path.exist(ad):
            noDeleted.append(ad)
        else:
            deleted.append(ad)
    print('---'*9)
    print('总共',len(adlist),'个文件.')  
    print('---'*9)
    print(len(deleted),'个文件已经删除.')
    for i in deleted:
        print('成功删除: ',i)
    print('---'*9)
    print(len(noDeleted),'个文件未能够删除.')
    for i in noDeleted:
        print('未删除: ',i)
    pass  


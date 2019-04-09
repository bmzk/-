# -*- coding: utf-8  -*-
import os
import random
import time
'''腾讯'''
Tencent='C:\\Users\\asd\\AppData\\Roaming\\Tencent\\'
Tencent2='C:\\Program Files (x86)\\Tencent\\QQMicroGameBoxService\\1.0.5.2\\'
#'''广告文件列表,集合是一个无序的不重复元素序列,可以避免面使用列表时出现重复元素'''
adlist={
Tencent+"QQMicroGameBox\\Launch.exe",
# Tencent+'QQMicroGameBox\\1.1.4.5\\QQMGameBoxUpdater.exe',
# Tencent+"QQMicroGameBox\\1.1.4.5\\QQMicroGameBox.exe",
# Tencent+"QQMicroGameBox\\1.1.4.5\\QQMicroGameBoxTray.exe",
# Tencent+'QQMicroGameBox\\1.1.4.5\\Toolkit.exe',
# Tencent+'QQMicroGameBox\\1.1.4.5\\WebBrowserProcess.exe',
# Tencent+'QQMicroGameBox\\1.1.4.5\\WebServer.exe'
}

# adlist.add(Tencent2+'plugin.exe')
# adlist.add(Tencent2+'QQMGBWebserver.exe')
# adlist.add(Tencent2+'QQMicroGameBoxService.exe')
# adlist.add(Tencent2+'QQMicroGameBoxServiceUpdate.exe')
# adlist.add(Tencent2+'QQMicroGameBoxServiceUpdate.exe')
# 'wps'
# wps='C:\\Program Files (x86)\\WPS Office\\'
# adlist.add(wps+'10.1.0.6747\\wtoolex\\desktoptip.exe')
# adlist.add(wps+'10.1.0.6747\\wtoolex\\wpsnotify.exe')
# adlist.add(wps+'10.1.0.6747\\wtoolex\\wpsupdate.exe')
# adlist.add(wps+'10.1.0.6747\\wtoolex\\updateself.exe')
# adlist.add(wps+'QQMicroGameBox\\1.1.4.5\\Toolkit.exe')
# adlist.add(wps+'QQMicroGameBox\\1.1.4.5\\Toolkit.exe')
# adlist.add(wps+'QQMicroGameBox\\1.1.4.5\\Toolkit.exe')
# adlist.add(wps+'QQMicroGameBox\\1.1.4.5\\Toolkit.exe')
# adlist.add(wps+'QQMicroGameBox\\1.1.4.5\\Toolkit.exe')
# adlist.add(wps+'QQMicroGameBox\\1.1.4.5\\Toolkit.exe')
adlist.add('C:\\Users\\asd\\Desktop\\asd.txt')
adlist.add('C:\\Users\\asd\\Desktop\\学院ppt制作模版2.JPG')


noFindFile=[]
existAd=[]
canNotDeleteFile=[]
errorlist=[]
successDeleteFile=[]
unsuccessDeleteFile=[]
def delete(adList:list):
    '''sub_删除广告程序,无返回值 \n
    调用函数 fgx()'''
    for i in adList:#显示要删除的文件
        #print("要删除文件：",i)
        pass
    fgx()
    for i in adList:
        if os.path.exists(i):
            existAd.append(i)
            renameFile(i)
            #print(i)
        else:
            print(getTime(time.time()),'文件未找到:',i)
            noFindFile.append(i)
    fgx()
    checkResult()
    fgx()

def renameFile(file):
    '''对文件进行重命名'''
    t_current=time.time()
    t_current=20190409
    try:
        a=file
        b=file[:-4]+getTime(t_current)+'.txt'
        #print('00000000000000000000000000',a,b)
        print('successDeleteFile',successDeleteFile)
        print( os.path.basename(file))
        os.rename(a, b)
        #os.rename(file, file[:-4]+getTime(t_current))
        successDeleteFile.append(file)
        
    # except PermissionError:
    #     print(getTime(time.time()),'文件被占用或权限不足:',file)
    #     canNotDeleteFile.append(file)
    # except IOError:
    #     print('IOError', file)
    #     if os.path.exists(file):
    #         print('IOError000000000000000000000000000000')
    #     errorlist.append(file)
    except:
        print(getTime(time.time()),'删除文件出现错误:',file)
        errorlist.append(file)

def getTime(t=0.0):      
    '''获得14个数字表示的时间字符串,如2019040911203'''
    return time.strftime('%Y%m%d%H%M%S',time.localtime(t))
def checkResult():
    for ad in successDeleteFile:
        if os.path.exists(ad):
            unsuccessDeleteFile.append(ad)
            successDeleteFile.remove(ad)
        else:
            newfile = open(ad,'a+' )
            newfile.write('012345698761416raegfgg')
            newfile.close
    fgx()
    print('  要删除文件: ',len(adlist))
    print('实际存在文件: ',len(existAd))
    print('  不存在文件: ',len(noFindFile))
    fgx()
    print('成功删除: ',len(successDeleteFile))
    print('未 删 除: ',len(unsuccessDeleteFile))
    print('出现错误:',len(errorlist))
    fgx()
    for i in noFindFile:
        print('未 找 到: ',i)
    fgx()
    for i in successDeleteFile:
        print('成功删除: ',i)
    fgx()
    for i in unsuccessDeleteFile:
        print('未 删 除: ',i)
    fgx()
    for i in errorlist:
        print('出现错误: ',i)

def fgx(n=22,tips=""):
    '''分割线,为使输出更美观,输出一行 - 符号\n'''
    print(tips,'--'*22)

delete(adlist)

input("按任意键结束")

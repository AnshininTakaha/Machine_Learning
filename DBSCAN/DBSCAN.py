
# coding=gbk

#导入对应的numpy包和sklearn工程包
import numpy as np
# from sklearn.cluster import DBSCAN
import sklearn.cluster as skc
from sklearn import metrics
import matplotlib.pyplot as plt


def LoadData(filepath):
    fileObj = open(filepath,'r+')
    Allsample = fileObj.readlines()

    mac2id = {}
    onlinetimes = []

    for sample in Allsample:
        namewithdata = sample.strip().split(",")            #去掉空格，以逗号为分隔符转换成为list
        
        mac = namewithdata[2]
        onlinetime = int(namewithdata[6])
        starttime = namewithdata[5][12:13]                    #截取需要使用的信息

        if mac not in mac2id:
            mac2id[mac] = len(onlinetimes)                  #利用dict做对应上网时间在list的位置的索引
            onlinetimes.append((starttime,onlinetime))      #就就是 mac2id[M1] = 0  那么onlinetimes[0]就是他对应的开始时间和持续时间
        else:                                               #以此类推mac2id[M2] = 1 对应onlinetimes[1]
            onlinetimes[mac2id[mac]]=[(starttime,onlinetime)]

    return mac2id,onlinetimes

maclist={}
Datalist=[]

maclist,Datalist = LoadData("D:\CoreStorge\PythonCore\DBSCAN\TestData.txt")
real_x = np.array(Datalist)                               #构造数组，并转为n行2列的数组
real_x.reshape((-1,2))  

#创建dbscan算法
Myx = real_x[:,0:1]                                #这里是numpy的一种写法，意思是取所有数据集的第0到第1-1列的数据
dbs = skc.DBSCAN(eps=0.01,min_samples=20).fit(Myx)    #创建DBSCAN算法，最小距离为0.01，最小需要的点为20                                                       #执行计算，此时labels_已经计算完成了
dbs_label = dbs.labels_
print(dbs_label)

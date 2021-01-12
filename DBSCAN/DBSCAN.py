
# coding=gbk

#�����Ӧ��numpy����sklearn���̰�
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
        namewithdata = sample.strip().split(",")            #ȥ���ո��Զ���Ϊ�ָ���ת����Ϊlist
        
        mac = namewithdata[2]
        onlinetime = int(namewithdata[6])
        starttime = namewithdata[5][12:13]                    #��ȡ��Ҫʹ�õ���Ϣ

        if mac not in mac2id:
            mac2id[mac] = len(onlinetimes)                  #����dict����Ӧ����ʱ����list��λ�õ�����
            onlinetimes.append((starttime,onlinetime))      #�;��� mac2id[M1] = 0  ��ôonlinetimes[0]��������Ӧ�Ŀ�ʼʱ��ͳ���ʱ��
        else:                                               #�Դ�����mac2id[M2] = 1 ��Ӧonlinetimes[1]
            onlinetimes[mac2id[mac]]=[(starttime,onlinetime)]

    return mac2id,onlinetimes

maclist={}
Datalist=[]

maclist,Datalist = LoadData("D:\CoreStorge\PythonCore\DBSCAN\TestData.txt")
real_x = np.array(Datalist)                               #�������飬��תΪn��2�е�����
real_x.reshape((-1,2))  

#����dbscan�㷨
Myx = real_x[:,0:1]                                #������numpy��һ��д������˼��ȡ�������ݼ��ĵ�0����1-1�е�����
dbs = skc.DBSCAN(eps=0.01,min_samples=20).fit(Myx)    #����DBSCAN�㷨����С����Ϊ0.01����С��Ҫ�ĵ�Ϊ20                                                       #ִ�м��㣬��ʱlabels_�Ѿ����������
dbs_label = dbs.labels_
print(dbs_label)

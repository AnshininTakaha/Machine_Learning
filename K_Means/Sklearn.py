
# coding=gbk
#�����Ӧ��numpy����sklearn���̰�
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


#��ȡ��Ϣ�����ض�Ӧ�ĳ������ֺͳ������ݵ�list
#����ֵ����Ҫ��ȡ���ļ���·��
#����ֵ����������list�ͳ�������list
def LoadData(filepath):
    fileObj = open(filepath,'r+')                   #�򿪶�Ӧ��filepath���ֵ��ļ���ģʽ�����ڶ�дģʽ���ļ�ָ����ڿ�ͷ
    Allsample = fileObj.readlines()                 #��ȡ�������ݣ�ת����Ϊlist
    
    store_cityname =[]                              #���ڴ���������ֺͳ������ݵ�������list
    store_citydata =[]

    for sample in Allsample:
        namewithdata = sample.strip()               #list�����Ԫ��ȥ������Ŀո��\n����Ҫ��ȥ��\n
        namewithdata = namewithdata.split(',')      #��Ϊ�б��Զ���Ϊ�ָ�Ԫ��
        store_cityname.append(namewithdata[0])      #�����б�ĵ�һ��Ԫ�أ�Ҳ���ǳ��е����ּ����ȥ��Ӧ��list����ȥ
        store_citydata.append(namewithdata[1:])     #�����������ȫ�������뵽��Ӧ��list����ȥ

    # for i in range(len(namewithdata)):
    print(store_citydata)
    return store_cityname,store_citydata
        
                        
    
#��ȡ��Ӧ�ĳ������ֺ����ݵĶ�Ӧlist
cityname,citydata = LoadData('D:\CoreStorge\PythonCore\SKlearn\city.txt')

#����һ��KMeans�ľ����㷨
kmeans = KMeans(n_clusters=3)                       #����һ�����������ص�KM�㷨,0,1,2
city_label = kmeans.fit_predict(citydata)           #���ݳ��е����ݣ�����ص����������ͬʱԤ��label������ֵ��n*1��label����
                                                    #����ʵ����cluster_centers_�Ѿ�������ˣ�������n-clusters*n_features�ľ���
                                                    #��ʾ�������ĵ�����
expense = np.sum(kmeans.cluster_centers_,axis = 1)  #����ӵó�ƽ�����,Ҳ����ƽ������ˮƽ��
                                                    
CityCluster = [
    [], #0��
    [], #1��
    []  #2��
]

for i in range(len(cityname)):                      #ͨ���������label�ֺ��࣬���뵽CityCluster��Ӧ��list��
    CityCluster[city_label[i]].append(cityname[i])

for i in range(len(CityCluster)):
    print(f"Expenses:{expense[i]}",end = "\n")
    print(f"�������ĳ����У�{str(CityCluster[i])}",end = "\n")



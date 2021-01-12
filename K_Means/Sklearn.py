
# coding=gbk
#导入对应的numpy包和sklearn工程包
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


#读取信息及返回对应的城市名字和城市数据的list
#输入值：需要读取的文件的路径
#返回值：城市名字list和城市数据list
def LoadData(filepath):
    fileObj = open(filepath,'r+')                   #打开对应的filepath名字的文件，模式是用于读写模式，文件指针放在开头
    Allsample = fileObj.readlines()                 #读取所有数据，转换成为list
    
    store_cityname =[]                              #用于储存城市名字和城市数据的两个空list
    store_citydata =[]

    for sample in Allsample:
        namewithdata = sample.strip()               #list里面的元素去除多余的空格和\n，主要是去掉\n
        namewithdata = namewithdata.split(',')      #变为列表，以逗号为分割元素
        store_cityname.append(namewithdata[0])      #将新列表的第一个元素，也就是城市的名字加入进去对应的list里面去
        store_citydata.append(namewithdata[1:])     #将后面的数据全部都加入到对应的list里面去

    # for i in range(len(namewithdata)):
    print(store_citydata)
    return store_cityname,store_citydata
        
                        
    
#获取对应的城市名字和数据的对应list
cityname,citydata = LoadData('D:\CoreStorge\PythonCore\SKlearn\city.txt')

#创建一个KMeans的聚类算法
kmeans = KMeans(n_clusters=3)                       #创建一个生成三个簇的KM算法,0,1,2
city_label = kmeans.fit_predict(citydata)           #根据城市的数据，计算簇的质心在哪里，同时预测label，返回值是n*1的label矩阵
                                                    #这里实际上cluster_centers_已经被算过了，出来的n-clusters*n_features的矩阵
                                                    #表示聚类中心的坐标
expense = np.sum(kmeans.cluster_centers_,axis = 1)  #行相加得出平均输出,也就是平均消费水平，
                                                    
CityCluster = [
    [], #0簇
    [], #1簇
    []  #2簇
]

for i in range(len(cityname)):                      #通过算出来的label分好类，加入到CityCluster对应的list中
    CityCluster[city_label[i]].append(cityname[i])

for i in range(len(CityCluster)):
    print(f"Expenses:{expense[i]}",end = "\n")
    print(f"所包含的城市有：{str(CityCluster[i])}",end = "\n")



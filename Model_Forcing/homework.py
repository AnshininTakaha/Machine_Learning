
# coding=gbk
import numpy as np
from sklearn.neighbors import KNeighborsClassifier          #KNN分类器
from sklearn.tree import DecisionTreeClassifier             #决策树分类器
from sklearn.naive_bayes import GaussianNB                  #高斯牛逼
from sklearn.metrics import classification_report          

def LoadData(filepath,Mode):
    fileObj = open(filepath,'r+')                   #打开对应的filepath名字的文件，模式是用于读写模式，文件指针放在开头
    Allsample = fileObj.readlines()                 #读取所有数据，转换成为list
    
    if Mode == 1:
        store_data =[]                                  #用于数据的储存和最后label的储存，分别对应一个数组
        store_label =[]

        for sample in Allsample:
            data_and_label = sample.split()               #以空格为分割，变成list(默认值是空格)
            store_data.append(data_and_label[:54])        #前面的54个元素,data
            store_label.append(data_and_label[54:])       #最后的第55个元素,label

        return store_data,store_label
    else: #Mode == 0
        store_data_P =[]                                  #用于测试的数据

        for sample in Allsample:
            data_and_label_P = sample.split()               #以空格为分割，变成list(默认值是空格)
            store_data_P.append(data_and_label_P[:54])        #前面的54个数据
            
        return store_data_P

def Print_to_txt(listdata,file):
    f = open(file,'w+')
    for i in listdata:
        print(str(i),file=f)
    f.close()


if __name__ == "__main__":
    Data,Label = LoadData("D:\CoreStorge\PythonCore\大作业\data_train.txt",1)
    test = LoadData("D:\CoreStorge\PythonCore\大作业\data_test.txt",0)
    #复制到对应的位置，准备训练
    x_train = Data
    y_train = Label
    x_test = test

    #K近邻分类器，并在测试集上面预测
    print('Start training KNN')
    knn = KNeighborsClassifier().fit(x_train,y_train)
    print('Training done!')
    answer_knn = knn.predict(x_test[0:100])
    print('Done!')

    #DT决策树
    print('Start trainning DT')
    dt = DecisionTreeClassifier().fit(x_train,y_train)
    print('Training done!')
    answer_dt = dt.predict(x_test[0:100])
    print('Done!')

    #贝叶斯
    print('Start trainning Bayes')
    gnb = GaussianNB().fit(x_train,y_train)
    print('Trainning done!')
    answer_gnb = gnb.predict(x_test[0:100])
    print('Prediction done!')

    Print_to_txt(answer_knn,'D:\CoreStorge\PythonCore\大作业\model_1.txt')
    Print_to_txt(answer_dt,'D:\CoreStorge\PythonCore\大作业\model_2.txt')
    Print_to_txt(answer_gnb,'D:\CoreStorge\PythonCore\大作业\model_3.txt')
    print("All done!!")

    



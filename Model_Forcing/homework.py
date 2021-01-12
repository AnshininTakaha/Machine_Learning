
# coding=gbk
import numpy as np
from sklearn.neighbors import KNeighborsClassifier          #KNN������
from sklearn.tree import DecisionTreeClassifier             #������������
from sklearn.naive_bayes import GaussianNB                  #��˹ţ��
from sklearn.metrics import classification_report          

def LoadData(filepath,Mode):
    fileObj = open(filepath,'r+')                   #�򿪶�Ӧ��filepath���ֵ��ļ���ģʽ�����ڶ�дģʽ���ļ�ָ����ڿ�ͷ
    Allsample = fileObj.readlines()                 #��ȡ�������ݣ�ת����Ϊlist
    
    if Mode == 1:
        store_data =[]                                  #�������ݵĴ�������label�Ĵ��棬�ֱ��Ӧһ������
        store_label =[]

        for sample in Allsample:
            data_and_label = sample.split()               #�Կո�Ϊ�ָ���list(Ĭ��ֵ�ǿո�)
            store_data.append(data_and_label[:54])        #ǰ���54��Ԫ��,data
            store_label.append(data_and_label[54:])       #���ĵ�55��Ԫ��,label

        return store_data,store_label
    else: #Mode == 0
        store_data_P =[]                                  #���ڲ��Ե�����

        for sample in Allsample:
            data_and_label_P = sample.split()               #�Կո�Ϊ�ָ���list(Ĭ��ֵ�ǿո�)
            store_data_P.append(data_and_label_P[:54])        #ǰ���54������
            
        return store_data_P

def Print_to_txt(listdata,file):
    f = open(file,'w+')
    for i in listdata:
        print(str(i),file=f)
    f.close()


if __name__ == "__main__":
    Data,Label = LoadData("D:\CoreStorge\PythonCore\����ҵ\data_train.txt",1)
    test = LoadData("D:\CoreStorge\PythonCore\����ҵ\data_test.txt",0)
    #���Ƶ���Ӧ��λ�ã�׼��ѵ��
    x_train = Data
    y_train = Label
    x_test = test

    #K���ڷ����������ڲ��Լ�����Ԥ��
    print('Start training KNN')
    knn = KNeighborsClassifier().fit(x_train,y_train)
    print('Training done!')
    answer_knn = knn.predict(x_test[0:100])
    print('Done!')

    #DT������
    print('Start trainning DT')
    dt = DecisionTreeClassifier().fit(x_train,y_train)
    print('Training done!')
    answer_dt = dt.predict(x_test[0:100])
    print('Done!')

    #��Ҷ˹
    print('Start trainning Bayes')
    gnb = GaussianNB().fit(x_train,y_train)
    print('Trainning done!')
    answer_gnb = gnb.predict(x_test[0:100])
    print('Prediction done!')

    Print_to_txt(answer_knn,'D:\CoreStorge\PythonCore\����ҵ\model_1.txt')
    Print_to_txt(answer_dt,'D:\CoreStorge\PythonCore\����ҵ\model_2.txt')
    Print_to_txt(answer_gnb,'D:\CoreStorge\PythonCore\����ҵ\model_3.txt')
    print("All done!!")

    



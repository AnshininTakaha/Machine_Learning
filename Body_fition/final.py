
# coding=gbk
import pandas as pd
import numpy as np

from sklearn.impute import SimpleImputer               #Ԥ����ģ��
from sklearn.model_selection import train_test_split   #�Զ�����ѵ�����Ͳ��Լ�ģ��
from sklearn.metrics import classification_report      #Ԥ��������ģ��
from sklearn.neighbors import KNeighborsClassifier     #K���ڷ�����
from sklearn.tree import DecisionTreeClassifier        #������������
from sklearn.naive_bayes import GaussianNB             #Ҷ��˹����

def load_datasets(feature_paths,label_paths):
    feature = np.ndarray(shape=(0,41))                 #����һ��41��Ŀ���������data
    label = np.ndarray(shape=(0,1))                    #����һ��41��Ŀ���label
    for file in feature_paths:
        df = pd.read_table(file,delimiter=',',na_values='?',header=None)   #�ָ����Ϊ���ţ�ȱʧֵΪ�ʺţ��ļ�������ͷ��
        imp = SimpleImputer(missing_values=np.nan,strategy='mean')    #ʹ��Imputer������strategyΪ'mean',��ȱʧ���ݽ��в�ȫ
        imp.fit(df)
        df = imp.transform(df)
        feature = np.concatenate((feature,df))
    for file in label_paths:
        df = pd.read_table(file,header=None)
        label = np.concatenate((label,df))

    label = np.ravel(label)
    return feature,label

if __name__  == '__main__':
    #��������·��
    Onfeature_Paths = ['A/A.feature','B/B.feature','C/C.feature','D/D.feature','E/E.feature']
    OnlabelPaths = ['A/A.label','B/B.label','C/C.label','D/D.label','E/E.label']
    #��ǰ���4��������Ϊѵ��������
    x_train,y_train = load_datasets(Onfeature_Paths[:4],OnlabelPaths[:4])
    #�����һ��������Ϊ���Լ�����
    x_test,y_test = load_datasets(Onfeature_Paths[4:],OnlabelPaths[4:])
    #��������
    x_train,y_train,y_= train_test_split(x_train,y_train,test_size=None)

    #K���ڷ����������ڲ��Լ�����Ԥ��
    print('Start training KNN..')
    knn = KNeighborsClassifier().fit(x_train,y_train)
    print('Training done!')
    answer_knn = knn.predict(x_test)
    print('Done!')

    #DT������
    print('Start trainning DT')
    dt = DecisionTreeClassifier().fit(x_train,y_train)
    print('Training done!')
    answer_dt = dt.predict(x_test)
    print('Done!')

    #��Ҷ˹
    print('Start trainning Bayes')
    gnb = GaussianNB().fit(x_train,y_train)
    print('Trainning done!')
    answer_gnb = gnb.predict(x_test)
    print('Prediction done!')

    print('\n\nThe classification report for knn:')
    print(classification_report(y_test,answer_knn))
    print('\n\nThe classification report for DT:')
    print(classification_report(y_test,answer_dt))
    print('\n\nThe classification reprot for Bayes:')
    print(classification_report(y_test,answer_gnb))

    



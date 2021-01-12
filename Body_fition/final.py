
# coding=gbk
import pandas as pd
import numpy as np

from sklearn.impute import SimpleImputer               #预处理模块
from sklearn.model_selection import train_test_split   #自动生成训练集和测试集模块
from sklearn.metrics import classification_report      #预测结果评估模块
from sklearn.neighbors import KNeighborsClassifier     #K近邻分类器
from sklearn.tree import DecisionTreeClassifier        #决策树分类器
from sklearn.naive_bayes import GaussianNB             #叶贝斯函数

def load_datasets(feature_paths,label_paths):
    feature = np.ndarray(shape=(0,41))                 #创建一个41个目标的列向量data
    label = np.ndarray(shape=(0,1))                    #创建一个41个目标的label
    for file in feature_paths:
        df = pd.read_table(file,delimiter=',',na_values='?',header=None)   #分割符号为逗号，缺失值为问号，文件不包含头行
        imp = SimpleImputer(missing_values=np.nan,strategy='mean')    #使用Imputer函数，strategy为'mean',对缺失数据进行补全
        imp.fit(df)
        df = imp.transform(df)
        feature = np.concatenate((feature,df))
    for file in label_paths:
        df = pd.read_table(file,header=None)
        label = np.concatenate((label,df))

    label = np.ravel(label)
    return feature,label

if __name__  == '__main__':
    #设置数据路径
    Onfeature_Paths = ['A/A.feature','B/B.feature','C/C.feature','D/D.feature','E/E.feature']
    OnlabelPaths = ['A/A.label','B/B.label','C/C.label','D/D.label','E/E.label']
    #将前面的4个数据作为训练集读入
    x_train,y_train = load_datasets(Onfeature_Paths[:4],OnlabelPaths[:4])
    #将最后一个数据作为测试集读入
    x_test,y_test = load_datasets(Onfeature_Paths[4:],OnlabelPaths[4:])
    #打乱数据
    x_train,y_train,y_= train_test_split(x_train,y_train,test_size=None)

    #K近邻分类器，并在测试集上面预测
    print('Start training KNN..')
    knn = KNeighborsClassifier().fit(x_train,y_train)
    print('Training done!')
    answer_knn = knn.predict(x_test)
    print('Done!')

    #DT决策树
    print('Start trainning DT')
    dt = DecisionTreeClassifier().fit(x_train,y_train)
    print('Training done!')
    answer_dt = dt.predict(x_test)
    print('Done!')

    #贝叶斯
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

    




# coding=gbk
from sklearn.neighbors import KNeighborsClassifier

x_data =[
    [0],
    [1],
    [2],
    [3]
]

y_label =[0,0,1,1]

#设置分类器的大小,并进行计算（这一步等于数据训练），取3个近邻数
neigh = KNeighborsClassifier(n_neighbors=3).fit(x_data,y_label)

#对一个未知的标签进行分类，得出对应预测分类的label（）
print(neigh.predict([[2.1]]))


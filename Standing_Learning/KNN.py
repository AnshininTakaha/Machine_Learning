
# coding=gbk
from sklearn.neighbors import KNeighborsClassifier

x_data =[
    [0],
    [1],
    [2],
    [3]
]

y_label =[0,0,1,1]

#���÷������Ĵ�С,�����м��㣨��һ����������ѵ������ȡ3��������
neigh = KNeighborsClassifier(n_neighbors=3).fit(x_data,y_label)

#��һ��δ֪�ı�ǩ���з��࣬�ó���ӦԤ������label����
print(neigh.predict([[2.1]]))


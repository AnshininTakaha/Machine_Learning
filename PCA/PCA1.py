
# coding=gbk
import matplotlib.pyplot as plt  
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris

#��ȡ��Ӧ������
Datastore = load_iris()

#���浽��Ӧ��Datastore��λ��
iris_label = Datastore.target
iris_data = Datastore.data
# iris_label = iris_label[0:2]
# iris_data = iris_data[0:2]
#�����㷨�����ý�ά������ɷ���2
pca = PCA(n_components=2)
Reduced_data = pca.fit_transform(iris_data)
print(Reduced_data)

#�������������
Red_Reduce_y = []
Red_Reduce_x = []
Blue_Reduce_y = []
Blue_Reduce_x = []
Green_Reduce_y =[]
Green_Reduce_x = []

#��Ӧlabel�ʹ����������ݽ��д���
for i in range(len(Reduced_data)):
    if iris_label[i] == 0:
        Red_Reduce_x.append(Reduced_data[i][0])
        Red_Reduce_y.append(Reduced_data[i][1])
    if iris_label[i] == 1:
        Blue_Reduce_x.append(Reduced_data[i][0])
        Blue_Reduce_y.append(Reduced_data[i][1])
    else:
        Green_Reduce_x.append(Reduced_data[i][0])
        Green_Reduce_y.append(Reduced_data[i][1])
    
plt.scatter(Red_Reduce_x,Red_Reduce_y,c='r',marker='x')
plt.scatter(Blue_Reduce_x,Blue_Reduce_y,c='b',marker='D')
plt.scatter(Green_Reduce_x,Green_Reduce_y,c='g',marker='.')
plt.show()




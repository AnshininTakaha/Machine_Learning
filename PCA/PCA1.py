
# coding=gbk
import matplotlib.pyplot as plt  
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris

#获取对应的数据
Datastore = load_iris()

#储存到对应的Datastore的位置
iris_label = Datastore.target
iris_data = Datastore.data
# iris_label = iris_label[0:2]
# iris_data = iris_data[0:2]
#加载算法，设置降维后的主成分是2
pca = PCA(n_components=2)
Reduced_data = pca.fit_transform(iris_data)
print(Reduced_data)

#定义三种坐标点
Red_Reduce_y = []
Red_Reduce_x = []
Blue_Reduce_y = []
Blue_Reduce_x = []
Green_Reduce_y =[]
Green_Reduce_x = []

#对应label和处理过后的数据进行处理
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




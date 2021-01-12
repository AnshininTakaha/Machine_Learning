
# coding=gbk
import matplotlib.pyplot as plt
from sklearn import decomposition
from sklearn.datasets import fetch_olivetti_faces
from numpy.random import RandomState

#设置排列情况和特征数目
n_row,n_col = 2,3
n_components = n_row * n_col

#设置人脸数据图片的大小
image_shape = (64,64)

#加载数据并打乱数据
dataset = fetch_olivetti_faces(shuffle=True,random_state=RandomState(0))
face = dataset.data

def plot_gallery(title,images,n_col=n_col,n_row=n_row):
    plt.figure(figsize=(2.*n_col,2.26*n_row))             #创建图片，制定尺寸
    plt.suptitle(title,size=16)                           #设置标题
    for i,comp in enumerate(images):
        plt.subplot(n_row,n_col,i+1)                      #展开一个n_row行，n_cow列的网格，并将图画在第i+1个位置
                                                          #注意，enumerate的标识数据是从0开始的，所以要+1
        vmax = max(comp.max(),-comp.min())                #定义颜色数据覆盖的最大范围
        
        plt.imshow(comp.reshape(image_shape),             #对应图
                   cmap= plt.cm.gray,                     #使用灰度图
                   interpolation= 'nearest',              #对数值归一化，以灰度图显示
                   vmin= -vmax,
                   vmax= vmax)
        
        plt.xticks(())                                    #取消x坐标和y坐标的值
        plt.yticks(())

    plt.subplots_adjust(0.01,0.05,0.99,0.93,0.04,0.)



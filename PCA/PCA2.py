
# coding=gbk
import matplotlib.pyplot as plt
from sklearn import decomposition
from sklearn.datasets import fetch_olivetti_faces
from numpy.random import RandomState

#�������������������Ŀ
n_row,n_col = 2,3
n_components = n_row * n_col

#������������ͼƬ�Ĵ�С
image_shape = (64,64)

#�������ݲ���������
dataset = fetch_olivetti_faces(shuffle=True,random_state=RandomState(0))
face = dataset.data

def plot_gallery(title,images,n_col=n_col,n_row=n_row):
    plt.figure(figsize=(2.*n_col,2.26*n_row))             #����ͼƬ���ƶ��ߴ�
    plt.suptitle(title,size=16)                           #���ñ���
    for i,comp in enumerate(images):
        plt.subplot(n_row,n_col,i+1)                      #չ��һ��n_row�У�n_cow�е����񣬲���ͼ���ڵ�i+1��λ��
                                                          #ע�⣬enumerate�ı�ʶ�����Ǵ�0��ʼ�ģ�����Ҫ+1
        vmax = max(comp.max(),-comp.min())                #������ɫ���ݸ��ǵ����Χ
        
        plt.imshow(comp.reshape(image_shape),             #��Ӧͼ
                   cmap= plt.cm.gray,                     #ʹ�ûҶ�ͼ
                   interpolation= 'nearest',              #����ֵ��һ�����ԻҶ�ͼ��ʾ
                   vmin= -vmax,
                   vmax= vmax)
        
        plt.xticks(())                                    #ȡ��x�����y�����ֵ
        plt.yticks(())

    plt.subplots_adjust(0.01,0.05,0.99,0.93,0.04,0.)




# coding=gbk
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier             #������������
from sklearn.model_selection import cross_val_score         #������ֵ֤�ĺ���

#������������ʹ�û���ϵ����Ҳ����0��1
clf = DecisionTreeClassifier()

#���β�������ݸ�ֵ��iris
iris = load_iris()

#������飬ʹ�þ�������ģ�ͣ�ʹ���β����data��label����ģ�����������۱�׼Ϊ׼ȷ�ȣ�ѡ��10����Ϊ�жϱ�׼
#��ȻҲ����ʹ�ñ��ģ�ͽ����������ߣ�����Ϊʲô�������Ӿ��ߵĿ��Կ��ʼ�
accurate_sorce = cross_val_score(clf,iris.data,iris.target,cv=10)
# print(accurate_sorce)

#ʹ��iris�����ݽ���ѵ��,����10���������ṩ���ݽ���ģ��Ԥ��
clf.fit(iris.data[10:],iris.target[10:])

#ʣ�µ�ʮ�����ݽ���ģ��Ԥ��
prt = clf.predict(iris.data[:10])




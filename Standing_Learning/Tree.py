
# coding=gbk
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier             #决策树分类器
from sklearn.model_selection import cross_val_score         #交叉验证值的函数

#创建决策树，使用基尼系数，也就是0到1
clf = DecisionTreeClassifier()

#将鸢尾花的数据赋值给iris
iris = load_iris()

#交叉检验，使用决策树的模型，使用鸢尾花的data和label进行模型评估，评价标准为准确度，选择10株作为判断标准
#当然也可以使用别的模型进行评估决策，具体为什么是这样子决策的可以看笔记
accurate_sorce = cross_val_score(clf,iris.data,iris.target,cv=10)
# print(accurate_sorce)

#使用iris的数据进行训练,留下10个数据来提供数据进行模型预测
clf.fit(iris.data[10:],iris.target[10:])

#剩下的十个数据进行模型预测
prt = clf.predict(iris.data[:10])




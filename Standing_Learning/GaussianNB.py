
# coding=gbk
import numpy as np
from sklearn.naive_bayes import GaussianNB

x_data = np.array([
    [-1,-1],
    [-2,-1],
    [-3,-2],
    [1,1],
    [2,1],
    [3,2]
])

y_label = np.array([1,1,1,2,2,2])


#������Ҷ˹����
clf = GaussianNB(priors= None)
clf.fit(x_data,y_label)


print(clf.predict([[-0.8,-1]]))

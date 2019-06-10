# _*_ coding:utf-8 _*_
"""
author:Bevishe
date:2019/6/10
"""

import pandas as pd
import numpy as np
from sklearn.datasets import load_iris

data = load_iris()
# 将target拼接到第一列，并且将数据转换测DataFrame类型
irisData =  pd.DataFrame(np.insert(data.data,0,values=data.target,axis=1),columns=np.array(['target','feature1','feature2','feature3','feature4']))
print(irisData)

# 对数据进行划分，并将数据写入csv文件
from sklearn.model_selection import train_test_split

train,test = train_test_split(irisData,test_size=0.25)
print(train)
print(test)
train.to_csv('../data/iris/train.csv',index=False)
test.to_csv('../data/iris/test.csv',index=False)

from sklearn import tree
model = tree.DecisionTreeClassifier(criterion='entropy')
model.fit(train.iloc[:,1:],train.iloc[:,0])
print(model.score(test.iloc[:,1:],test.iloc[:,0]))



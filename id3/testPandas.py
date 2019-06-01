# _*_ coding:utf-8 _*_
"""
Author:BevisHe
Date:
"""

# 用来测试pandas对csv的处理
import pandas as pd
import numpy as np

data = pd.read_csv('../data/test.csv')
print(data.shape)
print(data.info())
print(data.values)
print(data.columns)
print(data['class'].shape)
print(data['class'].values)

newData = data.iloc[:,0]
print(newData)
S = pd.Series(newData)
print(S)
l = list(S.value_counts())
print(l)
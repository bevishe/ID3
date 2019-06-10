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

print("************************************")
dic = {'f1':{},'f2':{}}
print(dic)
dic['f1'][1] = {}
print(dic)

test = pd.read_csv('../data/test.csv')
newTest = test.iloc[1,1:-1].to_dict()
print(newTest)

dic = {1:{2:{'name':'he','sex':'nan'},4:5}}
print(dic.keys())
print(list(dic.keys()))
print(dic[1][2])
# _*_ coding:utf-8 _*_


# _*_ coding:utf-8 _*_

"""
Author:BevisHe
Date:
"""

import pandas as pd
import numpy as np

def ent(data):
    """
    用来计算熵
    :param data:
    :return:
    """
    C = pd.Series(data.iloc[:,0])
    ent = 0
    counts = list(C.value_counts())
    for i in range(len(counts)):
        p =  counts[i]/len(C)
        ent += p * np.log2(p)
    return -ent

# 计算各个属性的条件熵，按照V来划分数据集
def coditionEnt(data,V):
    coditionEnt = 0
    for i in data[V].unique():
        Vdata = data[data[V] == i]
        p = len(Vdata) / len(data)
        coditionEnt += p * ent(Vdata)
    return coditionEnt

# 计算最大信息增益的属性
def maxGain(data):
    gain = []
    cols = data.shape[1]
    features = list(data.columns[1:cols-1])
    for i in range(len(features)):
        g = ent(data) - coditionEnt(data,features[i])
        gain.append(g)
    gain = np.array(gain)
    return features[gain.argmax()]

# 获得属性之后，拆分数据集
def split(data,feature,value):
    newData = data[data[feature]==value]
    del newData[feature]
    return newData

# 若属性为空时，结果多的为终节点
def classfiy(C):
    counts = C.value_counts().sort_index()
    return str(counts.index[-1])

# 创建决策树
def decision_tree(data):
    features = list(data.columns[1])
    C = list(data.ix[:,data.shape[1]-1])
    if C.count(C[0]) == len(C):
        return C[0]
    if len(features) == 0:
        return classfiy(data.ix[:,data.shape[1]-1])
    feature = maxGain(data)
    tree = {feature:{}}
    for value in data[feature].unique():
        newData = split(data,feature,value)
        tree[feature][value] = decision_tree(newData)
    return tree

# 预测结果
def predict(tree,test):
    result = []
    for i in range(len(test)):
        newData = test.ix[i,0:4].to_dic()
        while isinstance(tree,dict):
            key = list(tree.keys())
            tree = tree[key][newData[key]]
        result.append(tree)
    return result

def accuracy():
    data = pd.read_csv('../data/train.csv')
    tree = decision_tree(data=data)
    print(tree)
    # test = pd.read_csv('../data/test.csv')
    # result = predict(tree,test)
    # accuracy =

if __name__ == '__main__':
    accuracy()

# _*_ coding:utf-8 _*_

"""
Author:BevisHe
Date:
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties
from sklearn import tree
from sklearn.datasets import load_iris

# import treeplotter


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
        p = counts[i]/len(C)
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
    print(gain)
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
    # 当前数据的第一个列
    features = list(data.head())[1:]
    print(features)
    # 当前数据的标签分类情况，当当前数据都是一类时，返回分类结果
    C = list(data.ix[:,0])
    if C.count(C[0]) == len(C):
        return C[0]
    # 当当前数据的属性已经都划分完了之后，选取当前数据中种类最多的作为分类结果返回
    if len(features) == 0:
        return classfiy(data.ix[:,0])
    # 计算每一次的feature特征属选择信息增益最大的那个
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
        # newData 是将预测的每一条数据变成一个字典
        newData = test.iloc[i,1:-1].T.to_dict()
        mytree = tree
        print(mytree)
        # 将test中每一条测试数据变为dict
        while isinstance(mytree,dict):
            key = list(mytree.keys())
            # 此处存在bug，当测试数据的某个属性值的情况未再训练集中出现就找不到，此时需要先检测dic中的value是否在mytree中
            if newData[key[0]] in mytree[key[0]]:
                mytree = mytree[key[0]][newData[key[0]]]
            else:
                mytree = -1         # 识别不出来标记为-1
        result.append(mytree)
    return result

# def classify(inputTree,testVec):
#     firstStr = list(inputTree.keys())[0]
#     secondDict = inputTree[firstStr]
#     for key in secondDict.keys():
#         if testVec[firstStr]==key:
#             if type(secondDict[key]).__name__=='dict':
#                 classlabel=classify(secondDict[key],testVec)
#
#             else:
#                 classlabel=secondDict[key]
#     return classlabel

# 统计模型的准确率，传入训练好的tree和测试数据集test
def accuracy(tree,test):
    result = predict(tree,test)
    # result = []
    # for i in range(test.shape[0]):
    #     result.append(classify(tree,test.iloc[i,:]))
    realResult = test.ix[:,0]
    print(result)
    print(realResult)
    tResult = 0
    for i in range(len(result)):
        if result[i] == realResult[i]:
            tResult += 1
    accur = i / len(result)
    print("预测正确的样本数有："+str(i))
    print("该模型的正确率是："+ str(accur))

# 使用sklearn自带的决策树进行测试
def sklearnTree(data,test):#传入的data数据集应该是DataFrame类型，同时第一列是样本标签
    x = data.iloc[1:,1:]
    y = data.iloc[1:,0]
    model = tree.DecisionTreeClassifier(criterion='entropy')
    # 训练
    model = model.fit(np.array(x), np.array(y))
    X_test = test.iloc[1:,1:]
    y_test = test.iloc[1:,0]
    print('Sklearn decisonTree Test score:{:.3f}'.format(model.score(np.array(X_test),np.array(y_test))))

if __name__ == '__main__':
    # 训练数据和测试数据
    trainData = pd.read_csv('../data/train3.csv')


    testData = pd.read_csv('../data/test3.csv')

    # 自己的实现
    mytree = decision_tree(data=trainData)
    print("通过ID3算法训练数据训练出来的决策树：")
    print("tree:")
    accuracy(mytree,test=testData)
    import treeplotter
    treeplotter.create_plot(mytree)

    # 自带库里面的实现方法
    sklearnTree(testData,testData)

    # irisData = load_iris()
    # print(irisData)
    #
    # print(irisData.data.shape)
    # print(irisData.target.shape)
    # print(irisData.target_names)
    #
    # irisDataFrame = pd.DataFrame(np.insert(irisData.data,0,values=irisData.target,axis=1),columns=np.arange(5))
    # print(irisDataFrame)
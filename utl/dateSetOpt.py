# _*_ coding:utf-8 _*_
"""
author:Bevishe
date:2019/6/7
"""
import pandas as pd
import numpy as np

def changeCharToNum(inputData):
    '''
    将inputData出的文件转换成属性都是数字的数据集，存储在outputData处
    :param inputData:
    :param outputData:
    :return: 成功返回0，失败返回-1
    '''
    features = list(inputData.head())
    dic = {}
    for feature in features:
        dic[feature] = list(inputData[feature].unique())
    # 对每一列中的属性，分别标号0到len（dic[feature]）-1
    for feature in features:
        for i in range(len(dic[feature])):
            inputData.loc[inputData[feature] == list(dic[feature])[i],feature] = i
    print(inputData)


def resetColumn(inputData):
    '''
    将标签从最后一列调整到最开始一列
    :param inputData:
    :return:
    '''
    features = list(inputData.columns)
    features = features[-1].append(features[0:-2])
    inputData.reindex(columns=features)



if __name__ == '__main__':
    changeCharToNum(pd.read_table('../data/data.txt'))
    data = pd.read_table('../data/data.txt',sep='\t')
    print(data.shape)
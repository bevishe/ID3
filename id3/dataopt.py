# _*_ coding:utf-8 _*_
"""
author:Bevishe
date:2019-05-29
"""
import pandas as pd
import numpy as np
from utl.dateSetOpt import resetColumn
#
cap_shape = ['b','c','x','f','k','s']
cap_surface = ['f','g','y','s']
cap_color = ['n','b','c','g','r','u','e','w','y','p']
bruises = ['t','f']
odor = ['a','l','c','y','f','m','n','p','s']
gill_attachment = ['a','d','f','n']
gill_spacing = ['c','w','d']
gill_size = ['b','n']
gill_color = ['k','n','b','h','g','r','o','p','u','e','w','y']
stalk_shape = ['e','t']
# stalk_root = ['b','c','u','e','z','r']
stalk_surface_above_ring = ['f','y','k','s']
stalk_surface_below_ring = ['f','y','k','s']
stalk_color_above_ring = ['n','b','c','g','o','p','e','w','y']
stalk_color_below_ring = ['n','b','c','g','o','p','e','w','y']
veil_type = ['p','u']
veil_color = ['n','o','w','y']
ring_number = ['n','o','t']
ring_type = ['c','e','f','l','n','p','s','z']
spore_print_color = ['k','n','b','h','r','o','u','w','y']
population = ['a','c','n','s','v','y']
habitat = ['g','l','m','p','u','w','d']
# # 'stalk_root':stalk_root,'
dic = {'cap_shape':cap_shape,'cap_surface':cap_surface,'cap_color':cap_color,'bruises':bruises,
       'odor':odor,'gill_attachment':gill_attachment,'gill_spacing':gill_spacing,'gill_size':gill_size,
       'gill_color':gill_color,'stalk_shape':stalk_shape,'stalk_surface_above_ring':stalk_surface_above_ring,
       'stalk_surface_below_ring':stalk_surface_below_ring,'stalk_color_above_ring':stalk_color_above_ring,
       'stalk_color_below_ring':stalk_color_below_ring,'veil_type':veil_type,'veil_color':veil_color,
       'ring_number':ring_number,'ring_type':ring_type,'spore_print_color':spore_print_color,'population':population,'habitat':habitat}
data = pd.read_csv('../data/mushrooms.csv')
print(data.shape)
data.loc[data['class'] == 'p','class'] = 1
data.loc[data['class'] == 'e','class'] = 0
print(data)
data = data.drop(axis = 1, labels=['stalk_root'])

def changeCToNum(data,columnName,list):
    for i in range(list.__len__()):
        data.loc[data[columnName] == list[i],columnName] = i


for k in dic.keys():
    changeCToNum(data,k,dic[k])
    print(k,dic[k])

print(data)
data.to_csv('../data/new2.csv')

from sklearn.model_selection import train_test_split
# 将数据集切分成训练集和测试集
def splitData():
    data = pd.read_csv('../data/new2.csv')
    train,test = train_test_split(data,test_size=0.25)
    train = train.reset_index().iloc[:,2:-1]
    test = test.reset_index().iloc[:,2:-1]
    train.to_csv('../data/train3.csv',index=False)
    test.to_csv('../data/test3.csv',index=False)

if __name__ == '__main__':
    # data = pd.read_csv('../data/IRIS.csv')
    # lis = list(data.ix[:,0].unique())
    # for i in range(lis.__len__()):
    #     data.loc[data[0]==lis[i],0] = i
    # print(data)
    splitData()

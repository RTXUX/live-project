# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 10:56:02 2019

@author: HP
"""
from sklearn.cluster import KMeans
import matplotlib .pyplot as plt
import numpy as np

def readCSV2List(filePath):
    file=open(filePath,'r',encoding='utf-8')# 读取以utf-8
    context = file.read() # 读取成str
    list_result=context.split("\n")#  以回车符\n分割成单独的行
    #每一行的各个元素是以【,】分割的，因此可以
    length=len(list_result)
    items=list_result[0].split(',')
    d={}
    l=[]
    for item in items:
        d[item]=[] 
        l.append(item)
    for i in range(length-2):
        items=list_result[i+1].split(',')
        for j in range(len(l)):
            d[l[j]].append(items[j])
    return d

def transfer(l):
    for i in range(len(l)):
        l[i]=float(l[i])
def dis(X,center):
    x=[]
    for item in X:
        x.append(((item[0]-center[0])**2+(item[1]-center[1])**2)**0.5)
    return x
def cluster_r(center,X,y_pre):
    l=[[] for i in range(len(center))]
    for i in range(len(X)):
        l[y_pred[i]].append(X[i])
    rlist=[]
    for i in range(len(center)):
        rlist.append(max(dis(l[i],center[i])))
    return rlist

dlist=readCSV2List(r"C:\Users\HP\Documents\Tencent Files\2780334265\FileRecv\HaikouRestaurants.csv")
transfer(dlist['经度'])
transfer(dlist['纬度'])
X=[]
for i in range(len(dlist['纬度'])):
    X.append([dlist['纬度'][i],dlist['经度'][i]])
X=np.array(X)
kmeans= KMeans(init='k-means++',n_clusters=7, random_state=9)
y_pred=kmeans.fit_predict(X)
print(kmeans.cluster_centers_)
plt.scatter(X[:,0],X[:,1],c=y_pred)
plt.show()
rlist=cluster_r(kmeans.cluster_centers_,X,y_pred)
print(rlist)
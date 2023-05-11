import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
V = pd.read_csv('https://raw.githubusercontent.com/jsedq/Conductividad_termica/main/Datos1.csv',header=0,  sep=';')
m=len(V)
n=len(V.columns)
r=m/40
r=int(r)
list1=[]
list3=[]
for i in range(0,r):
    list2=[]
    list=[]
    for j in range(40*i,40*(i+1)):
        list2.append(V.loc[j][0])
    q=len(list2)
    for k in range(q):
        if list2[k] not in list:
            list.append(list2[k])
    band=False
    while band==False:
        band=True
        for l in range(len(list)-1):
            if list[l] > list[l+1]:
                aux=list[l]
                list[l]=list[l+1]
                list[l+1]=aux
                band=False
    list1.append(list[-1])
print(list1)
for i in range(0,r):
    list2=[]
    list=[]
    for j in range(40*i,40*(i+1)):
        list2.append(V.loc[j][1])
    q=len(list2)
    for k in range(q):
        if list2[k] not in list:
            list.append(list2[k])
    band=False
    while band==False:
        band=True
        for l in range(len(list)-1):
            if list[l] > list[l+1]:
                aux=list[l]
                list[l]=list[l+1]
                list[l+1]=aux
                band=False
    list3.append(list[-1])
print(list3)

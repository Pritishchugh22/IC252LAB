#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr 24 00:49:28 2019

@author: tushar
"""

import pandas as pd
df=pd.read_csv('medical_expenditure.csv')
a=["Nmale","Nfemale","Nhp0","Nhp1","Nicd2"]
tot=df["Nmale"].count()
b=["AverageDailyExpenditure"]*5
aasd=[]
for i in range(5):
    aa=df[a[i]].mean()
    ss1=df[a[i]].std()
    df[a[i]]=df[a[i]]-aa   
    ab=df[b[i]].mean()
    ss2=df[b[i]].std()
    df[b[i]]=df[b[i]]-ab
    df["ank"]=df[b[i]]*df[a[i]]
    aaa=df["ank"].sum()
    print(round(aaa/(tot-1),2))
    aaaaa=round(aaa/(tot-1),2)
    r=aaaaa/(ss1*ss2)
    aasd.append(r)
for i in range(5):
    r=aasd[i]
    if r==0:
        print("None")
    elif -0.1<=r<0:
        print("weak")
    elif -0.3<=r<-0.1:
        print("moderate")
    elif -0.5<=r<-0.3:
        print("strong")
        

#code 2 and 3.py
#Displaying code 2 and 3.py.
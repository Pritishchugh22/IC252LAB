#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 08:52:36 2019

@author: tushar
"""

import pandas as pd

file=open("/home/tushar/Downloads/file_B.dat",'r')
list1=file.read().split()

citylist=list1[::2]
productlist=list1[1::2]

d = {'City':citylist,'Product':productlist}

df=pd.DataFrame(d)
x=input("Enter the source city: ")

y=input("Enter the product:  ")

xtoy=df['City'][df['City']==x][df['Product']==y].count()
xcount=df['City'][df['City']==x].count()
print("(a) is ",xtoy/xcount)
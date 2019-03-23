#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 08:34:37 2019

@author: tushar
"""


'''
Let x be a destination and y be a source. Accept x and y from the user.
(a) Estimate the probability that destination x was forwarded from source router y.
(b) What is the probability that a packet comes from source y
'''

import pandas as pd

file=open("/home/tushar/Downloads/file_B.dat",'r')
list1=file.read().split()

srclist=list1[::2]
destlist=list1[1::2]
d = {'Src':srclist,'Destn':destlist}

df=pd.DataFrame(d)
x=input("Enter the source router: ")

y=input("Enter the destination:  ")

xtoy=df['Src'][df['Src']==x][df['Destn']==y].count()
xcount=df['Src'][df['Src']==x].count()
print("(a) is ",xtoy/xcount)

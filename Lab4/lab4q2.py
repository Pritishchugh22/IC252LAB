#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 11:49:43 2019

@author: tushar
"""

import matplotlib.pyplot as plt
import numpy as np

def fact(n):
    if n==0: return 1
    else: return n*fact(n-1)

def comb(n,k):
    return fact(n)/(fact(k)*fact(n-k))

N,n =500,10

x=[]
for p in [0.2,0.8]:
    f=open("binomial_N_n_"+str(p)+".dat",'w',encoding="utf8")
    d=list(np.random.binomial(n,p,size=N))
    x.append(d)
    for i in d: f.writelines(str(i)+"\n")
    f.close()

p1,p2=0.2,0.8
a=[comb(n,i)*(p1**i)*((1-p1)**(n-i)) for i in x[0]]
b=[comb(n,i)*(p2**i)*((1-p2)**(n-i)) for i in x[0]]
c=[comb(n,i)*(p1**i)*((1-p1)**(n-i)) for i in x[1]]
d=[comb(n,i)*(p2**i)*((1-p2)**(n-i)) for i in x[1]]
data=np.column_stack((a,b,c,d))
#print(data)

plt.grid()
for lis in [a,b,c,d]:
    plt.hist(lis,rwidth=0.24)
   # print(lis)
plt.show()
for lis in [a,b,c,d]: 
    plt.plot(lis)
plt.show()
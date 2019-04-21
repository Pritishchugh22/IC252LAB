#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 13:29:48 2019

@author: tushar
"""

import numpy as np,matplotlib.pyplot as plt
p,q=input("Enter p_q..").split()
p=float(p);q=float(q);
n=int(input("N="))
X=list(np.random.choice([0,1],p=[.5,.5],size=n))
Y=[]
a11=0
a10=0
a01=0
a00=0
for a in X:
    if a==1:
        aa=int(np.random.choice([0,1],p=[q,1-q]))
        Y.append(aa)
        if aa==1:
            a11+=1
        else:
            a10+=1
    else:
        ab=int(np.random.choice([0,1],p=[1-p,p]))
        Y.append(ab)
        if ab==1:
            a01+=1
        else:
            a00+=1
q,w=np.unique(Y,return_counts=True)
print("Y=0  =>",w[0]/n,"\nY=1  =>",w[1]/n)
print("X=0 Y=0",a00/n,"\nX=0 Y=1",a01/n,"\nX=1 Y=0",a10/n,"\nX=1 Y=1",a11/n)
print("1-p=",2*(a00/n),"\nq=",2*(a01/n),"\np=",2*(a10/n),"\n1-q",2*(a11/n))
plt.scatter([0,1],[w[0]/n,w[1]/n])
plt.show()
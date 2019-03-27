#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 11:21:10 2019

@author: tushar
"""

import numpy as np,matplotlib.pyplot as plt

N,n,p=[float(x) for x in input().split()]

for iw in [p,0.1,0.5,0.9]:
    data=np.random.binomial(int(n),iw,int(N))
    with open("ass.dat","w+") as dat:
        for i in range(len(data)):
            dat.writelines(str(data[i]))
            dat.writelines("\n")
    bins = np.arange(0, max(data) + 2,1)-0.5
    print(bins)
    #plt.hist(data,bins=bins,rwidth=0.92);plt.margins(0.02)
    plt.hist(data,bins,align="mid",rwidth=0.9)
    plt.xlabel("X axis")
    plt.ylabel("Y axis")
    plt.show()
    dat.close()

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 10:53:11 2019

@author: tushar
"""
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

N=int(input())
n=int(input())
p=float(input())

datapoints=np.random.binomial(n,p,N)
print(datapoints)

#%%

df=pd.DataFrame({'Data':datapoints})
df.to_csv('binomial_N_n_p.dat',index=False)

#%%
sns.set()
bins=[np.arange(0,n,1)]
plt.hist(datapoints,rwidth=0.6,edgecolor='r')
plt.xticks(np.arange(int(min(datapoints)),int(max(datapoints)),1))
plt.xlabel('Intervals')
plt.title('Analysis via Histogram')
plt.show()
#%% 
sns.set()
plt.hist(np.random.binomial(n,0.1,N),rwidth=0.6,edgecolor='r')
#plt.xticks(np.arange(int(min(datapoints)),int(max(datapoints)),1))
plt.xlabel('Intervals')

plt.title('Analysis via Histogram')
plt.show()
#%%
sns.set()
plt.hist(np.random.binomial(n,0.5,N),rwidth=0.6,edgecolor='r')
#plt.xticks(np.arange(int(min(datapoints)),int(max(datapoints)),1))
plt.xlabel('Intervals')
plt.title('Analysis via Histogram')
plt.show()
#%%
sns.set()
plt.hist(np.random.binomial(n,0.9,N),rwidth=0.6,edgecolor='r')
#plt.xticks(np.arange(int(min(datapoints)),int(max(datapoints)),1))
plt.xlabel('Intervals')
plt.title('Analysis via Histogram')
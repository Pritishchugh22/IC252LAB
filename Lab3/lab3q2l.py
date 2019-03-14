#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 18:49:18 2019

@author: tushar
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

ntrials = [10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000]

def computeProb(n):
    df = pd.DataFrame(columns = ['T', 'C'])
    df.T = np.random.random(n)
    df.C = np.random.random(n)

    for i, col in enumerate(['T', 'C']):
        temp = np.array(df[col])
        idx4 = np.where(np.logical_and(temp >= 0, temp < 0.5) == True)
        df.iloc[list(idx4[0]), i] = 4

        indices = [np.where(np.logical_and(temp >= j/10, temp < 0.1*(j+1)) == True) for j in range(5, 10)]
        nums = [1, 2, 3, 5, 6]
        for k in range(len(nums)):
            df.iloc[list(indices[k][0]), i] = nums[k]

    t = df['T'][df['T'] >= 4].count()
    c = df['C'][df['C'] < 4].count()
    return (t/n)*(c/n)

lst = []
for n in ntrials:
    lst.append(computeProb(n))
scaleddowntrials=list(map(math.log10,ntrials))
print('-----------------------------')
print('Hand Calculated Value is 0.21')
print('------------------------------')
plt.plot(scaleddowntrials,lst)

plt.grid()
plt.xlabel('log(numberoftrials) ==>')
plt.ylabel('Cond. Probab. for particular number of trials==>')
plt.axhline(0.21,linestyle='dashed',alpha=0.5)
#plt.text(3,0.21,'Joint probability P(T≥ 4,C< 4)',fontsize=9)
plt.text(3.3, 0.21, '0.21', fontsize=10, va='center', ha='center')
plt.title('Experiment',fontsize=20)
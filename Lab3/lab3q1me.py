#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 12:09:12 2019

@author: tushar
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import math

ntrials = [10, 50, 100, 500, 1000, 5000, 10000, 50000, 100000]


def computeProb(n):
    df = pd.DataFrame(columns = ['T', 'C'])
    df.T = np.random.randint(1,7,n)
    df.C = np.random.randint(1,7,n)
    T = df['T'][df['T'] >= 4].count()
    C = df['C'][df['C'] < 4].count()
    direct=df['T'][df['T'] >= 4][df['C'] < 4].count()
    return (T*C)/(n*n)

lst = []

for n in ntrials:
    lst.append(computeProb(n))
scaleddowntrials=list(map(math.log10,ntrials))
print('-----------------------------')
print('Hand Calculated Value is 0.25')
print('------------------------------')
plt.plot(scaleddowntrials,lst)

plt.grid()
plt.xlabel('log(numberoftrials) ==>')
plt.ylabel('Cond. Probab. for particular number of trials==>')
plt.axhline(0.25,linestyle='dashed',alpha=0.5)
plt.text(3,0.24,'Joint probability P(T≥ 4,C< 4)',fontsize=9)
plt.text(3.3, 0.25, '0.25', fontsize=10, va='center', ha='center')
plt.title('Experiment',fontsize=20)






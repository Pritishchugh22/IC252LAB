#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May 27 15:57:53 2019

@author: tushar
"""
#%%
import numpy as np
import math
import matplotlib.pyplot as plt


N = 100    # no of I.I.Ds to be generated

# Part A : Creating n i.i.ds  => Gaussian(mean,std_dev)
Lambda = 7
X = np.random.exponential(1/Lambda,N)


# n = known = t
# p = unknown
P = np.arange(3,11,0.2)
L = []
for p in P:
    lp = 1
    for xi in X:
        lp *= p*(math.exp(-p*xi))
    L.append(lp)
plt.plot(P,L)

p_max = np.argmax(L)
print(P[p_max])

plt.axvline(P[p_max],color='r',ls='dashed',label=str(P[p_max]))
plt.legend()
plt.grid()

plt.yticks([])
#%%
import numpy as np
import math
import matplotlib.pyplot as plt
import scipy.stats as st
binom=st.binom.pmf
N=100#no. of iid data points 

D=np.random.binomial(100,0.7,N)


P=np.arange(0.1,1,0.01)
L=[]
for p in P:
    l=0
    for i in range(N):
        l=l+math.log(binom(D[i],100,p))
    L.append(l)

p_max = np.argmax(L)
print(P[p_max])
plt.plot(P,L)
plt.axvline(P[p_max],color='r',ls='dashed',label=str(P[p_max]))
plt.legend()
plt.grid()

plt.yticks([])

#%%
import numpy as np
import math
import matplotlib.pyplot as plt
norm=st.norm.pdf
N=100
D=np.random.normal(0,9,N)
P=np.arange(6,12,0.2)

L=[]
for p in P:
    l=0
    for i in range(N):
        l=l+math.log(norm(D[i],0,p))
    L.append(l)

p_max = np.argmax(L)
print(P[p_max])
plt.plot(P,L)
plt.axvline(P[p_max],color='r',ls='dashed',label=str(P[p_max]))
plt.legend()
plt.grid()

plt.yticks([])


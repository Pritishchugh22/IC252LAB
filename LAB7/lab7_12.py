#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  1 13:03:47 2019

@author: tushar
"""

import pandas as pd
import numpy as np
d = pd.DataFrame({"a":[50,20,10],"b":[50,20,10]})
x,z=int(input("x=")),int(input("z="))
y=0
for i in range(x):
     d[i] =np.random.randint(0,2,size=3)
     if z==1:
         d["a"]+=d["b"]*d[i]
     if z==2:
         if d[i].tolist().count(1)==2:
             y+=1
             d["a"]+=d["b"]*d[i]
if z==1:
     print(d["a"].sum()/x)
if z==2:
     print(d["a"].sum()/y)
     
     
     
import random
#question 2
print("a.)")
sum1=0
for i in range(10000):
     p=random.randint(1,6)
     sum1+=p*pow(-1,p+1)
print(sum1/10000)
print()
print("b.)")
sum2=0
for i in range(10000):
     p=random.randint(1,6)
     sum2+=p*pow(-1,p)
print(sum2/10000)
print()

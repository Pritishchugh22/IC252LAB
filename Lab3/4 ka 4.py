#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 14 01:53:05 2019

@author: b18007
"""
#importing libraries
import numpy as np
ss=[]
l=0
#N=50
for i in range(100000):
    birthday=list(np.random.randint(1,366,23))
    #applying algorithm
     #take elements from set of birthday..
    #calculate no. of time it repeats..
    #subtract -1
    #multiply with string
    #filter None
    #calculate length
    #append it in list ss
    a=["a"*(birthday.count(s)-1) for s in set(birthday)]
    b=list(filter(None,a))
    #checking the condition.. c>=1
    if len(b)>=1:
        l+=1
#print answer
print("probability",l/100000)


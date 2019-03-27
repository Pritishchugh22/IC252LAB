#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 13:36:39 2019

@author: tushar
"""

#. A discrete random variable X takes on values 1, 2 and 3 with probabilities 0.1, 0.2 and 0.7 respectively.
#Generate N = 1000 realizations of X. Estimate the probabilities of X from the generated realizations
import numpy as np
l=[1,2,2,3,3,3,3,3,3,3]
s=[]
for i in range(10000):
    s.append(np.random.choice(l))
print(s.count(1)/1000)
print(s.count(2)/1000)
print(s.count(3)/1000)
import socket
socket.get
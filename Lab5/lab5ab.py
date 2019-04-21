#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 16 13:40:20 2019

@author: tushar
"""

#import modules
import numpy as np,matplotlib.pyplot as plt
#take input
p,q=input("Enter p_q..==>").split()
p=float(p);q=float(q);
n=int(input("N="))
#create list of X with probability of x=0 and x=1 with each having prob. of 0.5
X=list(np.random.choice([0,1],p=[.5,.5],size=n))
Y=[]
a11=0
a10=0
a01=0
a00=0
#use condition given to create Y
#(1) Generate a value of X .
#(2) Let x1 be the value generated in step 1.
#(3) From the given joint pmf find P(Y = y|X = x1) for y ∈ R(Y ).
#(4) Using this conditional pmf and generate a sample of Y
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
#Count Y=1 and Y=0 ... 
q,w=np.unique(Y,return_counts=True)
#print and enjoy....
print("Y=0  =>",w[0]/n,"   Y=1  =>",w[1]/n)
print("X=0 Y=0",a00/n,"\nX=0 Y=1",a01/n,"\nX=1 Y=0",a10/n,"\nX=1 Y=1",a11/n)
x0=X.count(0)
x1=X.count(1)
print("X=0=>",x0,"X=1=>",x1)
print("1-p=",(a00/x0),"\nq=",(a01/x0),"\np=",(a10/x1),"\n1-q",(a11/x1))
#create a plot...
plt.scatter([0,1],[w[0]/n,w[1]/n])
plt.title('PMF of Y')
plt.ylabel('Probability')
plt.xlabel('Values of Y')
plt.show()
#create a plot...
plt.scatter(["X=0 and Y=0",'X=0 and Y=1',"X=1 and Y=0",'X=1 and Y=1'],[a00/n,a01/n,a10/n,a11/n])
plt.ylabel('Probability')
plt.title('Joint PMF of X,Y')
plt.xlabel('Range')
plt.show()

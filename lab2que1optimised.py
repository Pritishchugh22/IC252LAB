#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 12:01:58 2019

@author: tushar
"""
#%%
print('Accept the file name:')
filename=input()
if( filename=='A'):
    f="/home/tushar/Desktop/IC252/ic252_lab1_data/largeTextFiles/fileA_time_mach.txt"
else:
    f="/home/tushar/Desktop/IC252/ic252_lab1_data/largeTextFiles/fileB_jane_eyre.txt"    

data=open(f,"r")
charcount={ch : 0 for ch in [chr(i) for i in range(97, 123)]}
for char in data.read():
    try:
        charcount[char.lower()]+=1
    except:
        pass

for val in charcount.values():
    sum=sum+val
probcharcount={ch : 0 for ch in [chr(i) for i in range(97, 123)]}

for i in probcharcount:
    probcharcount[i] = charcount[i] / sum

x = input('Enter x:').lower()
y = input('Enter y:').lower()

print('Computing the prior probability of x and prior probability of y')
print('---------')
print('Prior probability of',x,':',round(probcharcount[x],4))
print('Prior probability of ',y,':',round(probcharcount[y],4))
print('---------')

file = ''
data=open(f,"r")
for i in data.read():
    try:
        i = i.lower()
        if 97 <= ord(i) <= 122:
            file += i
    except:
        pass
    
total_y_bigram = file.count(y)

if file[-1] == y:
    total_y_bigram -= 1
    
total_x_bigram = file.count(x)
if file[-1] == x:
    total_x_bigram -= 1
    
total_yx_bigram = file.count(y+x)
total_xy_bigram = file.count(x+y)
print('Conditional probability P(',x,'|',y,') = ',round(total_yx_bigram/total_y_bigram,4))
print('Conditional probability P(',y,'|',x,') = ', round(total_xy_bigram/total_x_bigram,4))
print('---------')
#%%
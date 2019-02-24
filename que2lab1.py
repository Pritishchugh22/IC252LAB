#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 24 16:41:07 2019

@author: tushar
"""
#%%
def readfile(file):
    f=open(file,"r")
    charcount={ch : 0 for ch in [chr(i) for i in range(97, 123)]}
    for char in f.read():
        try:
            charcount[char.lower()]+=1
        except:
            pass
    reqdlist=sorted(charcount, key = lambda i : charcount[i],reverse=True)[0:10]
    print(reqdlist)
    print()
    sum=0
    for val in charcount.values():
        sum=sum+val
    probcharcount={ch : 0 for ch in [chr(i) for i in range(97, 123)]}
    
    for i in probcharcount:
        probcharcount[i] = charcount[i] / sum

    print(probcharcount)
    print()        
    f.close()
    
    
    
    
   
readfile("/home/tushar/Desktop/IC252/ic252_lab1_data/largeTextFiles/fileA_time_mach.txt")
readfile("/home/tushar/Desktop/IC252/ic252_lab1_data/largeTextFiles/fileB_jane_eyre.txt")
print("Result is not same for fileA and fileB")

        
 #%%       
        
 
    
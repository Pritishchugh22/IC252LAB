#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 23 22:43:07 2019

@author: tushar
"""

import pandas as pd
import numpy as np

df=pd.read_csv('medical_expenditure.csv')
#Please check whether the following events are independent between 2nd January 2011 and 15th April 2015: 
#
#(A) “Number of males <= 93” and “Average daily expenditure on medicine A <= $504”.
#(B) “Number of females <= 131” and “Average daily expenditure on medicine A <= $504”.
#(C) “Number in age-group 2” <= 25” and “Average daily expenditure on medicine A > $504”.
#(D) “Number in age-group 2” <= 25” and “Average daily expenditure on medicine A > $504”.
#(E) “Number in region 5” <= 53” and “Average daily expenditure on medicine A > $504”.
#

#%%
#A)
PA=df['Nmale'][df['Nmale']<=93].count()/len(df)
PB=df['AverageDailyExpenditure'][df['AverageDailyExpenditure']<=504].count()/len(df)
print('P(A) is',PA)
print('P(B) is',PB)
PAB=df['Nmale'][df['Nmale']<=93][df['AverageDailyExpenditure']<=504].count()/len(df)

if(PAB==PA*PB):
    print('A and B are independent')
else:
    print('Not Independent ')

#%%
print('P(A) = ', df['Nfemale'][df['Nfemale'] <= 131].count()/len(df))
print('P(B) =', df['AverageDailyExpenditure'][df['AverageDailyExpenditure']<=504].count()/len(df))

if (df['Nfemale'][df['Nfemale'] <= 131].count()/len(df)*\
    df['AverageDailyExpenditure'][df['AverageDailyExpenditure']<=504].count()/len(df) ==\
    df['Nfemale'][df['Nfemale']<=131][df['AverageDailyExpenditure']<=504].count()/len(df)):
        
        print('A and B independent')
else:
    print('A and B are Not Independent')
#%%
if (df['Nage-group2'][df['Nage-group2'] <= 25].count()/len(df)*\
    df['AverageDailyExpenditure'][df['AverageDailyExpenditure']>504].count()/len(df) ==\
    df['Nage-group2'][df['Nage-group2']<=25][df['AverageDailyExpenditure']<=504].count()/len(df)):
        
        print('independent')
else:
    print('Not Independent')
    
#%%    

if (df['Nage-group5'][df['Nage-group5'] <= 53].count()/len(df)*\
    df['AverageDailyExpenditure'][df['AverageDailyExpenditure']>504].count()/len(df) ==\
    df['Nage-group5'][df['Nage-group5']<=53][df['AverageDailyExpenditure']<=504].count()/len(df)):
        
        print('independent')
else:
    print('Not Independent')
    
#%%
def pearson():
    Y=list(df['AverageDailyExpenditure'])
    y=df['AverageDailyExpenditure'].mean()
    lst = ['Nmale', 'Nfemale', 'Nhp0', 'Nhp1', 'Nicd2']
    for inp in lst:
        X=list(df[inp])
        x=df[inp].mean()
        z = list(zip(X, Y))
        sm = 0
        for i in z:
            sm += (i[0]-x) * (i[1]-y)
        cov = sm / (len(X) - 1)

        print('Covariance of {0} and AverageDailyExpenditure is: '.format(inp),cov)
        print('Covariance of {0} and AverageDailyExpenditure by Python library is: '.format(inp),np.cov(X,Y)[0][1])
        
        #3)
        print('Pearson Correlation of {0} and AverageDailyExpenditure is: '.format(inp),cov/(df[inp].std()*df['AverageDailyExpenditure'].std()))
        if(cov/(df[inp].std()*df['AverageDailyExpenditure'].std())>-0.1):
            print('WEAK')
        else:
            print('MODERATE')
        print()

  
pearson()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 13:06:07 2019

@author: tushar
"""
import pandas as pd
df=pd.read_csv('/home/tushar/Downloads/AllElectronicsCustomer.csv')
Count_Buys_Yes=df['Class: Buys_Computer'][df['Class: Buys_Computer']=='Yes'].count()
Count_Buys_No=df['Class: Buys_Computer'][df['Class: Buys_Computer']=='No'].count()
print('Give the attribute you need to discuss for the probability')
attribute=input()
print('Give value of attribute')
value=input()
val_Count_Buys_Yes=df['Class: Buys_Computer'][df['Class: Buys_Computer']=='Yes'][df[attribute]==value].count()
val_Count_Buys_No=df['Class: Buys_Computer'][df['Class: Buys_Computer']=='No'][df[attribute]==value].count()

print('Probability of ',value,attribute,' customer buying the computer i.e., P(',attribute,'=',value,'|Buys_Computer = Yes)',val_Count_Buys_Yes/Count_Buys_Yes)
print('Probability of',value,attribute,' customer not buying the computer i.e., P(',attribute,'=',value,' |Buys_Computer =No)',val_Count_Buys_No/Count_Buys_No)


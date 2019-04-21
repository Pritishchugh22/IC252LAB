#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 22:37:37 2019

@author: tushar
"""

import pandas as pd
#Read the file by adding the COlumn Headings 

df=pd.read_csv('systemA.csv',names=['Date/Time','Code','Range','Result'])
#Splitting the first column to 3 columns containing Date,Time and AM/PM respectively and making a seperate dataframe

df2=pd.DataFrame(df['Date/Time'].str.split(' ',2).tolist(),
                                   columns = ['Date', 'Time', 'AM/PM'])
#Getting the index of the column which we splitted

i = df.columns.get_loc('Date/Time')
#Making required dataframe
df3=pd.concat([df.iloc[:, :i], df2, df.iloc[:, i+1:]], axis=1)
#Changing the format of Dates
df3['Date'] =pd.to_datetime(df3.Date)
#Sorting the dataframe by 'DATA','AM/PM','Time'

df3=df3.sort_values(['Date','AM/PM','Time'])
#Saving the final dataframe in a csv file

df3.to_csv('out.csv',encoding='utf-8')
#Joining the results of HIT In a single string

string=''.join(list(df3['Result']))
#Taking K as input from user

K=int(input('Enter K:'))
src='M'*K+'H'
#Method1
print('Method1:\n The probability that System A performed K firings before hitting the target (i.e. the\
target was hit on the K + 1 th firing)?',string.count(src)/(len(df3)-(K+1)+1))
#Method2
print('Method2: \n the probability that System A performed K firings before hitting the target (i.e. the\
target was hit on the K + 1 th firing) without sorting ?',''.join(list(df['Result'])).count(src)/(len(df3)-(K+1)+1))

#the probability of hitting the target be p
p=string.count('H')/(len(df3))
print('\nThe probability of hitting the target be p is:',p)
#Method3
print('Method3:\n The probability that System A performed K firings before hitting the target (i.e. the\
target was hit on the K + 1 th firing)?', p*(1-p)**K)
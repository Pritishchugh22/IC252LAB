#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 19 22:25:31 2019

@author: tushar
"""
import pandas as pd

df=pd.read_csv('cneos_fireball_data.csv')
df = pd.DataFrame(df['Peak Brightness Date/Time (UT)'].str.split(' ',1).tolist(),
                                   columns = ['Date','time'])
df.sort_values(by='Date')
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 06:52:55 2018

@author: Nita
"""


import pandas as pd

print(sys.argv[0])
# Read the data in 
seqs = pd.read_csv('./csvfiles/GenbankStats.csv') 
print(seqs.mean())

#set the date column to datetime
seqs.Date = pd.to_datetime(seqs.Date, infer_datetime_format=True)

#locate by column name and print
print(seqs.loc[10:15,['Sequences']])
#set the index to the date column and print
seqs.set_index('Date', inplace=True)
print(seqs.index)

#group by year and sum
summed_data=seqs['Sequences'].resample('A').sum()
print(summed_data)




# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 06:52:55 2018

@author: Nita
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
 
plt.rcParams['figure.figsize']=(20,10) # set the figure size
plt.style.use('fivethirtyeight') # using the fivethirtyeight matplotlib theme
#Set up Fonts for the text on the plot
font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 24}
plt.rc('font', **font)
 
seqs = pd.read_csv('C:/Users/Nita/Documents/PythonScripts/GenbankStats.csv') # Read the data in
print(seqs.loc[:,['Date']])
seqs.Date = pd.to_datetime(seqs.Date, infer_datetime_format=True) #set the date column to datetime
print(seqs.loc[:,['Date']])
seqs.set_index('Date', inplace=True) #set the index to the date column
print(seqs.index)
#group by year and sum
summed_data=seqs['Sequences'].resample('A').sum()
print(summed_data)

#fig = plt.figure()
ax1 = plt.subplot2grid((1,1), (0,0))
ax1.set_title('Genbank Annual Sequence Submissions')
ax1.get_yaxis().get_major_formatter().set_scientific(False)
summed_data.plot(color='r')
plt.legend()
plt.show()

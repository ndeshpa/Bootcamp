# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 06:52:55 2018

@author: Nita
"""
import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style

if(len(sys.argv) == 1):
    print("Please enter the complete path of the csv file. Ex: C:/your/folder/name/filename.csv")
    sys.exit
else:
    #Set up Fonts for the text on the plot
    font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 24}
    plt.rc('font', **font)
    
     # Read the data in
    seqs = pd.read_csv(sys.argv[1])
    print(seqs.loc[:,['Date']])
    #set the date column to datetime
    seqs.Date = pd.to_datetime(seqs.Date, infer_datetime_format=True)
    print(seqs.loc[:,['Date']])
    #set the index to the date column
    seqs.set_index('Date', inplace=True)
    print(seqs.index)
    #group by year and sum
    summed_data=seqs['Sequences'].resample('A').sum()
    print(summed_data)

    ax=summed_data.plot(color='r')
    ax.get_yaxis().get_major_formatter().set_scientific(False)
    ax.set_title('Genbank Annual Sequence Submissions') 
    plt.legend()
    plt.show()

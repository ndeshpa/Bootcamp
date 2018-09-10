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
    # set the figure size
    plt.rcParams['figure.figsize']=(20,10) 
    # using the fivethirtyeight matplotlib theme
    #Set up Fonts for the text on the plot
    plt.style.use('fivethirtyeight')
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

    ax1 = plt.subplot2grid((1,1), (0,0))
    ax1.set_title('Genbank Annual Sequence Submissions')
    ax1.get_yaxis().get_major_formatter().set_scientific(False)
    summed_data.plot(color='r')
    plt.legend()
    plt.show()

# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 06:52:55 2018

@author: Nita
"""

import numpy as np      # Python package for number crunching/math
import pandas as pd     # Python package for data analysis - used widely in 
                        # Data Science
import matplotlib.pyplot as plt #Popular plotting/graphing library
from matplotlib import style


# Read the data in using the Pandas read_csv function. Pandas also has functions
# to read from excel files, SQL databases etc and write to the same

# Once read, the data is mantained as a dataframe
seqs = pd.read_csv('./csvfiles/GenbankStats.csv')

#The dataframe can be manipulated in many ways:
# The following line retrieves data from the 'Date' column from first to the
# last row and prints it to std out 
print(seqs.loc[:,['Date']])

# Column manipulations - 
# set the date column to datetime and print to std out
seqs.Date = pd.to_datetime(seqs.Date, infer_datetime_format=True)
print(seqs.loc[:,['Date']])

#set the index to the date column
seqs.set_index('Date', inplace=True)
print(seqs.index)

# Row manipulations - 
# group rows by by year using the 'resample' method and sum/year
# Resample is a convenience method that groups a time series by 
# periodicity of your choice - Ex. Seconds, Minutes, Hours, Days etc
# In this case, the argument 'A' groups the periods by year
summed_data=seqs['Sequences'].resample('A').sum()
print(summed_data)

#Set up Fonts for the text on the plot
font = {'family' : 'normal',
    'weight' : 'bold',
    'size'   : 24}
plt.rc('font', **font)

# plot the summed data
ax=summed_data.plot(color='r')

# set scientific notation off on the y axis
ax.get_yaxis().get_major_formatter().set_scientific(False) 

# set the plot title
ax.set_title('Genbank Annual Sequence Submissions') 

# set to print the legend and draw
plt.legend()
plt.show()

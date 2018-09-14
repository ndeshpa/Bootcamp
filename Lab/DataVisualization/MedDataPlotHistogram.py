# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 10:38:12 2018

@author: Nita
"""


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Read in the data into a dataframe
medData=pd.read_csv('./csvfiles/processed.cleveland.data.csv')
medDataDf = pd.DataFrame(medData)
print(medDataDf)
 
# Histogram data can be created using the histogram() function in numpy  
# np.histogram bins the data into 10 equal sized bins
hist, binEdges = np.histogram(medData['Age'])
    
print(hist)
print(binEdges)    
    
# Alternatively, use matplotlib hist function directly to set up the binned
# data and draw the histogram
 #matplotlib hist function will auto bin the data and present it as
# a histogram

n, bins, patches = plt.hist(x=medData['Age'], bins='auto', color='#0504aa',
                        alpha=0.7, rwidth=0.85)
print('------------------')
print(bins)

#Set up Fonts for the text on the plot
font = {'family' : 'normal',
    'weight' : 'bold',
    'size'   : 24}
plt.rc('font', **font)

# the histogram set up by matplotlib can then be plotted
plt.grid(axis='y', alpha=0.75)
plt.xlabel('Age')
plt.ylabel('Frequency')
plt.title('Distribution of Data set by Age')
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 10 10:38:12 2018

@author: Nita
"""

import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

if(len(sys.argv) == 1):
    print("Please enter the complete path of the csv file. Ex: C:/your/folder/name/filename.csv")
    sys.exit
else:
    #Set up Fonts for the text on the plot
    font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 24}
    plt.rc('font', **font)

    medData=pd.read_csv(sys.argv[1])
    medDataDf = pd.DataFrame(medData)
    print(medDataDf)
    
    #np.histogram bins the data into 10 equal sized bins
    hist, binEdges = np.histogram(medData['Age'])
    
    print(hist)
    print(binEdges)    
    
    #OR, use matplotlib hist function directly to set up the binned
    # data and draw the histogram
    #matplotlib hist function will auto bin the data and present it as
    #a histogram
    n, bins, patches = plt.hist(x=medData['Age'], bins='auto', color='#0504aa',
                            alpha=0.7, rwidth=0.85)
    print('------------------')
    print(bins)
    plt.grid(axis='y', alpha=0.75)
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.title('Distribution of Data set by Age')
   
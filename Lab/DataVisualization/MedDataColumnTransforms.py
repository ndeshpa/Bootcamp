# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 11:28:40 2018

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
        'size'   : 20}
    plt.rc('font', **font)

    medData=pd.read_csv(sys.argv[1])
    medDataDf = pd.DataFrame(medData)
    print(medDataDf)

    #add a new column identifying rows with RestBP >120
    medDataDf['HighRestBP']=medDataDf['RestBP'].apply(lambda x: x > 120)
    #add a new column identifying rows with FBS = 0/1
    medDataDf['HighFBS']=medDataDf['FBS'].apply(lambda x: x == 1)
    
    #create boolean variables for each condition
    edf=medDataDf['RestECG'] == 2
    hrBp=medDataDf['RestBP'] > 120
    hFbs=medDataDf['FBS'] == 1
    #retrieve dataframe rows that test true for all conditions
    print(medDataDf[edf & hrBp & hFbs].count())
    
    #calculate mean of all values in a column
    print("Mean of Column RestBP:", medDataDf['RestBP'].mean())
    #calculate max of all values in a column
    print("Max value of Column RestBP:", medDataDf['RestBP'].max())
    #calculate min of all values in a column
    print("Min value of Column RestBP:", medDataDf['RestBP'].min())
    #calculate median of all values in a column
    print("Median of Column RestBP:", medDataDf['Age'].median())

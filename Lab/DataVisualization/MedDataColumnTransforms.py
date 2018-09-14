# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 11:28:40 2018

@author: Nita
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Read the data in and once read in, we can:
# run data transformations on columns 
# filter rows by conditions 
# sort data etc
medData=pd.read_csv('./csvfiles/processed.cleveland.data.csv')
medDataDf = pd.DataFrame(medData)
print(medDataDf)

# From the dataset, transform a column and save it as a new column in the
# dataframe: Ex. add a new column identifying rows with RestBP >120
medDataDf['HighRestBP']=medDataDf['RestBP'].apply(lambda x: x > 120)
# add a new column identifying rows with High or normal FBS
medDataDf['HighFBS']=medDataDf['FBS'].apply(lambda x: x == 1)
    
# Filter rows using conditions. This can be done by creating the condition 
# and generating a boolean array variable for each condition
# EX. the following 3 lines creates a boolean array, with each row having 
# a True saved if the condition is met or False if it isnt't. 
# The length of such a boolean array is equal to the total number of rows 
# in the dataframe
edf=medDataDf['RestECG'] == 2
hrBp=medDataDf['RestBP'] > 120
hFbs=medDataDf['FBS'] == 1

# Once the boolean arrays are created, they can be used singly to filter 
# rows of combined with operators like 'And' 'Or' etc 
print(medDataDf[edf & hrBp & hFbs].count())
  
# Column wise calculation of stats using functions like mean(), max() etc  
#calculate mean of all values in a column
print("Mean of Column RestBP:", medDataDf['RestBP'].mean())
#calculate max of all values in a column
print("Max value of Column RestBP:", medDataDf['RestBP'].max())
#calculate min of all values in a column
print("Min value of Column RestBP:", medDataDf['RestBP'].min())
#calculate median of all values in a column
print("Median of Column RestBP:", medDataDf['Age'].median())

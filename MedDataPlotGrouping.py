# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 11:28:40 2018

@author: Nita
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.rcParams['figure.figsize']=(20,10) # set the figure size
plt.style.use('fivethirtyeight') # using the fivethirtyeight matplotlib theme
#Set up Fonts for the text on the plot
font = {'family' : 'normal',
        'weight' : 'bold',
        'size'   : 24}
plt.rc('font', **font)

medData=pd.read_csv("C:/Users/Nita/Documents/PythonScripts/processed.cleveland.data.csv")
medDataDf = pd.DataFrame(medData)
print(medDataDf)

#Group people into Age-groups and print out counts for each group and plot a bar graph
bins =  np.arange(20,90,10)
binLabels = ['21-30','31-40', '41-50', '51-60', '61-70', '71-80']
binData=medDataDf.groupby(pd.cut(medDataDf['Age'], bins=bins, labels=binLabels)).size().reset_index(name='patient_count')
barPlot = binData.plot.bar(rot=0, color="b", figsize=(12,8))
barPlot.set_xticklabels(binLabels)
barPlot.set_ylabel('Number of Patients')


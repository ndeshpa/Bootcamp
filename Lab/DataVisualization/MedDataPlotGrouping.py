# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 11:28:40 2018

@author: Nita
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Read the data into a dataframe using Pandas
medData=pd.read_csv('./csvfiles/processed.cleveland.data.csv')
medDataDf = pd.DataFrame(medData)
print(medDataDf)

#Group people into Age-groups using bins. The arange function in numpy takes 
# the start and end of the range and increment as arguments to create bins
bins =  np.arange(20,90,10)
# set the bin labels
binLabels = ['21-30','31-40', '41-50', '51-60', '61-70', '71-80']
# the cut function slices the Age column data and assigns them to the 
# appropriate bins. This is grouped and size of each group is determined and 
# saved 'patient_count'
binData=medDataDf.groupby(pd.cut(medDataDf['Age'], bins=bins, labels=binLabels)).size().reset_index(name='patient_count')

#Set up Fonts for the text on the plot
font = {'family' : 'normal',
   'weight' : 'bold',
    'size'   : 24}
plt.rc('font', **font)

# set up the binned data and plot a bar graph
barPlot = binData.plot.bar(rot=0, color="b", figsize=(12,8))
barPlot.set_xticklabels(binLabels) # set x tick labels
barPlot.set_ylabel('Number of Patients', labelpad=15) # set y label


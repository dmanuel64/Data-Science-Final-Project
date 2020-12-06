# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 23:36:48 2020

@author: Dylan Manuel (xgk011)
"""

import storm_dat_utils as utils
import os
import matplotlib.pyplot as plt

DATA_PATH = utils.DATA_PATH + 'New York Winter Data/' # Path to New York winter data

#%% Load winter data
dataFiles = list(map(lambda name: DATA_PATH + name, os.listdir(DATA_PATH)))

winterData = utils.loadMultiCSVs(*dataFiles) # All NY winter data
utils.preprocessStormData(winterData)
# Remove any missed Unnamed columns
winterData = utils.removeUnnamedColumns(winterData)
# Filter for significant data
usefulData = utils.getUsefulData(winterData) # Data containing deaths, injuries, or damage
print(usefulData.columns)
print(usefulData.shape)
#print(usefulData.describe())
print(usefulData[['Direct Deaths', 'Indirect Deaths', 'Direct Injuries', 
          'Indirect Injuries', 'Property Damage', 'Damaged Crops']].sum())
print(usefulData['Weather Event'].unique())

#%% Plot bar
utils.barUsefulData(usefulData)
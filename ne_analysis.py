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
#%% Plot bar chart of useful data, plot useful data over time, and print summary statistics
utils.barUsefulData(usefulData, subTitle=['Injuries and Deaths From Winter Weather Events in NY (1995-2000)', 
                                          'Property and Crop Damage From Winter Weather Events in NY (1995-200)'])
# Plot injuries, deaths, and damage over time
utils.plotStatOverTime(usefulData, 'Indirect Injuries', 
                       subTitle='Indirect Injuries in NY From Winter Weather (1995-2020)', 
                       subYLabel='Number of Injuries')
utils.plotStatOverTime(usefulData, 'Direct Injuries', 
                       subTitle='Direct Injuries in NY From Winter Weather (1995-2020)', 
                       subYLabel='Number of Injuries')
utils.plotStatOverTime(usefulData, 'Direct Deaths', 
                       subTitle='Direct Deaths in NY From Winter Weather (1995-2020)', 
                       subYLabel='Number of Deaths')
utils.plotStatOverTime(usefulData, 'Indirect Deaths', 
                       subTitle='Indirect Deaths in NY From Winter Weather (1995-2020)', 
                       subYLabel='Number of Deaths')
utils.plotStatOverTime(usefulData, 'Property Damage', 
                       subTitle='Property Damage in NY From Winter Weather (1995-2020)', 
                       subYLabel='Damage ($)', logScale=True)
utils.plotStatOverTime(usefulData, 'Damaged Crops', 
                       subTitle='Damaged Crops in NY From Winter Weather (1995-2020)', 
                       subYLabel='Number of Damaged Crops', logScale=True)
# Print summary statistics
utils.printSummaryStats(usefulData, printColumns=['Weather Event', 'County'])
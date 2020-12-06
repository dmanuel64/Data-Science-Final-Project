# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 23:36:48 2020

@author: Dylan Manuel (xgk011)
"""

import storm_dat_utils as utils

DATA_PATH = utils.DATA_PATH + 'New York Snow Data/' # Path to New York snow data

#%% Load winter data
df = utils.loadMultiCSVs(DATA_PATH + 'NY_blizzards_50-20.csv', 
                         DATA_PATH + 'NY_avalanches_50-20.csv', 
                         DATA_PATH + 'NY_wind_chill_09-20.csv', 
                         DATA_PATH + 'NY_wind_chill_50-09.csv', 
                         DATA_PATH + 'NY_ex_cold_50-20.csv', 
                         DATA_PATH + 'NY_freezing_fog_50-20.csv', 
                         DATA_PATH + 'NY_ice_storm_50-20.csv')
#TODO: include sleet, frost/freeze, winter storm, and winter weather
utils.preprocessStormData(df)
# Filter for significant data
# df = df[(df['Direct Deaths'] > 0) | (df['Indirect Deaths'] > 0) | 
#         (df['Direct Injuries'] > 0) | (df['Indirect Injuries'] > 0) | 
#         (df['Damaged Crops'] > 0) | (df['Property Damage'] > 0)]
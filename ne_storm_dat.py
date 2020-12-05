# -*- coding: utf-8 -*-
"""
Created on Fri Dec  4 23:36:48 2020

@author: Dylan Manuel (xgk011)
"""

import storm_dat_utils as storm_utils

if __name__ == '__main__':
    df = storm_utils.loadMultiCSVs(storm_utils.DATA_PATH + 'sample_data.csv', 
                                   storm_utils.DATA_PATH + 'sample_data.csv', 
                                   removeDups=False)
    storm_utils.preprocessStormData(df)
    # Get the rows where the county is Midland county
    print(df[df['County'] == 'MIDLAND CO.'])
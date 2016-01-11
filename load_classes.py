# -*- coding: utf-8 -*-
"""
Created on Fri Jan 01 18:22:45 2016

@author: looper
"""

import pandas as pd
import pylab as plb

class CountrySet(object):
    ### Used as storage for data of one country

    def __init__(self, full_dataframe):
        
        full_dataframe = full_dataframe.set_index('Indicator Code')
        self.indicator_name = full_dataframe['Indicator Name']
        self.country_name = full_dataframe['Country Name'].values.all()
        
        cropped_dataframe = full_dataframe.drop(['Country Name', 'Indicator Name'], axis = 1)
        
        self.timeline = cropped_dataframe.columns
        self.df = cropped_dataframe
        
        # collect info on how many data points are present        
        counter_array = []
        
        for n in range(len(self.df)):
            
            counter_array.append(len(self.df.iloc[n].dropna()))
            
        self.data_qty = pd.Series(data=counter_array,index=self.df.index,name='Data Quantity')
        self.qty_sorted = self.data_qty.sort_values(ascending = False)
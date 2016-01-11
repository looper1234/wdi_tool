# -*- coding: utf-8 -*-
"""
Created on Fri Jan 01 18:40:28 2016

@author: looper
"""

from load_classes import CountrySet
import zipfile, gzip, cPickle, os
import pandas as pd


def load_gzip(file_loc):
    
    fp=gzip.open(file_loc,'rb')
    
    return cPickle.load(fp)
    
    fp.close()
    
    
def save_gzip(var,output_path,filename):
    
    if not os.path.isdir(output_path):
        os.makedirs(output_path)
    
    fp=gzip.open(os.path.join(output_path,filename),'wb')
    cPickle.dump(var,fp)
    
    fp.close()

# This functions is designed to take the WorldBank data file as is,
# and to crop out the relevent data sections and feed them to each CountrySet

def wdi_to_datadict(wdi_zip_loc = '.\\data\\WDI_csv.zip',output_dir = '.\\output\\data_dict.zip'):
    
    ### return data_dict containing all CountrySet classes

    data_dict = {} # result to be compressed and saved
    
    zip_handle = zipfile.ZipFile(wdi_zip_loc) # remember to close
    data_csv_handle = zip_handle.open('WDI_Data.csv') # remember to close
    
    full_df = pd.read_csv(data_csv_handle, index_col = 1)
    country_code_array = full_df.index.unique()
    
    for n in range(len(country_code_array)):
        
        key = country_code_array[n]
        partial_df = full_df.loc[key]
        
        data_dict[key] = CountrySet(partial_df)
        print data_dict[key].country_name
   
    zip_handle.close()
    data_csv_handle.close()
    
    return data_dict
    
# function to give visual clues as to the concentration of data points 
    
#def show_data_qty(data_dict):
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 01 18:53:15 2016

@author: looper
"""

#from load_classes import *
from load_functions import *

def main():
    
    data_dict = wdi_to_datadict()
    save_gzip(data_dict,'.\\data\\sorted\\','data_dict.gzip')
    pass
    
if __name__ == '__main__':
    main()
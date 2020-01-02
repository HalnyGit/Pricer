# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 18:10:10 2019

@author: Halny
"""

import numpy as np
import pandas as pd
import os
import glob
import datetime

import schedule




#getting csv filepaths from directory
pathfiles = glob.glob('..\\data\\*.csv')

filenames = []
curvenames = []
for filename in pathfiles:
    p, f = os.path.split(filename)
    filenames.append(f)
    curvenames.append(f.split('.')[0])

#reading data from csv files to particular variables
curves = {}
for i in range(len(curvenames)):
    var = curvenames[i]
    curves[var]= pd.read_csv(pathfiles[i], sep=';', decimal='.' )

#curves['pln_dep']['G'] = curves['PLN_DEP_WI']['Rate'] * curves['PLN_DEP_WI']['F']

d1=datetime.date(2020, 1, 2)
d2=datetime.date(2021, 1, 2)
s1 = Schedule(d1, d2, 'pln', 3)
print(s1.dates_table)
print(get_eom(d1))


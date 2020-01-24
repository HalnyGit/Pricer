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

from schedule import *

INIT_DATE = datetime.date.today()

currencies = {'pln', 'eur', 'usd'}

#getting csv filepaths from directory
pathfiles = glob.glob('..\\data\\*.csv')

filenames = []
curvenames = []
for filename in pathfiles:
    p, f = os.path.split(filename)
    filenames.append(f)
    curvenames.append(f.split('.')[0])

#reading data from csv files, curve indexing
curves = {}
for i in range(len(curvenames)):
    var = curvenames[i]
    curves[var]= pd.read_csv(pathfiles[i], sep=';', decimal='.' )

#curves['pln_irs_6m']['start_date'] = curves['pln_irs_6m']['TENOR'].apply(lambda x: calc_period(datetime.date(2020, 1, 22), 'pln', 'pln', 'pln', x)[0])
#curves['pln_irs_6m']['end_date'] = curves['pln_irs_6m']['TENOR'].apply(lambda x: calc_period(datetime.date(2020, 1, 22), 'pln', 'pln', 'pln', x)[1])
#curves['pln_dep']['G'] = curves['PLN_DEP_WI']['Rate'] * curves['PLN_DEP_WI']['F']

for curve_name in curves.keys():
    ccy1, ccy2, *rest = curve_name.split('_')
    if ccy2 not in currencies:
        curves[curve_name]['ccy_1']=ccy1
        curves[curve_name]['start_date'] = curves[curve_name]['TENOR'].apply(lambda x: calc_period(INIT_DATE, ccy1, ccy1, ccy1, x)[0])
        curves[curve_name]['end_date'] = curves[curve_name]['TENOR'].apply(lambda x: calc_period(INIT_DATE, ccy1, ccy1, ccy1, x)[1])
    else:
        curves[curve_name]['ccy_1']=ccy1
        curves[curve_name]['ccy_2']=ccy2
        curves[curve_name]['start_date'] = curves[curve_name]['TENOR'].apply(lambda x: calc_period(INIT_DATE, ccy1, ccy1, (ccy1, ccy2), x)[0])
        curves[curve_name]['end_date'] = curves[curve_name]['TENOR'].apply(lambda x: calc_period(INIT_DATE, ccy1, ccy1, (ccy1, ccy2), x)[1])


#Estimation curves
        
#pln_ibor_3m
#pln_fra_3m_1x4
#pln_fra_3m_2x5
      
        
#discounting curves




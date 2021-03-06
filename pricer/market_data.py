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
market_rates = {}
for i in range(len(curvenames)):
    var = curvenames[i]
    market_rates[var]= pd.read_csv(pathfiles[i], sep=';', decimal='.' )

#curves['pln_irs_6m']['start_date'] = curves['pln_irs_6m']['TENOR'].apply(lambda x: calc_period(datetime.date(2020, 1, 22), 'pln', 'pln', 'pln', x)[0])
#curves['pln_irs_6m']['end_date'] = curves['pln_irs_6m']['TENOR'].apply(lambda x: calc_period(datetime.date(2020, 1, 22), 'pln', 'pln', 'pln', x)[1])
#curves['pln_dep']['G'] = curves['PLN_DEP_WI']['Rate'] * curves['PLN_DEP_WI']['F']


for curve_name in market_rates.keys():
    market_rates[curve_name]['instrument'] = curve_name
    ccy1, ccy2, *rest = curve_name.split('_')
    if ccy2 not in currencies:
        market_rates[curve_name]['ccy_1']=ccy1
        market_rates[curve_name]['start_date'] = market_rates[curve_name]['TENOR'].apply(lambda x: calc_period(INIT_DATE, ccy1, ccy1, ccy1, x)[0])
        market_rates[curve_name]['end_date'] = market_rates[curve_name]['TENOR'].apply(lambda x: calc_period(INIT_DATE, ccy1, ccy1, ccy1, x)[1])
    else:
        market_rates[curve_name]['ccy_1']=ccy1
        market_rates[curve_name]['ccy_2']=ccy2
        market_rates[curve_name]['start_date'] = market_rates[curve_name]['TENOR'].apply(lambda x: calc_period(INIT_DATE, ccy1, ccy1, (ccy1, ccy2), x)[0])
        market_rates[curve_name]['end_date'] = market_rates[curve_name]['TENOR'].apply(lambda x: calc_period(INIT_DATE, ccy1, ccy1, (ccy1, ccy2), x)[1])

#df2['Population'] = df2.apply(lambda x: df1.loc[x['Year'] == df1['Year'], x['State']].reset_index(drop=True), axis=1)

#label='pln_ois'
#market_rates[label][market_rates[label]['TENOR']=='1w']['start_date'][0]
#market_rates['pln_ois'].loc[market_rates['pln_ois']['TENOR']=='2w', 'MID']
#Estimation curves
        
#pln_ibor_3m
#pln_fra_3m_1x4
#pln_fra_3m_2x5
      
        
#curves structures 

c_structures={'pln_lch_disc':(['pln_ois','1w', 'act365'],
                               ['pln_ois','1m', 'act365'],
                               ['pln_ois','2m', 'act365'],
                               ['pln_ois','3m', 'act365'],
                               ['pln_fra_3m', '3x6', 'act365'],
                               ['pln_fra_3m', '6x9', 'act365'],
                               ['pln_fra_3m', '9x12','act365' ],
                               ['pln_irs_6m','2y', 'actact'],
                               ['pln_irs_6m','3y', 'actact'],
                               ['pln_irs_6m','4y', 'actact'],
                               ['pln_irs_6m','5y', 'actact'],
                               ['pln_irs_6m','6y', 'actact'],
                               ['pln_irs_6m','7y', 'actact'],
                               ['pln_irs_6m','8y', 'actact'],
                               ['pln_irs_6m','9y', 'actact'],
                               ['pln_irs_6m','10y', 'actact'],
                               ['pln_irs_6m','12y', 'actact'],
                               ['pln_irs_6m','20y', 'actact']
                               )
    }


class CurveBuilder(object):
    
    def __init__(self, structure):
        self.structure = structure
        curve_base_frame = pd.DataFrame(c_structures[self.structure], columns=['instrument', 'tenor', 'base']) 
        temp_1 = [market_rates[x] for x in set(curve_base_frame['instrument'])]
        temp_2 = [curve_base_frame.merge(x, left_on=['tenor', 'instrument'], right_on=['TENOR', 'instrument']) for x in temp_1]
        self.curve = pd.concat(temp_2, ignore_index=True).drop(columns=['TENOR']).sort_values(by='end_date')
        
        
        
        
d1 = datetime.date(2020, 2, 21)
d2 = datetime.date(2020, 3, 23)
x = getattr(schedule, 'dcf_act365')(d1, d2)        
        
        
        
        
        
    
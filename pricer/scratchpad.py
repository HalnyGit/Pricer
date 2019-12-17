# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 21:01:50 2019

@author: Komp
"""

import pandas as pd
import numpy as np
import datetime

def is_leap(d):
    '''
    d: date
    return: True if year of the date 'd' is leap, False otherwise
    '''
    try:
        datetime.date(d.year, 2, 29)
    except:
        return False
    return True

def days_between(d1, d2):
    '''
    d1: date
    d2: date
    return: integer, number of days between dates d1 and d2
    '''
    return (d2 - d1) / datetime.timedelta(days=1)


def dcf_actact(d1, d2):
    '''
    d1: date, d2: date
    return: day count fraction in ACT/ACT ISDA convention
    '''
    base1=366 if is_leap(d1) else 365
    base2=366 if is_leap(d2) else 365
    eoy = datetime.date(d1.year, 12, 31)
    return (((days_between(d1, eoy) + 1) / base1) + ((days_between(eoy, d2) - 1) / base2))




dates = {'A':[datetime.date(2019, 11, 15), datetime.date(2019, 12, 15)],
         'B':[datetime.date(2020, 11, 15), datetime.date(2020, 12, 15)]     
        }

df = pd.DataFrame(dates)

df['C'] = df['A'].apply(lambda x: x - datetime.timedelta(days=1))
df['D'] = (df['B'] - df['A']) / datetime.timedelta(days=1)

t=[]
for i in range(len(df['A'])):
    n = dcf_actact(df['A'][i], df['B'][i])
    t.append(n)



df['E'] = df.apply(lambda x: dcf_actact(x['A'], x['B']), axis=1)


df['F'] = dcf_actact(df['A'], df['B'])
    

# =============================================================================
# 
# 
# 
# weekmask_pd = 'Mon Tue Wed Thu Fri'
# holidays_pd = ['2019-11-15', '2019-12-09', '2019-12-13', '2020-02-01']
# bday_pd = pd.offsets.CustomBusinessDay(holidays=holidays_pd, weekmask=weekmask_pd, offset=datetime.timedelta(weeks=1))
# start_date = pd.Timestamp('2019-11-13')
# end_date = pd.Timestamp('2020-11-13')
# 
# #dts = pd.bdate_range(start_date, end_date, freq=(bday_pd))
# dts = pd.bdate_range(start_date, end_date, freq=bday_pd)
# dts
# 
# dts2 = pd.bdate_range(start_date, end_date, freq='CBMS', weekmask=weekmask_pd, holidays=holidays_pd) + pd.offsets.Day(start_date.day-1)
# dts2
# 
# dts3 = pd.bdate_range(start_date, end_date, freq='CBMS', weekmask=weekmask_pd, holidays=holidays_pd)+ datetime.timedelta(days=start_date.day-1)
# dts3
# 
# dts3 = pd.bdate_range(start_date, end_date, freq='CBMS+{}'.format(start_date.day), weekmask=weekmask_pd, holidays=holidays_pd)
# dts3
# 
# dts4 = pd.bdate_range(start_date, end_date, freq='11SMS', weekmask=weekmask_pd, holidays=holidays_pd)
# dts4
# 
# dts5 = pd.date_range(start_date, end_date,freq='1SMS+13')
# dts5
# 
# =============================================================================

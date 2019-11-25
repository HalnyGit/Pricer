# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 21:01:50 2019

@author: Komp
"""

import pandas as pd
import numpy as np
import datetime


weekmask_pd = 'Mon Tue Wed Thu Fri'
holidays_pd = ['2019-11-15', '2019-12-09', '2019-12-13', '2020-02-01']
bday_pd = pd.offsets.CustomBusinessDay(holidays=holidays_pd, weekmask=weekmask_pd, offset=datetime.timedelta(weeks=1))
start_date = pd.Timestamp('2019-11-13')
end_date = pd.Timestamp('2020-11-13')

#dts = pd.bdate_range(start_date, end_date, freq=(bday_pd))
dts = pd.bdate_range(start_date, end_date, freq=bday_pd)
dts

dts2 = pd.bdate_range(start_date, end_date, freq='CBMS', weekmask=weekmask_pd, holidays=holidays_pd) + pd.offsets.Day(start_date.day-1)
dts2

dts3 = pd.bdate_range(start_date, end_date, freq='CBMS', weekmask=weekmask_pd, holidays=holidays_pd)+ datetime.timedelta(days=start_date.day-1)
dts3

dts3 = pd.bdate_range(start_date, end_date, freq='CBMS+{}'.format(start_date.day), weekmask=weekmask_pd, holidays=holidays_pd)
dts3

dts4 = pd.bdate_range(start_date, end_date, freq='11SMS', weekmask=weekmask_pd, holidays=holidays_pd)
dts4

dts5 = pd.date_range(start_date, end_date,freq='1SMS+13')
dts5

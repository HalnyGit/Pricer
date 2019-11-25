# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 11:25:59 2019

@author: Halny
"""
import numpy as np
import pandas as pd
import datetime
import os

#some test lines
print(os.getcwd())
os.listdir('..\\data')


#reading holidays from csv files and making dictionary of holidays{ccy:[dates]}
holiday_paths = [os.path.join('..\\holidays', file) for file in os.listdir('..\\holidays') if file.endswith('.csv')]

hol_df = pd.DataFrame()
for i in range(len(holiday_paths)):
    data = pd.read_csv(holiday_paths[i])
    ccy = list(data.columns)[0]
    try:
        data[ccy] = pd.to_datetime(data[ccy], format='%Y-%m-%d')
    except:
        data[ccy] = pd.to_datetime(data[ccy], format='%d-%m-%Y')
    hol_df=pd.concat([hol_df, data], axis=1)

holidays = hol_df.to_dict('list')
#overwrite holidays dict for testing only
#holidays={'pln':[datetime.date(2020, 2, 3),
#            datetime.date(2021, 3, 1),
#            datetime.date(2020, 2, 28) ]}
    
#non working days dictionary {ccy:[1-Mon, ..., 7-Sun]}
non_working_days={'pln':[6, 7]}

#number of days to start and end from today for particular currency
dse={'pln':{'on':(0, 1),
         'tn':(1, 2),
         'sn':(2, 3),
         'w':(2,),
         'm':(2,),
         'q':(2,),
         'y':(2,)}
}

def calc_period(calc_date, ccy='', period='', hol=None):
    '''calc_date: date, calculation date
       ccy: string, (eg. pln, usd)
       period: string, (possible entries: on, tn, sn, iw, im, iq, iy,
               where i is integral eg 3w, 2m, 3q, 5y)
       hol: list of dates that represent holidays 
       returns: tuple of dates that represent start date and end date
               for given period an currency
    '''
    assert isinstance(calc_date, datetime.date), 'calc_date must be a date'
     
    if (period=='on' or period=='tn' or period=='sn'):
        start_date=calc_date + datetime.timedelta(days=dse[ccy][period][0])
        end_date=calc_date + datetime.timedelta(days=dse[ccy][period][1])

    p1=int(period[:-1])
    p2=period[len(period)-1:]
    
    if p2=='w':
        start_date=calc_date + datetime.timedelta(days=dse[ccy][p2][0])
        end_date=start_date + datetime.timedelta(weeks=p1)
    else:
        start_date=calc_date + datetime.timedelta(days=dse[ccy][p2][0])
        if p2=='m':
            mi = (start_date.month + p1) % 12
            yi = (start_date.month + p1) // 12
            end_date=(start_date.year + yi, mi, start_date.day)
        elif p2=='q':
            mi = (start_date.month + 3 * p1) % 12
            yi = (start_date.month + 3 * p1) // 12
            end_date=(start_date.year + yi, mi, start_date.day)
    
    return(start_date, end_date)


d = datetime.date(2020, 1, 31)
h1 = datetime.date(2020, 2, 3)
h2 = datetime.date(2021, 3, 1)
h3 = datetime.date(2020, 2, 28)

def move_date_by_days(init_date, roll=1, nwd_key='pln', hol_key='pln'):
    nwd = non_working_days.get(nwd_key, [])
    hol = holidays.get(hol_key,[])
    moved_date = init_date + datetime.timedelta(days=roll)
    if (moved_date.isoweekday() in nwd) or (moved_date in hol):
        if roll >= 0:
            moved_date=move_date_by_days(init_date + datetime.timedelta(days=1), roll=roll, nwd_key=nwd_key, hol_key=hol_key)
        else:
            moved_date=move_date_by_days(init_date + datetime.timedelta(days=-1), roll=roll, nwd_key=nwd_key, hol_key=hol_key)
    return moved_date
#test        
#move_date_by_days(d, 1)

def move_date_by_month_following(init_date, roll=1, nwd_key='pln', hol_key='pln', conv=None):
    n_month = (init_date.month + roll) % 12
    if n_month==0: n_month=12
    n_year = (init_date.month + roll)
    n_year = 0 if n_year == 12 else ((init_date.month + roll) // 12)
    try:
        moved_date=datetime.date(init_date.year + n_year, n_month, init_date.day)
    except:
        moved_date=move_date_by_month_following(init_date + datetime.timedelta(days=1), roll)
    moved_date=move_date_by_days(moved_date + datetime.timedelta(days=-1), roll=1, nwd_key=nwd_key, hol_key=hol_key) 
    return moved_date
#test
#move_date_by_month_following(d, 12)

def move_date_by_month_preceding(init_date, roll=1, nwd_key='pln', hol_key='pln', conv=None):   
    n_month = (init_date.month + roll) % 12
    if n_month==0: n_month=12
    n_year = (init_date.month + roll)
    n_year = 0 if n_year == 12 else ((init_date.month + roll) // 12)    
    try:
        moved_date=datetime.date(init_date.year + n_year, n_month, init_date.day)
    except:
        moved_date=move_date_by_month_preceding(init_date + datetime.timedelta(days=-1), roll)
    moved_date=move_date_by_days(moved_date + datetime.timedelta(days=1), roll=-1, nwd_key=nwd_key, hol_key=hol_key) 
    return moved_date

d = datetime.date(2020, 3, 31)
#test
#move_date_by_month_following(d, 1)
#move_date_by_month_preceding(d, 1)

def move_date_by_month_modfoll(init_date, roll=1, nwd_key='pln', hol_key='pln', conv=None):
    preceding_date = move_date_by_month_preceding(init_date, roll=roll, nwd_key=nwd_key, hol_key=hol_key)
    following_date = move_date_by_month_following(init_date, roll=roll, nwd_key=nwd_key, hol_key=hol_key)
    print(preceding_date, following_date)
    moved_date=preceding_date if following_date.month>preceding_date.month else following_date
    return moved_date

#test
#move_date_by_month_modfoll(d, 1)

# exampple of getattr
class Switcher(object):
    def indirect(self,i):
        method_name='number_'+str(i)
        method=getattr(self,method_name,lambda:'Invalid')
        return method()
    def number_0(self):
        return 'zero'
    def number_1(self):
        return 'one'
    def number_2(self):
        return 'two'

s=Switcher()
s.indirect(2)

def last_day_of_month(any_day):
    next_month = any_day.replace(day=28) + datetime.timedelta(days=4)  # this will never fail
    return next_month - datetime.timedelta(days=next_month.day)

#test
#last_day_of_month(d)

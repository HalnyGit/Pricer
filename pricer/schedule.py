# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 11:25:59 2019

@author: Halny
"""
import numpy as np
import pandas as pd
import datetime
import os

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
non_working_days={'pln':[6, 7], 
                  'eur':[6, 7], 
                  'usd':[6, 7]
                  }

#number of days to start and end from today for particular currency
dse={'pln':{'on':(0, 1),
         'tn':(1, 2),
         'sn':(2, 3),
         'w':(2,),
         'm':(2,),
         'q':(2,),
         'y':(2,)}
}

#some dates for testing purpose only
d = datetime.date(2020, 1, 31)
h1 = datetime.date(2020, 2, 3)
h2 = datetime.date(2021, 3, 1)
h3 = datetime.date(2020, 11, 28)

def get_eom(init_date):
    '''
    init_date: date
    return: date, last day of month of init_date
    '''
    temp_date = init_date.replace(day=28) + datetime.timedelta(days=4)
    return temp_date - datetime.timedelta(days=temp_date.day)
    
#test
#get_eom(h3)
    
def get_weom(init_date, nwd_key=None, hol_key=None):
    '''
    init_date: date
    return: date, last working day of month of init_date
    '''
    eom_date = get_eom(init_date)
    weom = move_date_by_days(eom_date + datetime.timedelta(days=1), roll=-1, nwd_key=nwd_key, hol_key=hol_key)
    return weom

#test
#get_weom(datetime.date(2020, 2, 28), 'pln', 'pln')

def is_eom(init_date):
    '''
    init_date: date
    return: boolean, True if init_date is the last day of month
    '''
    return init_date == get_eom(init_date)

#test
#is_eom(h3)

def is_weom(init_date, nwd_key=None, hol_key=None):
    '''
    init_date: date
    return: boolean, True if init_date is last working day of month
    '''
    return init_date == get_weom(init_date, nwd_key=nwd_key, hol_key=hol_key)

#test
#is_weom(datetime.date(2020, 2, 29), nwd_key='pln')

def move_date_by_days(init_date, roll=1, nwd_key=None, hol_key=None):
    '''
    moves date by n-number of working days forward or backward
    init_date: date, initial caluclation date
    roll: integer, number of days to move forward (+) or backward (-)
    nwd_key: string that stands for currency iso code, it is a key in non_working_days dictionary
    hol_key: string that stands for currency iso code, it is a key in holidays dictonary
    return: date
    '''
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
#move_date_by_days(d, 1, 'pln', 'pln')
#move_date_by_days(datetime.date(2020, 1, 6), -1, 'pln', 'pln')   

def mdbm_calendar(init_date, roll=1):
    '''
    moves date by n-number of months forward or backward
    init_date: date, initial caluclation date
    roll: integer, number of months the init_date will be rolled forward (+) or backward(-)
    return: date
    '''
    n_month = (init_date.month + roll) % 12
    if n_month==0: n_month=12
    n_year = (init_date.month + roll)    
    
    if roll >= 0:
        n_year = 0 if n_year == 12 else ((init_date.month + roll) // 12)    
    else:
        n_year = -1 if n_year == 0 else ((init_date.month + (roll-1)) // 12) 
    
    try:
        moved_date=datetime.date(init_date.year + n_year, n_month, init_date.day)
    except:
        moved_date=mdbm_preceding(init_date + datetime.timedelta(days=-1), roll=roll)
    
    return moved_date

#test
#mdbm_calendar(datetime.date(2019, 3, 31), -1)

def mdbm_following(init_date, roll=1, nwd_key=None, hol_key=None):
    '''
    moves date by n-number of months forward or backward, if moved date is weekend or holiday
    it is moved to next working day
    init_date: date
    roll: integer, number of months the init_date will be rolled forward (+) or backward(-)
    nwd_key: string that stands for currency iso code, it is a key in non_working_days dictionary
    hol_key: string that stands for currency iso code, it is a key in holidays dictonary
    the function does not comply end-end rule: 31/01 + 1 month => 01/03 as there is no 31/02
    return: date
    '''
    n_month = (init_date.month + roll) % 12
    if n_month==0: n_month=12
    n_year = (init_date.month + roll)    
    if roll >= 0:
        n_year = 0 if n_year == 12 else ((init_date.month + roll) // 12)    
    else:
        n_year = -1 if n_year == 0 else ((init_date.month + (roll-1)) // 12) 
    
    try:
        moved_date=datetime.date(init_date.year + n_year, n_month, init_date.day)
    except:
        moved_date=mdbm_following(init_date + datetime.timedelta(days=1), roll)
    moved_date=move_date_by_days(moved_date + datetime.timedelta(days=-1), roll=1, nwd_key=nwd_key, hol_key=hol_key) 
    return moved_date

#test   
#mdbm_following(datetime.date(2020, 3, 31), -1, 'pln', 'pln')


def mdbm_preceding(init_date, roll=1, nwd_key=None, hol_key=None):
    '''
    moves date by n-number of months forward or backward, if moved date is weekend or holiday
    it is moved to preceding working day
    init_date: date
    roll: integer, number of months the init_date will be rolled forward (+) or backward(-)
    nwd_key: string that stands for currency iso code, it is a key in non_working_days dictionary
    hol_key: string that stands for currency iso code, it is a key in holidays dictonary
    the function does not comply end-end rule: 29/02 + 1 month => 29/03, not 31/03
    return: date
    '''
    n_month = (init_date.month + roll) % 12
    if n_month==0: n_month=12
    n_year = (init_date.month + roll)    
    if roll >= 0:
        n_year = 0 if n_year == 12 else ((init_date.month + roll) // 12)    
    else:
        n_year = -1 if n_year == 0 else ((init_date.month + (roll-1)) // 12)   
    try:
        moved_date=datetime.date(init_date.year + n_year, n_month, init_date.day)
    except:
        moved_date=mdbm_preceding(init_date + datetime.timedelta(days=-1), roll)
    moved_date=move_date_by_days(moved_date + datetime.timedelta(days=1), roll=-1, nwd_key=nwd_key, hol_key=hol_key) 
    return moved_date

#test
#mdbm_preceding(datetime.date(2020, 2, 29), -1, 'pln', 'pln')

def mdbm_eom(init_date, roll=1):
    '''
    moves date by n-number of months forward or backward to the end of the new month irrespectively of working days 
    init_date: date
    roll: integer, number of months the init_date will be rolled forward (+) or backward(-)
    the function complies end-end rule: 29/02 + 1 month => 31/03
    return: date
    '''
    moved_date = mdbm_preceding(init_date, roll)
    return get_eom(moved_date)

#test
#mdbm_end_end(h3, 12)
    
def mdbm_eom_following(init_date, roll=1, nwd_key=None, hol_key=None):    
    '''
    moves date by n-number of months forward or backward to the end of the new month taking into account working days
    init_date: date
    roll: integer, number of months the init_date will be rolled forward (+) or backward(-)
    the function complies end-end rule: 29/02 + 1 month => 31/03
    return: date
    '''
    moved_date = mdbm_eom(init_date, roll)
    return move_date_by_days(moved_date, 0, nwd_key, hol_key)

#test
#mdbm_eom_following(datetime.date(2019, 12, 6), 1, 'usd', 'usd')
#mdbm_eom_following(datetime.date(2020, 1, 31), 1, 'pln', 'pln')
#mdbm_eom_following(datetime.date(2020, 2, 29), 1, 'pln', 'pln')  
   
def mdbm_modified_following(init_date, roll=1, nwd_key=None, hol_key=None):
    '''
    moves date by n-number of months forward or backward, if moved date is weekend or holiday
    it is moved according to modified following convention
    init_date: date
    roll: integer, number of months the init_date will be rolled forward (+) or backward(-)
    nwd_key: string that stands for currency iso code, it is a key in non_working_days dictionary
    hol_key: string that stands for currency iso code, it is a key in holidays dictonary
    the function complies end-end rule: 29/02 + 1 month => 31/03
    '''
    if is_weom(init_date):
        moved_date = mdbm_preceding(init_date, roll, nwd_key, hol_key)
        return get_weom(moved_date, nwd_key, hol_key)
    
    n_month = (init_date.month + roll) % 12
    if n_month == 0: n_month = 12
    n_year = (init_date.month + roll)    
    if roll >= 0:
        n_year = 0 if n_year == 12 else ((init_date.month + roll) // 12)    
    else:
        n_year = -1 if n_year == 0 else ((init_date.month + (roll-1)) // 12)   
    try:
        moved_date = datetime.date(init_date.year + n_year, n_month, init_date.day)
        md_pre = move_date_by_days(moved_date + datetime.timedelta(days=1), -1, nwd_key, hol_key)
        md_fol = move_date_by_days(moved_date, 0, nwd_key, hol_key)
    except:
        md_pre = mdbm_preceding(init_date + datetime.timedelta(days=-1), roll, nwd_key, hol_key)
        md_fol = mdbm_following(init_date + datetime.timedelta(days=1), roll, nwd_key, hol_key)
    if md_fol.month != md_pre.month:
        moved_date = md_pre
    else:
        moved_date = md_fol    
    return moved_date

#test
#mdbm_modified_following(datetime.date(2019, 12, 6), 1, 'usd', 'usd')
#mdbm_modified_following(datetime.date(2020, 1, 31), 1, 'pln', 'pln')
#mdbm_modified_following(datetime.date(2020, 2, 29), 1, 'pln', 'pln')
    
def days_between(d1, d2):
    '''
    d1: date
    d2: date
    return: integer, number of days between dates d1 and d2
    '''
    return (d2 - d1) / datetime.timedelta(days=1)

def is_leap(d):
    '''
    date
    return: True if year of the date 'd' is leap, False otherwise
    '''
    try:
        datetime.date(d.year, 2, 29)
    except:
        return False
    return True

def dcf_act365(d1, d2):
    '''
    d1: date, d2: date
    return: day count fraction in ACT365 convention
    '''
    return days_between(d1, d2)/365

def dcf_actact(d1, d2):
    '''
    d1: date, d2: date
    return: day count fraction in ACT/ACT ISDA convention
    '''
    base1=366 if is_leap(d1) else 365
    base2=366 if is_leap(d2) else 365
    eoy = datetime.date(d1.year, 12, 31)
    return (((days_between(d1, eoy) + 1) / base1) + ((days_between(eoy, d2) - 1) / base2))
    

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



class Schedule(object):
    CONVENTIONS = {'calendar', 'following', 'preceding', 'eom', 'eom_following', 
                       'modified_following'}
    def __init__(self, start=None, end=None, ccy=None, roll=None, convention='calendar', stub=None, pay_shift=None, dcf='act365'):
        '''
        start: date
        end: date
        ccy: string, iso currency code (eg 'usd', 'eur')
        roll: integer, number of month the interest periods will roll
        convention: string, one of the values from CONVENTIONS set
        stub: date
        pay_shift: tuple (integer, string), integer specifies number of days the payment date needs to be shifted +/- from start or end date
                          string: 'start_date' or 'end_date' represents the date from which payment date shall be deduced
                          if pay_shift=None then payment date equals end date
        dcf: string, day count factor
        self.dates_table: is DataFrame that consist of interest periods meaning, start dates, end dates, fixing dates and payment dates                
        '''
        self.start = start
        self.end = end
        self.ccy = ccy
        self.roll = roll
        self.stub = stub
        self.pay_shift = pay_shift
        self.convention = convention
        self.dcf = dcf
        if self.convention not in self.CONVENTIONS:
            raise ValueError ('\"{0}\" is not valid convention, available conventions are: {1}'.format(self.convention, self.CONVENTIONS))
    
        i = 1
        dates = [self.start]
        if self.stub != None:
            dates.append(self.stub)
            roll_date = self.stub
        else:
            roll_date = self.start
        while dates[-1] < self.end:
            if self.convention == 'calendar':
                next_date = mdbm_calendar(roll_date, self.roll * i)
            if self.convention == 'following':
                next_date = mdbm_following(roll_date, self.roll * i, self.ccy, self.ccy)
            if self.convention == 'preceding':
                next_date = mdbm_preceding(roll_date, self.roll * i, self.ccy, self.ccy)
            if self.convention == 'eom':
                next_date = mdbm_eom(roll_date, self.roll * i)
            if self.convention == 'eom_following':
                next_date = mdbm_eom_following(roll_date, self.roll * i, self.ccy, self.ccy)
            if self.convention == 'modified_following':
                next_date = mdbm_modified_following(roll_date, self.roll * i, self.ccy, self.ccy)
            if next_date < self.end:
                dates.append(next_date)
            else:
                dates.append(self.end)        
            i += 1
        
        self.dates = dates
        self.start_dates = self.dates[:-1]
        self.end_dates = self.dates[1:]
        days_to_spot = dse[self.ccy]['sn'][0]
        #self.fixing_dates = [move_date_by_days(d, -days_to_spot, self.ccy, self.ccy ) for d in self.start_dates]
        temp_data = {'start_date':self.start_dates,
                     'end_date':self.end_dates}
        self.dates_table = pd.DataFrame(temp_data)
        self.dates_table['fixing_date'] = self.dates_table['start_date'].apply(lambda x: move_date_by_days(x, -days_to_spot, self.ccy, self.ccy))
        if self.pay_shift == None:
            self.dates_table['payment_date'] = self.dates_table['end_date']
        else:
            self.dates_table['payment_date'] = self.dates_table[self.pay_shift[0]].apply(lambda x: move_date_by_days(x, self.pay_shift[1], self.ccy, self.ccy))

        #self.dates_table['start_date'] = (self.dates_table['start_date']).astype('datetime64[ns]')
        #self.dates_table['end_date']= (self.dates_table['end_date']).astype('datetime64[ns]')
                
        if self.dcf == 'act365':
            self.dates_table['dcf'] = dcf_act365(self.dates_table['start_date'], self.dates_table['end_date'])
        elif self.dcf == 'actact':
            self.dates_table['dcf'] = self.dates_table.apply(lambda x: dcf_actact(x['start_date'],  x['end_date']), axis=1)

    def get_dates(self):
        return self.dates
    
    def get_start_dates(self):
        return self.start_dates
    
    def get_end_dates(self):
        return self.end_dates
    
    def get_dates_table(self):
        return self.dates_table
    
    


      

        
    
     


            



# not connected to the rest of this script
# some exampple of using getattr
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

#test
#s=Switcher()
#s.indirect(2)



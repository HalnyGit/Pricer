# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 10:45:20 2019

@author: 115095
"""

import unittest
import datetime
import schedule

d1 = datetime.date(2020, 1, 31)
d2 = datetime.date(2021, 1, 1)
d3 = datetime.date(2021, 3, 1)
d4 = datetime.date(2020, 2, 28)


#move_date_by_days(init_date, roll=1, nwd_key='pln', hol_key='pln')

class TestSchedule(unittest.TestCase):
    
    def test_move_date_by_days(self):
        # checks if rolling forward ok
        self.assertEqual(move_date_by_days(d1, roll=1), datetime.date(2020, 2, 3))
        self.assertEqual(move_date_by_days(d1, roll=8), datetime.date(2020, 2, 10))
        self.assertEqual(move_date_by_days(d1, roll=31), datetime.date(2020, 3, 2))
        
        #checks if rolling over holidays ok
        self.assertEqual(move_date_by_days(d1, roll=73), datetime.date(2020, 4, 14))
        
        #checks if rolling over year end ok
        self.assertEqual(move_date_by_days(d1, roll=365), datetime.date(2021, 2, 1))
        self.assertEqual(move_date_by_days(d1, roll=367), datetime.date(2021, 2, 1))
        
        #checks if rolling backward ok
        self.assertEqual(move_date_by_days(d1, roll=-1), datetime.date(2020, 1, 30))
        self.assertEqual(move_date_by_days(d1, roll=-5), datetime.date(2020, 1, 24))
        
        #checks if rolling backward over weekends
        self.assertEqual(move_date_by_days(d1, roll=-62), datetime.date(2019, 11, 29))
        
        #checks if rolling backward over year end ok
        self.assertEqual(move_date_by_days(d1, roll=-365), datetime.date(2019, 1, 31))
        self.assertEqual(move_date_by_days(d2, roll=-366), datetime.date(2019, 12, 31))

if __name__ == '__main__':
    unittest.main()
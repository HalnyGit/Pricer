# -*- coding: utf-8 -*-
"""
Created on Mon Nov 25 10:45:20 2019

@author: 115095
"""

import unittest
import datetime
import sys
sys.path.append('..\\pricer\\')

from schedule import *

d1 = datetime.date(2020, 1, 31)
d2 = datetime.date(2021, 1, 1)
d3 = datetime.date(2021, 3, 1)
d4 = datetime.date(2020, 2, 28)
d5 = datetime.date(2020, 2, 29)
d6 = datetime.date(2023, 1, 31)

class TestSchedule(unittest.TestCase):
    
    def test_move_date_by_days(self):
        # checks if rolling forward ok
        self.assertEqual(move_date_by_days(d1, 1, 'pln', 'pln'), datetime.date(2020, 2, 3))
        self.assertEqual(move_date_by_days(d1, 8, 'pln', 'pln'), datetime.date(2020, 2, 10))
        self.assertEqual(move_date_by_days(d1, 31, 'pln', 'pln'), datetime.date(2020, 3, 2))
        
        #checks if rolling over holidays ok
        self.assertEqual(move_date_by_days(d1, 73, 'pln', 'pln'), datetime.date(2020, 4, 14))
        self.assertEqual(move_date_by_days(d2, 5, 'pln', 'pln'), datetime.date(2021, 1, 7))
        self.assertEqual(move_date_by_days(d2, 5, 'usd', 'usd'), datetime.date(2021, 1, 6))
        
        #checks if rolling over year end ok
        self.assertEqual(move_date_by_days(d1, 365, 'pln', 'pln'), datetime.date(2021, 2, 1))
        self.assertEqual(move_date_by_days(d1, 367, 'pln', 'pln'), datetime.date(2021, 2, 1))
        
        #checks if rolling backward ok
        self.assertEqual(move_date_by_days(d1, -1, 'pln', 'pln'), datetime.date(2020, 1, 30))
        self.assertEqual(move_date_by_days(d1, -5, 'pln', 'pln'), datetime.date(2020, 1, 24))
        
        #checks if rolling backward over weekends
        self.assertEqual(move_date_by_days(d1, -62, 'pln', 'pln'), datetime.date(2019, 11, 29))
        
        #checks if rolling backward over year end ok
        self.assertEqual(move_date_by_days(d1, -365, 'pln', 'pln'), datetime.date(2019, 1, 31))
        self.assertEqual(move_date_by_days(d2, -366, 'pln', 'pln'), datetime.date(2019, 12, 31))

    def test_mdbm_calendar(self):
        # checks if rolling forward ok
        self.assertEqual(mdbm_calendar(d1, 1), datetime.date(2020, 2, 29))
        self.assertEqual(mdbm_calendar(d1, 3), datetime.date(2020, 4, 30))
        self.assertEqual(mdbm_calendar(d1, 6), datetime.date(2020, 7, 31))
        self.assertEqual(mdbm_calendar(d1, 11), datetime.date(2020, 12, 31))
        self.assertEqual(mdbm_calendar(d1, 12), datetime.date(2021, 1, 31))
        self.assertEqual(mdbm_calendar(d1, 13), datetime.date(2021, 2, 28))
        self.assertEqual(mdbm_calendar(d1, 24), datetime.date(2022, 1, 31))
        self.assertEqual(mdbm_calendar(d1, 25), datetime.date(2022, 2, 28))
        
        #checks if rolling over holidays ok
        self.assertEqual(mdbm_calendar(datetime.date(2019, 12, 6), 1), datetime.date(2020, 1, 6))

        #checks if rolling backward ok
        self.assertEqual(mdbm_calendar(d1, -1), datetime.date(2019, 12, 31))
        self.assertEqual(mdbm_calendar(d1, -3), datetime.date(2019, 10, 31))
        self.assertEqual(mdbm_calendar(d1, -6), datetime.date(2019, 7, 31))
        self.assertEqual(mdbm_calendar(d1, -11), datetime.date(2019, 2, 28))
        self.assertEqual(mdbm_calendar(d1, -12), datetime.date(2019, 1, 31))
        self.assertEqual(mdbm_calendar(d1, -13), datetime.date(2018, 12, 31))
        self.assertEqual(mdbm_calendar(d1, -24), datetime.date(2018, 1, 31))
        self.assertEqual(mdbm_calendar(d6, -25), datetime.date(2020, 12, 31))

    def test_mdbm_following(self):
        # checks if rolling forward ok
        self.assertEqual(mdbm_following(d1, 1, 'pln', 'pln'), datetime.date(2020, 3, 2))
        self.assertEqual(mdbm_following(d1, 3, 'pln', 'pln'), datetime.date(2020, 5, 4))
        self.assertEqual(mdbm_following(d1, 6, 'pln', 'pln'), datetime.date(2020, 7, 31))
        self.assertEqual(mdbm_following(d1, 11, 'pln', 'pln'), datetime.date(2020, 12, 31))
        self.assertEqual(mdbm_following(d1, 12, 'pln', 'pln'), datetime.date(2021, 2, 1))
        self.assertEqual(mdbm_following(d1, 13, 'pln', 'pln'), datetime.date(2021, 3, 1))
        self.assertEqual(mdbm_following(d1, 24, 'pln', 'pln'), datetime.date(2022, 1, 31))
        self.assertEqual(mdbm_following(d1, 25, 'pln', 'pln'), datetime.date(2022, 3, 1))
        
        #checks if rolling over holidays ok
        self.assertEqual(mdbm_following(datetime.date(2019, 12, 6), 1, 'pln', 'pln'), datetime.date(2020, 1, 7))
        self.assertEqual(mdbm_following(datetime.date(2019, 12, 6), 1, 'usd', 'usd'), datetime.date(2020, 1, 6))

        #checks if rolling backward ok
        self.assertEqual(mdbm_following(d1, -1, 'pln', 'pln'), datetime.date(2019, 12, 31))
        self.assertEqual(mdbm_following(d1, -3, 'pln', 'pln'), datetime.date(2019, 10, 31))
        self.assertEqual(mdbm_following(d1, -6, 'pln', 'pln'), datetime.date(2019, 7, 31))
        self.assertEqual(mdbm_following(d1, -11, 'pln', 'pln'), datetime.date(2019, 3, 1))
        self.assertEqual(mdbm_following(d1, -12, 'pln', 'pln'), datetime.date(2019, 1, 31))
        self.assertEqual(mdbm_following(d1, -13, 'pln', 'pln'), datetime.date(2018, 12, 31))
        self.assertEqual(mdbm_following(d1, -24, 'pln', 'pln'), datetime.date(2018, 1, 31))
        self.assertEqual(mdbm_following(d6, -25, 'pln', 'pln'), datetime.date(2020, 12, 31))

    def test_mdbm_preceding(self):
        # checks if rolling forward ok
        self.assertEqual(mdbm_preceding(d1, 1, 'pln', 'pln'), datetime.date(2020, 2, 28))
        self.assertEqual(mdbm_preceding(d1, 3, 'pln', 'pln'), datetime.date(2020, 4, 30))
        self.assertEqual(mdbm_preceding(d1, 6, 'pln', 'pln'), datetime.date(2020, 7, 31))
        self.assertEqual(mdbm_preceding(d1, 11, 'pln', 'pln'), datetime.date(2020, 12, 31))
        self.assertEqual(mdbm_preceding(d1, 12, 'pln', 'pln'), datetime.date(2021, 1, 29))
        self.assertEqual(mdbm_preceding(d1, 13, 'pln', 'pln'), datetime.date(2021, 2, 26))
        self.assertEqual(mdbm_preceding(d1, 24, 'pln', 'pln'), datetime.date(2022, 1, 31))
        self.assertEqual(mdbm_preceding(d1, 25, 'pln', 'pln'), datetime.date(2022, 2, 28))
        
        #checks if rolling over holidays ok
        self.assertEqual(mdbm_preceding(datetime.date(2019, 12, 6), 1, 'pln', 'pln'), datetime.date(2020, 1, 3))
        self.assertEqual(mdbm_preceding(datetime.date(2019, 12, 6), 1, 'usd', 'usd'), datetime.date(2020, 1, 6))

        #checks if rolling backward ok
        self.assertEqual(mdbm_preceding(d6, -1, 'pln', 'pln'), datetime.date(2022, 12, 30))
        self.assertEqual(mdbm_preceding(d6, -3, 'pln', 'pln'), datetime.date(2022, 10, 31))
        self.assertEqual(mdbm_preceding(d6, -6, 'pln', 'pln'), datetime.date(2022, 7, 29))
        self.assertEqual(mdbm_preceding(d6, -11, 'pln', 'pln'), datetime.date(2022, 2, 28))
        self.assertEqual(mdbm_preceding(d6, -12, 'pln', 'pln'), datetime.date(2022, 1, 31))
        self.assertEqual(mdbm_preceding(d6, -13, 'pln', 'pln'), datetime.date(2021, 12, 31))
        self.assertEqual(mdbm_preceding(d6, -24, 'pln', 'pln'), datetime.date(2021, 1, 29))
        self.assertEqual(mdbm_preceding(d6, -25, 'pln', 'pln'), datetime.date(2020, 12, 31))

    def test_mdbm_modified_following(self):
        # checks if rolling forward ok
        self.assertEqual(mdbm_modified_following(datetime.date(2019, 12, 6), 1, 'pln', 'pln'),datetime.date(2020, 1, 7))
        self.assertEqual(mdbm_modified_following(datetime.date(2020, 1, 31), 1, 'pln', 'pln'),datetime.date(2020, 2, 28))
        self.assertEqual(mdbm_modified_following(datetime.date(2020, 2, 29), 1, 'pln', 'pln'),datetime.date(2020, 3, 31))
        self.assertEqual(mdbm_modified_following(d1, 1, 'pln', 'pln'), datetime.date(2020, 2, 28))
        self.assertEqual(mdbm_modified_following(d1, 3, 'pln', 'pln'), datetime.date(2020, 4, 30))
        self.assertEqual(mdbm_modified_following(d1, 6, 'pln', 'pln'), datetime.date(2020, 7, 31))
        self.assertEqual(mdbm_modified_following(d1, 11, 'pln', 'pln'), datetime.date(2020, 12, 31))
        self.assertEqual(mdbm_modified_following(d1, 12, 'pln', 'pln'), datetime.date(2021, 1, 29))
        self.assertEqual(mdbm_modified_following(d1, 13, 'pln', 'pln'), datetime.date(2021, 2, 26))
        self.assertEqual(mdbm_modified_following(d1, 24, 'pln', 'pln'), datetime.date(2022, 1, 31))
        self.assertEqual(mdbm_modified_following(d1, 25, 'pln', 'pln'), datetime.date(2022, 2, 28))
        
        #checks if rolling over holidays ok
        self.assertEqual(mdbm_modified_following(datetime.date(2019, 12, 6), 1, 'pln', 'pln'), datetime.date(2020, 1, 7))
        self.assertEqual(mdbm_modified_following(datetime.date(2019, 12, 6), 1, 'usd', 'usd'), datetime.date(2020, 1, 6))

        #checks if rolling backward ok
        self.assertEqual(mdbm_modified_following(d6, -1, 'pln', 'pln'), datetime.date(2022, 12, 30))
        self.assertEqual(mdbm_modified_following(d6, -3, 'pln', 'pln'), datetime.date(2022, 10, 31))
        self.assertEqual(mdbm_modified_following(d6, -6, 'pln', 'pln'), datetime.date(2022, 7, 29))
        self.assertEqual(mdbm_modified_following(d6, -11, 'pln', 'pln'), datetime.date(2022, 2, 28))
        self.assertEqual(mdbm_modified_following(d6, -12, 'pln', 'pln'), datetime.date(2022, 1, 31))
        self.assertEqual(mdbm_modified_following(d6, -13, 'pln', 'pln'), datetime.date(2021, 12, 31))
        self.assertEqual(mdbm_modified_following(d6, -24, 'pln', 'pln'), datetime.date(2021, 1, 29))
        self.assertEqual(mdbm_modified_following(d6, -25, 'pln', 'pln'), datetime.date(2020, 12, 31))

    def test_mdbm_eom(self):
        # checks if rolling forward ok
        self.assertEqual(mdbm_eom(datetime.date(2019, 12, 6), 1),datetime.date(2020, 1, 31))
        self.assertEqual(mdbm_eom(datetime.date(2020, 1, 31), 1),datetime.date(2020, 2, 29))
        self.assertEqual(mdbm_eom(datetime.date(2020, 2, 29), 1),datetime.date(2020, 3, 31))
        self.assertEqual(mdbm_eom(d1, 1), datetime.date(2020, 2, 29))
        self.assertEqual(mdbm_eom(d1, 3), datetime.date(2020, 4, 30))
        self.assertEqual(mdbm_eom(d1, 6), datetime.date(2020, 7, 31))
        self.assertEqual(mdbm_eom(d1, 11), datetime.date(2020, 12, 31))
        self.assertEqual(mdbm_eom(d1, 12), datetime.date(2021, 1, 31))
        self.assertEqual(mdbm_eom(d1, 13), datetime.date(2021, 2, 28))
        self.assertEqual(mdbm_eom(d1, 24), datetime.date(2022, 1, 31))
        self.assertEqual(mdbm_eom(d1, 25), datetime.date(2022, 2, 28))

        #checks if rolling backward ok
        self.assertEqual(mdbm_eom(d6, -1), datetime.date(2022, 12, 31))
        self.assertEqual(mdbm_eom(d6, -3), datetime.date(2022, 10, 31))
        self.assertEqual(mdbm_eom(d6, -6), datetime.date(2022, 7, 31))
        self.assertEqual(mdbm_eom(d6, -11), datetime.date(2022, 2, 28))
        self.assertEqual(mdbm_eom(d6, -12), datetime.date(2022, 1, 31))
        self.assertEqual(mdbm_eom(d6, -13), datetime.date(2021, 12, 31))
        self.assertEqual(mdbm_eom(d6, -24), datetime.date(2021, 1, 31))
        self.assertEqual(mdbm_eom(d6, -25), datetime.date(2020, 12, 31))

    def test_mdbm_eom_following(self):
        # checks if rolling forward ok
        self.assertEqual(mdbm_eom_following(datetime.date(2019, 12, 6), 1,  'pln', 'pln'),datetime.date(2020, 1, 31))
        self.assertEqual(mdbm_eom_following(datetime.date(2020, 1, 31), 1,  'pln', 'pln'),datetime.date(2020, 3, 2))
        self.assertEqual(mdbm_eom_following(datetime.date(2020, 2, 29), 1,  'pln', 'pln'),datetime.date(2020, 3, 31))
        self.assertEqual(mdbm_eom_following(d1, 1, 'pln', 'pln'), datetime.date(2020, 3, 2))
        self.assertEqual(mdbm_eom_following(d1, 3, 'pln', 'pln'), datetime.date(2020, 4, 30))
        self.assertEqual(mdbm_eom_following(d1, 6, 'pln', 'pln'), datetime.date(2020, 7, 31))
        self.assertEqual(mdbm_eom_following(d1, 11, 'pln', 'pln'), datetime.date(2020, 12, 31))
        self.assertEqual(mdbm_eom_following(d1, 12, 'pln', 'pln'), datetime.date(2021, 2, 1))
        self.assertEqual(mdbm_eom_following(d1, 13, 'pln', 'pln'), datetime.date(2021, 3, 1))
        self.assertEqual(mdbm_eom_following(d1, 24, 'pln', 'pln'), datetime.date(2022, 1, 31))
        self.assertEqual(mdbm_eom_following(d1, 25, 'pln', 'pln'), datetime.date(2022, 2, 28))

        #checks if rolling backward ok
        self.assertEqual(mdbm_eom_following(d6, -1, 'pln', 'pln'), datetime.date(2023, 1, 2))
        self.assertEqual(mdbm_eom_following(d6, -3, 'pln', 'pln'), datetime.date(2022, 10, 31))
        self.assertEqual(mdbm_eom_following(d6, -6, 'pln', 'pln'), datetime.date(2022, 8, 1))
        self.assertEqual(mdbm_eom_following(d6, -11, 'pln', 'pln'), datetime.date(2022, 2, 28))
        self.assertEqual(mdbm_eom_following(d6, -12, 'pln', 'pln'), datetime.date(2022, 1, 31))
        self.assertEqual(mdbm_eom_following(d6, -13, 'pln', 'pln'), datetime.date(2021, 12, 31))
        self.assertEqual(mdbm_eom_following(d6, -24, 'pln', 'pln'), datetime.date(2021, 2, 1))
        self.assertEqual(mdbm_eom_following(d6, -25, 'pln', 'pln'), datetime.date(2020, 12, 31))

if __name__ == '__main__':
    unittest.main()
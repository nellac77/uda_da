# -*- coding: utf-8 -*-
'''
This is a script that will read in a few different csv files, as per the 
Udacity data analysis course instructions.
'''

import unicodecsv

with open('enrollments.csv', "rb") as f:
    reader = unicodecsv.DictReader(f)
    enrollments = list(reader)
    
enrollments[0]

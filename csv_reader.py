# -*- coding: utf-8 -*-
'''
This is a script that will read in a few different csv files, as per the 
Udacity data analysis course instructions.
'''

import unicodecsv

# open the enrollments data file as a dictionary
with open('enrollments.csv', "rb") as f:
    reader = unicodecsv.DictReader(f)
    enrollments = list(reader)

# open the daily engagements data file as a dictionary
with open('daily_engagement.csv', "rb") as f:
    reader = unicodecsv.DictReader(f)
    daily_engagement = list(reader)

# open the project submission data file as a dictionary
with open('project_submissions.csv', "rb") as f:
    reader = unicodecsv.DictReader(f)
    project_submissions = list(reader)
    
# view first row of each table
print('\n', enrollments[0])
print('\n', daily_engagement[0])
print('\n', project_submissions[0])




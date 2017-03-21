#!usr/bin/env python

abbr = input('What is the three letter abbreviation of this course? ')

answer_status = ('wrong','correct')[abbr=='ECL']

print(('Your answer is wrong','Your answer is correct')[answer_status=='correct'])

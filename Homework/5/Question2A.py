#!usr/bin/env python

abbr = input('What is the three letter abbreviation of this course? ')

answer_status = 'wrong'
if abbr == 'ECL': answer_status = 'correct'

if answer_status == 'correct':
    print('Your answer is correct')
else:
    print('Your answer is wrong')

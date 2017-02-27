#! /usr/bin/env python

life_expectancy = 120; print("The life expectancy for the millennials is projected to be %3d years! (But don't believe it...)" % life_expectancy + "\n")

print('''
    A recent study published in the journal of Nature, discovered that over the past century,
    although the life expectancy has significantly increased due to technological advances,
    the maximum life span of the oldest people in the world has not changed much.
''')

from cmath import sqrt # cmath function always return complex numbers
from math import sqrt as fsqrt # math function always work with and return real numbers
print("""
Cardano was the first to introduce complex numbers of the form a + sqrt(-b) into algebra, but he had misgivings about it. \

In his solution to an algebra equation he encountered the solution 5 + sqrt(-15) for the unknown, which is now mathematically represented by \n \n \
      {first:} \n\nin Python, which can also be obtained as an addition of real and imaginary numbers in Python like this \n\n\
      
      5 + sqrt(-15) = {second:}, \n\n
      which can also be manually stated as 
      
      
      {third:} \n

""".format(second=complex(5,sqrt(15)) ,first=(5+sqrt(-15)) , third=(5+3.872983346207417j) ) )

print('''

One final note: \n
\tIn python the sqrt function from math and cmath modules are different.
\tThe sqrt function that returns "float" results is sqrt from math module.
\tTherefore, if using math module, then,

\t\tsqrt(25) = {:.4f}, 

\twhich is obviously a float (real number).

''' .format(fsqrt(25)))

print('''

Also note that by convention, 0**0 = {first:d} in Python.
And division by 0, will give you a runtime exception: 1/0 = {second:}

''' .format(first=0**0,second='NaN') 
)
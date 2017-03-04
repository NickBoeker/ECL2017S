#!usr/bin/env python

from math import pi,exp,sqrt

mu = 0
sig = 2
x = 1

result = (1/(sqrt(2*pi)*sig))*exp(-0.5*((x-mu)/sig)**2)

print(result)
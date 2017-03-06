#!usr/bin/env python
from math import log,pi

m = 47
M = 67
p = 1.308
c = 3.7
K = 5.4*10**-3
Tw = 100
Ty = 70
To1 = 4
To2 = 20

t1 = M**(2/3)*c*p**(1/3)*log(.76*(To1-Tw)/(Ty-Tw))/(K*pi**2*(4*pi/3)**(2/3))
t2 = M**(2/3)*c*p**(1/3)*log(.76*(To2-Tw)/(Ty-Tw))/(K*pi**2*(4*pi/3)**(2/3))

print('t1 = {}, t2 = {}'.format(t1,t2))
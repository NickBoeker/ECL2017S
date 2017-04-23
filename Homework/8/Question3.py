import numpy as np
from math import pi,log

def midptEstimate(f,a,b,n):
    h = (b-a)/n
    x = np.arange(a,b,h)
    y = f(x+0.5*h)
    y = y[:-1]
    res = np.sum(h*y)
    return res

ex = midptEstimate(np.exp,0,log(3),100000)
cs = midptEstimate(np.cos,0,pi,100000)
sn = midptEstimate(np.sin,0,pi,100000)
snshort = midptEstimate(np.sin,0,pi/2,100000)

print(ex)
print(cs)
print(sn)
print(snshort)
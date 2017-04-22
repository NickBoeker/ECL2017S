import numpy as np
from math import pi,log

def midptEstimate(f,a,b,n):
    h = b-a/n
    x = np.arange(a,b,h)
    y = h*f(x+0.5)

    print(x)
    print(y)
    return y

y = midptEstimate(np.exp,0,log(3),10)
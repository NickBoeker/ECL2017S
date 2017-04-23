import numpy as np
from math import pi,floor
import matplotlib.pyplot as plt

a = 0
b = 10
n = 10
h = (b-a)/n

fig,ax = plt.subplots(1,1)    

x = np.arange(a,b,.001)
x_md = np.arange(a,b+.001,h)
f = lambda x:x*(12-x)+np.sin(pi*x)
y = f(x)
md = f(x_md+h/2)
md_fine = [md[floor((i-a)/h)] for i in x]
'''
for item in x:
    m = floor((item-a)/h)
    md_fine = md[m]
'''

ax.plot(x,y,'r')
#ax.step(x_md,md,'g',where="post")
ax.fill_between(x,md_fine,y)
plt.show()
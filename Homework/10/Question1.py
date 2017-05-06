import random as rnd
import numpy as np
import matplotlib.pyplot as plt
import math

def pi_gen(n):
    area = np.zeros(n); xaxis = np.zeros(n)
    Sc = 0; Ss = 0;

    for i in range(n):
        x = rnd.random()
		y = rnd.random()
        sqrtfunc = math.sqrt(x*x + y*y)
        if sqrtfunc <= 1:
            Sc = Sc+ 1
            Ss = Ss + 1
        else:
            Ss = Ss + 1
        area[i] = (Sc/Ss)*4
        xaxis[i] = (i+1)
    return area,xaxis
n = 1000
[dat,x]= pi_gen(n)
plt.plot(x, dat)
plt.xlabel('Number of Simulated Points')
plt.ylabel('Approximate Value of Pi')
plt.title('Estimating Pi Using Monte Carlo Simulations')
plt.show()
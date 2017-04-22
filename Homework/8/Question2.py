import sys
import numpy as np
import matplotlib.pyplot as plt

if len(sys.argv[:]) != 3:
    print("Usage: python Question2.py v0(m/s) m(kg)")
    sys.exit()
    
g = 9.81
v0 = float(sys.argv[1])
m = float(sys.argv[2])
t = np.arange(0,(2*v0/g),.1)
y = v0*t-0.5*g*np.square(t)
v = v0-g*t
P = m*g*y
K = .5*m*np.square(v)
E = P+K

plt.plot(t,P)
plt.plot(t,K)
plt.plot(t,E)
plt.xlabel('Time(s)')
plt.ylabel('Energy(J)')
plt.title('Conservation of Energy')
plt.savefig('Question2_Plot.png')
plt.show()

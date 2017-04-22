import numpy as np
def vectorHatFunction(x):
    y = x
    y = np.where(x<0,np.zeros(len(y)),y)
    y = np.where(np.logical_and(x>=1,x<2),y-2,y)
    y = np.where(x>=2,np.zeros(len(y)),y)
    return y

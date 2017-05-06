import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpa
import random as rnd
import math
def plotFnc():
	x = np.linspace(.001,15,10000)
	y = (x+1)/12*np.exp(-1*np.power(x-1,2)/(2*x))
	plt.plot(x,y,'r')
	plt.legend('f(x)')
	
def sample(n):
	dat = np.random.rand(n,2)
	goodDat = []
	dat[:,0] = 15*dat[:,0]
	dat[:,1] = .2*dat[:,1]
	plt.figure(2)
	for idx in range(n):
		x,y = dat[idx,0],dat[idx,1]
		if y < (x+1)/12*math.exp(-1*(x-1)**2/(2*x)):
			plt.plot(x,y,'ro')
			goodDat.append(x)
		else:
			plt.plot(x,y,'ko')
	plt.figure(1)
	arrDat = np.array(goodDat)
	hist, bin_edges = np.histogram(arrDat,bins=25)
	max = np.max(hist)
	scaleHist = .2/max*hist
	xHist = [(bin_edges[i+1]+bin_edges[i])/2 for i in range(25)]
	plt.bar(xHist,scaleHist,color='#33C3FF')
	
plt.figure(1)
plotFnc()
sample(10000)
plt.savefig('hist.png')
plt.figure(2)
red_dot = mpa.Patch(color='red',label='accepted')
blk_dot = mpa.Patch(color='black',label='rejected')
plt.legend(handles=[blk_dot,red_dot],loc=1)
plt.savefig('scatter.png')
plt.show()
import scipy.io as sio
import numpy as np
import matplotlib.pyplot as plt
from math import exp,log,pi,sqrt

def importMat(fileName):
	filePath = "../data/"+fileName
	fn = sio.loadmat(filePath)
	datM = fn['cells']
	dat = np.array(datM)
	return dat
	
def plotRaw(cells):
	global tReal #= [10,12,14,15,16,18,20]
	vMax = np.max(cells)
	vMin = np.min(cells)
	for t in range(cells.shape[3]):
		fig = plt.figure(t+1,figsize=(15,15))
		oax = fig.add_subplot(111)
		oax.set_title('Time = {} days. Brain MRI slices along Z-direction, Rat W09. No radiation treatment'.format(tReal[t]),y=1.03)
		oax.set_ylabel('Voxel Number in Y Direction')
		oax.set_xlabel('Voxel Number in X Direction')
		oax.spines['top'].set_color('none')
		oax.spines['bottom'].set_color('none')
		oax.spines['left'].set_color('none')
		oax.spines['right'].set_color('none')
		oax.tick_params(labelcolor='w', top='off',bottom='off',left='off',right='off')

		for z in range(cells.shape[2]):
			ax = fig.add_subplot(4,4,z+1)
			ax.set_title("z="+str(z+1))
			if (z+1)%4==1 and (z+1)>12:
				plt.yticks(np.arange(10,41,10))
				plt.xticks(np.arange(20,61,20))
			elif (z+1)%4 ==1:
				ax.axes.get_xaxis().set_visible(False)
				plt.yticks(np.arange(10,41,10))
			elif (z+1) > 12:
				ax.axes.get_yaxis().set_visible(False)
				plt.xticks(np.arange(20,61,20))
			else:
				ax.axes.get_xaxis().set_visible(False)
				ax.axes.get_yaxis().set_visible(False)
			dat = plt.imshow(cells[:,:,z,t],'nipy_spectral',clim=(vMin,vMax))
		fig.subplots_adjust(right=0.9)
		cbar_ax = fig.add_axes([0.91,0.1,.02,.8])
		fig.colorbar(dat,cax=cbar_ax)
		plt.savefig('../results/t{}.png'.format(tReal[t]))

def plotTrend(cells):

	tReal = [10,12,14,15,16,18,20]
	count = []
	
	for t in range(cells.shape[3]):
		count.append(np.sum(cells[:,:,:,t]))

	fig = plt.figure()
	plt.title('Rat W09. No radiation treatment.')
	plt.xlabel('Time [days]')
	plt.xlim((8,24))
	plt.ylabel('Tumor Cell Count')
	plt.plot(tReal,count,'b-')
	plt.plot(tReal,count,'bo')
	plt.savefig('../results/trend.png')

def Gomp(param,t):
	a = param[0]
	b = param[1]
	c = param[2]
	return a*exp(-b*exp(-c*t))

def prob(param):
	a = param[0]
	b = param[1]
	c = param[2]
	sig = param[3]
	
	global cells
	global tReal
	
	sum_prob = 0
	for t in range(len(tReal)):
		temp_prob = exp(-1*(np.sum(cells[:,:,:,t])-Gomp(param,t))**2/(2*sig**2))
		print(temp_prob)
		sum_prob += log(temp_prob /(sig*sqrt(2*pi)))
	print(sum_prob)
	return sum_prob

def logLike(param):
	global tReal
	global cells
	n = len(tReal)
	
	lsSum = 0
	for t in range(n):
		temp = (np.sum(cells[:,:,:,t])-Gomp(param,t))**2
		lsSum += temp
	
	log_prob = -n/2*(log(2*pi)+log(param[3]**2))-1/(2*param[3]**2)*lsSum#prob(param)
	#real_prob = exp(log_prob)
	return log_prob#real_prob
	
tReal = [10,12,14,15,16,18,20]
cells = importMat('cells.mat')
plotRaw(cells)
plotTrend(cells)
print("This is the log likelyhood "+str(logLike((1,1,3,1))))

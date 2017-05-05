import urllib.request as ur
from parseTable import parseTable
import sys
import os
import numpy as np
import matplotlib.pyplot as plt

def fetchHTMLTable(link,outputPath):
	ur.urlretrieve(link, filename=outputPath+'exactHTML.html')
	tableFile = open(outputPath+'exactHTML.html')
	tableOutput = tableFile.read()
	parsedHTML = parseTable(tableOutput)
	outfile = open(outputPath+'resultsTable.out','w')
	for line in parsedHTML:
		for item in line:
			outfile.write('{:>30}'.format(item))
		outfile.write('\n')
	outfile.close()
	
def fileRetriever(outputPath):
	tabFile = open(outputPath+'resultsTable.out','r')
	for line in tabFile:
		if line[28]=='#':
			continue
			
		dataNum=line[21:29]
		fName="http://butler.lab.asu.edu/swift/"+dataNum+"/bat/ep_flu.txt"
		try:
			ur.urlretrieve(fName,outputPath+"GRB"+dataNum+"_ep_flu.txt")
		except ur.HTTPError:
			print(fName+" does not exist")
			continue
			
def plotter(inPath,figFile):
	ax = plt.gca()  # generate a plot handle
	ax.set_xlabel('Fluence [ ergs/cm^2 ]') # set X axis title
	ax.set_ylabel('Epeak [ keV ]')  # set Y axis title
	ax.set_yscale('log')
	ax.set_xscale('log')
	ax.axis([1.0e-8, 1.0e-1, 1.0, 1.0e4]) # set axix limits [xmin, xmax, ymin, ymax]
	counter = 0     # counts the number of events
	
	for file in os.listdir(inPath):
		if file.endswith("ep_flu.txt"):
			data = np.loadtxt(os.path.join(inPath, file), skiprows=1)
			if data.size!=0 and all(data[:,1]<0.0):
				counter +=1
				data[:,1] = np.exp(data[:,1])
				ax.scatter(data[:,1],data[:,0],s=1,alpha=0.05,c='r',edgecolors='none')
	
	ax.set_title('Plot of Epeak vs. Fluence for {} Swift GRB events'.format(counter))
	plt.savefig(inPath+figFile)

link = "http://butler.lab.asu.edu/swift/bat_time_table.html"
outputPath = "q1output/"
fetchHTMLTable(link,outputPath)
fileRetriever(outputPath)
plotter(outputPath,'fig.png')
print("Program Complete")
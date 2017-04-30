import urllib.request as ur
from parseTable import parseTable
import sys

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
        outfile = open(outputPath+'resultsTable.out','r')

link = "http://butler.lab.asu.edu/swift/bat_time_table.html"
#21:28
outputPath = "q1output/"
fetchHTMLTable(link,outputPath)

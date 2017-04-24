import urllib.request as ur
from parseTable import parseTable

def fetchHTMLTable(link,outputPath):
        ur.urlretrieve(link, filename=outputPath+'exactHTML.html')
        parsed = parseTable(outputPath+'exactHTML.html')
        print(parsed)
        outfile = open(outputPath+'idk.txt','w')
        outfile.write('test')
        outfile.close()

link = "http://butler.lab.asu.edu/swift/bat_time_table.html"
outputPath = "q1output/"
fetchHTMLTable(link,outputPath)
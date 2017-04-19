import sys
if len(sys.argv) !=3:
    print("Usage: python outputter.py outputter.in outputter.out")
    sys.exit(1)
    
infn = sys.argv[1]
outfn = sys.argv[2]

infile = open(infn,"r")
outfile = open(outfn,"w")

for line in infile:
    linelist = line.split(',')
    for x in linelist:
        outfile.write("{:14.3f}".format(float(x)))
    outfile.write('\n')
        
outfile.close()
infile.close()
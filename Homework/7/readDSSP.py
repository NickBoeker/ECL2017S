import sys,os

if len(sys.argv) !=3:
    print("Usage: python readDSSP.py <input file> <output file>")
    print("Program aborted")
    sys.exit()
    
infn = sys.argv[1]
outfn = sys.argv[2]

infile = open(infn,"r")
if os.path.isfile(outfn):
    outfile = open(outfn,"a")
else:
    outfile = open(outfn,"w")

proName = sys.argv[1][:-5]
acidDict = {'A': 129.0,
            'R': 274.0,
            'N': 195.0,
            'D': 193.0,
            'C': 167.0,
            'Q': 225.0,
            'E': 223.0,
            'G': 104.0,
            'H': 224.0,
            'I': 197.0,
            'L': 201.0,
            'K': 236.0,
            'M': 224.0,
            'F': 240.0,
            'P': 159.0,
            'S': 155.0,
            'T': 172.0,
            'W': 285.0,
            'Y': 263.0,
            'V': 174.0}

outfile.write("pdb\tname\tACC\tRSA\n")
data = False
for line in infile:
    if line[2] == '#':
        data = True
        continue
    if data == True:
        if line[13]=="!": continue
        maxArea = acidDict[line[13]]
        rsa = int(line[35:38].strip())/maxArea
        outfile.write("{}\t{}\t{}\t{}\n".format(proName,line[13],line[35:38],rsa))
        
infile.close()
outfile.close()
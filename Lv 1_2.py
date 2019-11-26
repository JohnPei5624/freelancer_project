## Project URL from 
## Freelancer.com
## Level 1_2 Refining

inFileLoc = r'E:\2018-0511\GA Project - Freelancer & Experiment\1_2_supplement.txt'
outFileLoc = r'E:\2018-0511\GA Project - Freelancer & Experiment\1_2_1_proj_url.csv'

inFile = open(inFileLoc, 'r')
outFile = open(outFileLoc, 'a')

line = inFile.readline()
while line != '':
    outFile.write(line)
    line = inFile.readline()


inFile.close()
outFile.close()


#### python NSEvsBSE.py FileToKeepFully.csv SomeKeep.csv out.csv lookup outputCol1 outputCol2...
#### FileToKeepFully.csv data will be present to which SomeKeep.csvfile will be appended
import sys
import csv
import pandas as pd
import numpy as np
#filename=sys.argv[1]
if len(sys.argv)<6:
	print("Insufficient arguments")
	print("python NSEvsBSE.py FileToKeepFully.csv SomeKeep.csv out.csv lookup outputCol1 outputCol2...")
	exit(1)
else:
	input1file=sys.argv[2]		## input1file is SECOND argument
	input2file=sys.argv[1]		## input2file is FIRST argument
	outputfile=sys.argv[3]		# where output is to be written
	lookupColValue=sys.argv[4]	# lookup using this column
	outputColumns=list(sys.argv[5:])	# list of output columns to fetch from input1file
print(input1file+"\n"+input2file+"\n"+outputfile+"\n"+lookupColValue+"\n"+str(outputColumns))
# reading file1
with open(input1file, 'r') as csvfile:
    file1AsList=list(csv.reader(csvfile))
# reading file2
with open(input2file, 'r') as csvfile:
    file2AsList=list(csv.reader(csvfile))
## Finding Index for lookup Columns in file1 and file2
colHeadersfile1=file1AsList[0]	
colHeadersfile2=file2AsList[0]
lookupIndListfile1 = [i for i,x in enumerate(colHeadersfile1) if lookupColValue in x]
lookupIndListfile2 = [i for i,x in enumerate(colHeadersfile2) if lookupColValue in x]
if(len(lookupIndListfile2) == 0 or len(lookupIndListfile1) == 0):
	print("LookupCol not found in files")
	exit(1)
## Finding Index for Output Columns in file1
outputColmnIndexListfile1 = []
for outCol in outputColumns:
	colmnInd=0
	for headers in colHeadersfile1:
		if outCol == headers:
			outputColmnIndexListfile1.append(colmnInd)
		colmnInd=colmnInd+1
if len(outputColmnIndexListfile1)==0:
	print("Output Columns not found in file1")
	exit(1)
# for outColIndex in outputColmnIndexListfile1:
# 	print(outColIndex)
# print(str(lookupIndListfile1)+"|"+str(lookupIndListfile2))
# printing the field names
row=[]
finalList=[]
file2Notfound=[]
for f2row in file2AsList[1:len(file2AsList)]:
	found=0
	for f1row in file1AsList[1:len(file1AsList)]:
		if f2row[lookupIndListfile2[0]] == f1row[lookupIndListfile1[0]]:
			found=found+1
			for rowCntnt in f2row:
				row.append(rowCntnt)
			for outColIndex in outputColmnIndexListfile1:
				row.append(f1row[outColIndex])
			finalList.append(row)
			row=[]
			break
	if found==0:
		file2Notfound.append(f2row)

# print('Final Headers:f2' + ',f2'.join(head for head in colHeadersfile2)+',f1'+',f1'.join(colHeadersfile1[i] for i in outputColmnIndexListfile1))
#print ('Data rows'+str(len(fileAsList)-1))
#  printing first 5 rows
# print('\nFirst 5 rows are:\n')
# for row in finalList[1:6]:
#     # parsing each column of a row
#     print(str(row))
with open(outputfile,'w') as f:
	f.write('f2'+',f2'.join(head for head in colHeadersfile2)+',f1'+',f1'.join(colHeadersfile1[i] for i in outputColmnIndexListfile1))
	f.write('\n')
	for row in finalList:
		f.write(','.join(str(val) for val in row))
		f.write('\n')
print(outputfile)
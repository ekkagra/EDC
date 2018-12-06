#### python NSEvsBSE.py FileToKeepFully.csv SomeKeep.csv out.csv lookup outputCol1 outputCol2...
#### FileToKeepFully.csv data will be present to which SomeKeep.csvfile will be appended
import sys
import csv
import pandas as pd
import numpy as np
#filename=sys.argv[1]
if len(sys.argv)<6:
	print("Insufficient arguments")
	print("python NSEvsBSE.py FileToKeepFully.csv SomeKeep.csv [out.xlsx | out.csv] lookup outputCol1 outputCol2...")
	sys.exit()
else:
	input1file=sys.argv[2]		## input1file is SECOND argument
	input2file=sys.argv[1]		## input2file is FIRST argument
	outputfile=sys.argv[3]		# where output is to be written
	lookupColValue=sys.argv[4]	# lookup using this column
	outputColumns=list(sys.argv[5:])	# list of output columns to fetch from input1file
print(input1file+"\n"+input2file+"\n"+outputfile+"\n"+lookupColValue+"\n"+str(outputColumns))

#---------------------------- Reading files
df2=pd.read_csv(input2file)
df1=pd.read_csv(input1file)

#---------------------------- Finding Index for lookup Columns in file1 and file2
colHeadersfile1=df1.columns
colHeadersfile2=df2.columns
lookupColFile2=''
for colName in colHeadersfile2:
	if lookupColValue in colName:
		lookupColFile2=colName
lookupColFile1=''
for colName in colHeadersfile1:
	if lookupColValue in colName:
		lookupColFile1=colName
if lookupColFile1 == '' or lookupColFile2 == '':
	print("LookupCol not found in files")
	sys.exit()

#---------------------------- Finding Index for Output Columns in file
for colmn in outputColumns:
	if not(colmn in colHeadersfile1):
		print("Columns "+colmn+" not found in file1")
		sys.exit()

outputColumns.append(lookupColFile1)

print(outputColumns)
#---------------------------- Left Join of df2 with df1
dfJoined=df2.join(df1[outputColumns].set_index(lookupColFile1),how='inner', on=lookupColFile2,lsuffix='_2', rsuffix='_1')
dfJoined['Chnge']=(dfJoined['CLOSE_2']-dfJoined['CLOSE_1'])*100/dfJoined['CLOSE_1']
dfSorted=dfJoined.sort_values('Chnge',ascending=False)
# dfSorted.loc[dfSorted.SC_GROUP == 'A '].head(50)
# dfSorted.loc[dfSorted.SERIES == 'EQ'].head(50)

#---------------------------- writing to output csv/xlsx file
if outputfile.split('.')[-1] == 'csv':
	dfSorted.to_csv(outputfile)
elif outputfile.split('.')[-1] == 'xlsx':
	writer = pd.ExcelWriter(outputfile)
	dfSorted.to_excel(writer,'Sorted')
	writer.save()

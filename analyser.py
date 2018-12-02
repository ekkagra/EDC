## python analyser.py Filepath exchngeDateType

import pandas as pd
import numpy as np
import sys

if len(sys.argv)<=2:
	print("file path and exchnge data type missing")
	print("python analyser.py Filepath exchngeDateType")
	exit(1)
else:
	inputFile=sys.argv[1]
	exchngeDateType=sys.argv[2]
	outputFile='./analyserOut.csv'
df=pd.read_csv(inputFile)
if exchngeDateType=='diff':
	print(df.head(10))
	col=['f2SC_NAME', 'f2OPEN', 'f2HIGH', 'f2LOW', 'f2CLOSE', 'f2LAST', 'f2PREVCLOSE', 'f2NO_TRADES', 'f1CLOSE', 'f1PREVCLOSE']
	newdf=pd.DataFrame(df,columns=col)
	#print(newdf.head(10))
	#print(newdf.describe())
	newdf['BSEChnge']=(newdf['f2CLOSE']-newdf['f2PREVCLOSE'])*100/newdf['f2PREVCLOSE']
	newdf['NSEChnge']=(newdf['f1CLOSE']-newdf['f1PREVCLOSE'])*100/newdf['f1PREVCLOSE']
	newdf['avgChnge']=(newdf['BSEChnge']+newdf['NSEChnge'])/2
	sorted=newdf.sort_values('avgChnge',ascending=False)
	print(sorted.head(20))
	print(sorted.describe())
	sorted.to_csv(outputFile)
elif exchngeDateType=='same':
	print(df.head(10))
	col=['f2SC_NAME', 'f2OPEN', 'f2HIGH', 'f2LOW', 'f2CLOSE', 'f2LAST', 'f2PREVCLOSE', 'f2NO_TRADES', 'f1CLOSE', 'f1PREVCLOSE']
	newdf=pd.DataFrame(df,columns=col)
	#print(newdf.head(10))
	#print(newdf.describe())
	newdf['Chnge']=(newdf['f2CLOSE']-newdf['f1CLOSE'])*100/newdf['f1CLOSE']
	#newdf['NSEChnge']=(newdf['f1CLOSE']-newdf['f1PREVCLOSE'])*100/newdf['f1PREVCLOSE']
	#newdf['avgChnge']=(newdf['BSEChnge']+newdf['NSEChnge'])/2
	sorted=newdf.sort_values('Chnge',ascending=False)
	moreThan2000 = sorted['f2NO_TRADES'] > 2000
	sorted_filtered = sorted[moreThan2000]
	print(sorted.head(20))
	print(sorted.describe())
	print(sorted_filtered.head(20))
	print(sorted_filtered.describe())
	sorted.to_csv(outputFile)

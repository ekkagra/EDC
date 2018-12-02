import sys
import pandas as pd
import numpy as np
if len(sys.argv) == 1 or len(sys.argv) == 2:
	print("File arguments missing")
	sys.exit(1)

fileOld=sys.argv[1]
fileNew=sys.argv[2]
chunk = []
f1chunks = []
f2chunks = []
for line in open(fileOld):
	chunk = line.split(",")
	f1chunks.append(chunk[0:13])
	chunk = []
for line in open(fileNew):
	chunk = line.split(",")
	f2chunks.append(chunk[0:13])
	chunk = []

def takeSCCode(elem):
	return elem[0]

f1chunks.sort(key=takeSCCode)
#print(str(f1chunks[0]))
final_chunk = []
count1 = 0
notFound = []
for chunk in f2chunks[1:len(f2chunks)]:
	found=0
	for c in f1chunks[1:len(f1chunks)]:
		if chunk[0] == c[0]:
			chunk.append(c[7])
			final_chunk.append(chunk)
			change=(float(chunk[7])-float(c[7]))/float(c[7])
			final_chunk.append("{0:.5f}".(change))
			count1 = count1 +1
			break
	if found == 0:
		notFound.append(chunk)
print("SC_CODE,SC_NAME,SC_GROUP,SC_TYPE,OPEN,HIGH,LOW,CLOSE,LAST,PREVCLOSE,NO_TRADES,NO_OF_SHRS,NET_TURNOV,OLD_CLOSE,Change")
for chunk in final_chunk:
	for col in chunk[0:len(chunk)-1]:
		print(str(col)+",", end="")
	print(str(chunk[len(chunk)-1]))
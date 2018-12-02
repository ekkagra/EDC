# Module to download two bhav data files for comparison
### python downloadFile.py xvx dtF2 dtF1 DownloadDirectory\
import sys
import datetime
import time
import requests
import zipfile
import os
### path declaration with ending "/"
if len(sys.argv) <= 4:
	print("Output Directory path missing")
	print("python downloadFile.py XvX dtF2 dtF1 DownloadDirectory\\")
	exit(1)
xvx=sys.argv[1].lower()
dtF2=sys.argv[2]
dtF1=sys.argv[3]
data_path=sys.argv[4]
givenF2Date=datetime.datetime.strptime(dtF2,"%d%m%Y")
givenF1Date=datetime.datetime.strptime(dtF1,"%d%m%Y")
### function definitions
def latestWeekdayDate(givenDate):
	if givenDate.isoweekday() == 6 or givenDate.isoweekday() == 7:
		cur_weekday=givenDate.isoweekday()
		latest_date=givenDate-datetime.timedelta(days=cur_weekday-5)
	else:
		latest_date=givenDate
	return latest_date;

def dt2NSEdt(givenDate):
	return givenDate.strftime("%d%b%Y").upper();

def dt2BSEdt(givenDate):
	return givenDate.strftime("%d%m%y");

def dt2NSEURL(givenDate):
	dateNSE=givenDate.strftime("%d%b%Y").upper()
	cur_year=givenDate.strftime("%Y")
	cur_month=givenDate.strftime("%b").upper()
	nseZipURL="https://www.nseindia.com/content/historical/EQUITIES/"+cur_year+"/"+cur_month+"/cm"+dateNSE+"bhav.csv.zip"
	return nseZipURL;

def dt2BSEURL(givenDate):
	dateBSE=givenDate.strftime("%d%m%y")
	bseZipURL="https://www.bseindia.com/download/BhavCopy/Equity/EQ_ISINCODE_"+dateBSE+".zip"
	return bseZipURL;

### Saturday,Sunday logic
# curF2year=reqF2Date.strftime("%Y")
# curF2month=reqF2Date.strftime("%b").upper()
# curF1year=reqF1Date.strftime("%Y")
# curF1month=reqF1Date.strftime("%b").upper()
# if reqF2Date.isoweekday() == 6 or reqF2Date.isoweekday() == 7:
# 	curF2weekday=reqF2Date.isoweekday()
# 	latestF2date=reqF2Date-datetime.timedelta(days=curF2weekday-5)
# else:
# 	latestF2date=reqF2Date
# if reqF1Date.isoweekday() == 6 or reqF1Date.isoweekday() == 7:
# 	curF1weekday=reqF1Date.isoweekday()
# 	latestF1date=reqF1Date-datetime.timedelta(days=curF1weekday-5)
# else:
# 	latestF1date=reqF1Date	

### Setting Filenames to be downloaded
dtF22=latestWeekdayDate(givenF2Date)
dtF11=latestWeekdayDate(givenF1Date)

if xvx[0] == 'b':
	latestF2date=dt2BSEdt(dtF22)
	F2ZipURL=dt2BSEURL(dtF22)
	F2ZIPFile=data_path+"EQ_ISINCODE_"+latestF2date+".zip"
	F2CsvFile=F2ZIPFile.replace(".zip","")
elif xvx[0] == 'n':
	latestF2date=dt2NSEdt(dtF22)
	F2ZipURL=dt2NSEURL(dtF22)
	F2ZIPFile=data_path+"cm"+latestF2date+"bhav.csv.zip"
	F2CsvFile=F2ZIPFile.replace(".zip","")
if xvx[2] == 'b':
	latestF1date=dt2BSEdt(dtF11)
	F1ZipURL=dt2BSEURL(dtF11)
	F1ZIPFile=data_path+"EQ_ISINCODE_"+latestF1date+".zip"
	F1CsvFile=F1ZIPFile.replace(".zip","")
elif xvx[2] == 'n':
	latestF1date=dt2NSEdt(dtF11)
	F1ZipURL=dt2NSEURL(dtF11)
	F1ZIPFile=data_path+"cm"+latestF1date+"bhav.csv.zip"
	F1CsvFile=F1ZIPFile.replace(".zip","")

# if xvx == 'bvb':
# 	latestF2date=dt2BSEdt(dtF22)
# 	F2ZipURL=dt2BSEURL(dtF22)
# 	F2ZIPFile=data_path+"EQ_ISINCODE_"+latestF2date+".zip"
# 	F2CsvFile=F2ZIPFile.replace(".zip","")
# 	latestF1date=dt2BSEdt(dtF11)
# 	F1ZipURL=dt2BSEURL(dtF11)
# 	F1ZIPFile=data_path+"EQ_ISINCODE_"+latestF1date+".zip"
# 	F1CsvFile=F1ZIPFile.replace(".zip","")
# elif xvx == 'bvn':
# 	latestF2date=dt2BSEdt(dtF22)
# 	F2ZipURL=dt2BSEURL(dtF22)
# 	F2ZIPFile=data_path+"EQ_ISINCODE_"+latestF2date+".zip"
# 	F2CsvFile=F2ZIPFile.replace(".zip","")
# 	latestF1date=dt2NSEdt(dtF11)
# 	F1ZipURL=dt2NSEURL(dtF11)
# 	F1ZIPFile=data_path+"cm"+latestF1date+"bhav.csv.zip"
# 	F1CsvFile=F1ZIPFile.replace(".zip","")
# elif xvx == 'nvn':
# 	latestF2date=dt2NSEdt(dtF22)
# 	F2ZipURL=dt2NSEURL(dtF22)
# 	F2ZIPFile=data_path+"cm"+latestF2date+"bhav.csv.zip"
# 	F2CsvFile=F2ZIPFile.replace(".zip","")
# 	latestF1date=dt2NSEdt(dtF11)
# 	F1ZipURL=dt2NSEURL(dtF11)
# 	F1ZIPFile=data_path+"cm"+latestF1date+"bhav.csv.zip"
# 	F1CsvFile=F1ZIPFile.replace(".zip","")
# elif xvx == 'nvb':
# 	latestF2date=dt2NSEdt(dtF22)
# 	F2ZipURL=dt2NSEURL(dtF22)
# 	F2ZIPFile=data_path+"cm"+latestF2date+"bhav.csv.zip"
# 	F2CsvFile=F2ZIPFile.replace(".zip","")
# 	latestF1date=dt2BSEdt(dtF11)
# 	F1ZipURL=dt2BSEURL(dtF11)
# 	F1ZIPFile=data_path+"EQ_ISINCODE_"+latestF1date+".zip"
# 	F1CsvFile=F1ZIPFile.replace(".zip","")
	
# dateNSE=latest_date.strftime("%d%b%Y").upper()
# dateBSE=latest_date.strftime("%d%m%y")
# nseZipURL="https://www.nseindia.com/content/historical/EQUITIES/"+cur_year+"/"+cur_month+"/cm"+dateNSE+"bhav.csv.zip"
# bseZipURL="https://www.bseindia.com/download/BhavCopy/Equity/EQ_ISINCODE_"+dateBSE+".zip"
# NSEZIPFile=data_path+"cm"+dateNSE+"bhav.csv.zip"
# BSEZIPFile=data_path+"EQ_ISINCODE_"+dateBSE+".zip"
# NSECsvFile=NSEZIPFile.replace(".zip","")
# BSECsvFile=BSEZIPFile.replace(".zip","")

### Download files
r = requests.get(F2ZipURL, stream = True)
with open(F2ZIPFile,"wb") as zipFile:
	for chunk in r.iter_content(chunk_size=1024):
		# writing one chunk at a time to zip file
		if chunk:
			zipFile.write(chunk)
r = requests.get(F1ZipURL, stream = True)
with open(F1ZIPFile,"wb") as zipFile:
	for chunk in r.iter_content(chunk_size=1024):
		# writing one chunk at a time to zip file
		if chunk:
			zipFile.write(chunk)
with zipfile.ZipFile(F2ZIPFile,"r") as zip_ref:
		zip_ref.extractall(F2CsvFile)
with zipfile.ZipFile(F1ZIPFile,"r") as zip_ref:
		zip_ref.extractall(F1CsvFile)
F2CsvFile=F2CsvFile+"/"+os.listdir(F2CsvFile)[-1]
F1CsvFile=F1CsvFile+"/"+os.listdir(F1CsvFile)[-1]
print(F2CsvFile+" "+F1CsvFile)
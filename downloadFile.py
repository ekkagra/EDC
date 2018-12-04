# Module to download two bhav data files for comparison
### python downloadFile.py xvx dtF2 dtF1 DownloadDirectory\
import sys
import datetime
import time
import requests
import zipfile
import os
#----------------------------------- path declaration with ending "/"
if len(sys.argv) <= 4:
	print("Output Directory path missing")
	print("python downloadFile.py XvX dtF2 dtF1 DownloadDirectory\\")
	sys.exit()
xvx=sys.argv[1].lower()
dtF2=sys.argv[2]
dtF1=sys.argv[3]
if sys.argv[4][-1] == '/' or sys.argv[4][-1] == '\\':
	data_path = sys.argv[4]
else:
	data_path = sys.argv[4] + "/"
givenF2Date=datetime.datetime.strptime(dtF2,"%d%m%Y")
givenF1Date=datetime.datetime.strptime(dtF1,"%d%m%Y")

# print data_path,givenF2Date,givenF1Date,xvx
# sys.exit()
#----------------------------------- date & url function definitions
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

#----------------------------------- Get URL and file names
def getNames(dt,exc):
	if exc == 'b':
		latestDate=dt2BSEdt(latestWeekdayDate(dt))
		ZipURL=dt2BSEURL(latestWeekdayDate(dt))
		ZIPFile=data_path+"EQ_ISINCODE_"+latestDate+".zip"
		CsvFile=ZIPFile.replace(".zip","")
	elif exc == 'n':
		latestDate=dt2NSEdt(latestWeekdayDate(dt))
		ZipURL=dt2NSEURL(latestWeekdayDate(dt))
		ZIPFile=data_path+"cm"+latestDate+"bhav.csv.zip"
		CsvFile=ZIPFile.replace(".zip","")
	return (ZipURL,ZIPFile,CsvFile)

#----------------------------------- Download files and then extract to csv
def download_extract(ZipURL,ZIPFile,CsvFile):
	# downloading
	r = requests.get(ZipURL, stream = True)
	with open(ZIPFile,"wb") as zipFile:
		for chunk in r.iter_content(chunk_size=1024):
			# writing one chunk at a time to zip file
			if chunk:
				zipFile.write(chunk)
	# Extract zip to csv
	with zipfile.ZipFile(ZIPFile,"r") as zip_ref:
		zip_ref.extractall(CsvFile)
	fullCsvFile=CsvFile+"/"+os.listdir(CsvFile)[-1]	
	return fullCsvFile

#-------------------- Main -------------------------
f2URL,f2ZipFIle,F2CsvFIle=getNames(givenF2Date,xvx[0])
f2=download_extract(f2URL,f2ZipFIle,F2CsvFIle)
f1URL,f1ZipFIle,F1CsvFIle=getNames(givenF1Date,xvx[2])
f1=download_extract(f1URL,f1ZipFIle,F1CsvFIle)
print(f2+" "+f1)

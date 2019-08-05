import os, sys
from datetime import datetime

def openDir(targetdir):
	#open directory when done	
	rpath = os.path.realpath(targetdir)
	os.startfile(rpath)

def getBookIDFromPath(inPath):
	temp_path = inPath
	temp_path = os.path.basename(temp_path)
	fname, fext = os.path.splitext(temp_path)
	dbID = int(fname[-4:])
	return(dbID)

	
def readTextFile(filepath):
	try:
	    ofile = open(filepath, 'r', encoding = 'utf-8') 
	    data = ofile.read()
	    return data
	except FileNotFoundError:
	    print("file not found")    
	except Exception as e:
	    print(e)  

def getMatchTuple(inPath):
	maps =  readTextFile(inPath)
	#turn map into tuple list
	tempList = maps.split('\n')
	matchList=[]
	for item in tempList:
		#print(item)
		if (item):
			match = item.split(',')
			#print(match[0], match[1])
			matchList.append((match[0], match[1]))
	return matchList


def getDatedFilePath(initialString, dirOut):
	now = datetime.now()
	dateTime = now.strftime("%Y%m%d_%H%M")
	fileName = initialString + '_' + dateTime + ".txt"
	pathOut =  os.path.join(dirOut, fileName ) 
	return(pathOut)

def getDateStamp():
	getDateStamp = str(datetime.now())
	return(getDateStamp)

def writeListToFile(vlist, vpath):
    with open(vpath, 'w', encoding ='utf-8') as file:
        for item in vlist:    
            file.write(item + "\n")
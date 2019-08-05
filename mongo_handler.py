import json
import os, sys
from pprint import pprint
from system_handler import getDatedFilePath, getDateStamp, writeListToFile, openDir
from pymongo import MongoClient




def insertDBOne(doc, db):
	try:
		
		volumnName = 'google'
		collection = db[volumnName]
		objid = collection.insert_one(doc).inserted_id
		return str(objid)
			
	except Exception as e:
		print('Error: ', e)




def processSingleFile(dataFile, dataDir):
	#dataDir = 'E:/FULLTEXT/GOOGLE/ARCHIVES/RAW'
	#dataFile = 'Dict_Extract00000000.json'
	pathJSON = os.path.join(dataDir, dataFile) 
	pathWordList = 'E:/FULLTEXT/GOOGLE/LOG/Google_Word_List.txt'



	logData = []

	dateStamp = getDateStamp()
	message = 'Started processing ' + dataFile + ' at ' + dateStamp
	logData.append(message)
	print(message)



	message = 'Processing ' + dataFile
	logData.append(message)
	print(message)


	client = MongoClient('localhost', 27017)
	DB_NAME = 'dictionary'
	db = client[DB_NAME]



	jsonData = []

	with open(pathJSON) as json_file:
	    jsonData = json.load(json_file)

	fWordList= open(pathWordList, 'a', encoding = 'utf-8')

	#loop through data
	for itemList in jsonData:
		for item in itemList:
			#pprint(item)
			headWord = item['word']
			#print(headWord, '\n')

			strStatus = insertDBOne(item, db)
			message = 'Inserted ' + headWord + ' at ' + strStatus
			logData.append(message)
			print(message)
			fWordList.write(headWord + '\n')

	fWordList.close()

	return logData





def processJSONDirectory(dataDir, logDir):
	
	#dataDir = 'E:/FULLTEXT/GOOGLE/RAW/DATA010000'

	#logDir = 'E:/FULLTEXT/GOOGLE/LOG'

	logPath = getDatedFilePath('JSON_To_Mongo_Log', logDir )

	print('log path', logPath)


	logData = []

	dateStamp = getDateStamp()
	message = 'Started processing JSON at ' + dateStamp
	logData.append(message)
	print(message)




	dataFileList = os.listdir(dataDir)


	#print(dataFileList)

	for dataFile in dataFileList:
		logData += processSingleFile(dataFile, dataDir)

	

	dateStamp = getDateStamp()
	message = 'Finished processing JSON at ' + dateStamp
	logData.append(message)
	print(message)



	writeListToFile(logData, logPath)
		

def prepareMongoWrite(inPath):
	logDir = 'E:/FULLTEXT/GOOGLE/LOG'
	processJSONDirectory(inPath, logDir)
	openDir(logDir)

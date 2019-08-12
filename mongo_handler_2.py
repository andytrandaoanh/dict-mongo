import json
import os, sys
from pprint import pprint
from system_handler import getDatedFilePath, getDateStamp, writeListToFile, openDir
from pymongo import MongoClient




def insertDBOne(doc, db):
	try:
		
		volumnName = 'lexico'
		collection = db[volumnName]
		objid = collection.insert_one(doc).inserted_id
		return str(objid)
			
	except Exception as e:
		print('Error: ', e)




def processSingleFile(dataFile, dataDir):

	pathJSON = os.path.join(dataDir, dataFile) 
	pathWordList = 'E:/FULLTEXT/LEXICO/LOG/Lexico_Word_List.txt'



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


	#pprint(jsonData)
	try:
		headWord = jsonData['head-word']
		if headWord:
			strStatus = insertDBOne(jsonData, db)
			message = 'Inserted ' + headWord + ' at ' + strStatus
			logData.append(message)
			print(message)
			fWordList.write(headWord + '\n')
	except Exception as e:
		print('error encountered')

	fWordList.close()

	return logData





def processJSONDirectory(dataDir, logDir):
	

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
	logDir = 'E:/FULLTEXT/LEXICO/LOG'
	processJSONDirectory(inPath, logDir)
	openDir(logDir)



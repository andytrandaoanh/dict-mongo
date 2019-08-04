from pymongo import MongoClient
from system_handler import getBookIDFromPath, getMatchTuple
from mysql_data import getSentDict, getBookData

def assembleDoc(bookData, wordForm, sentence, sentID):
	
	newDoc = {'book_id': bookData['book_id'], 
		'book_title': bookData['book_title'], 
		'book_author': bookData['book_author'],
		'book_year': bookData['book_year'],  
		'key_word' : wordForm, 
		'sent_content' : sentence, 
		'sent_num': sentID}
	return newDoc

def insertDBOne(doc, db):
	try:
		
		if doc['key_word']:
		#print(doc['key_word'])
			volumnName = 'vol_' +  doc['key_word'][:1].lower()
			#print (volumnName)
			collection = db[volumnName]
			objid = collection.insert_one(doc).inserted_id
			
	except Exception as e:
		print('Error: ', e)

		

def prepareMongoWrite(inPath):
	#print(inPath)
	bookID = getBookIDFromPath(inPath)
	bookData = getBookData(bookID)
	#print(bookData)	

	client = MongoClient('localhost', 27017)
	DB_NAME = 'lexicon'
	db = client[DB_NAME]

	matchList = getMatchTuple(inPath)
	sentDict = getSentDict(bookID)
	for match in matchList:
		wordForm, sentID = match
		sentence = sentDict[str(sentID)]
		doc = assembleDoc(bookData, wordForm, sentence, int(sentID))
		print('inserting ', wordForm, ' at ', sentID)
		insertDBOne(doc, db)

	#mySent = sentDict['2']
	#print(mySent)
	#print(sentList)
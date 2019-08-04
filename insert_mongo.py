import json
import os, sys
from pprint import pprint

dataDir = 'E:/FULLTEXT/GOOGLE/ARCHIVES/RAW'
dataFile = 'Dict_Extract00000000.json'
pathJSON = os.path.join(dataDir, dataFile) 
jsonData = []

with open(pathJSON) as json_file:
    jsonData = json.load(json_file)

#for item in jsonData:
#	pprint(item)

#print(len(jsonData))

print(jsonData[0][0]['word'])
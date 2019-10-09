from pymongo import MongoClient
import sys
import json
import re


client = MongoClient("localhost", 27017)
sampleDB = client.sampleDB
sampleCollection = sampleDB.sampleCollection

metadataRawDir = "./meta_Kindle_Store.json"

def setup():
    with open(metadataRawDir, "r") as readFile:
        raw = readFile.readline()
        while raw:
            print(raw)
            parsed = re.sub("\{'", "{\"", raw)
            parsed = re.sub("'\}", "\"}", parsed)
            parsed = re.sub("\['", "[\"", parsed)
            parsed = re.sub("'\]", "\"]", parsed)
            
            parsed = re.sub("\], '", "], \"", parsed)
            parsed = re.sub("', \[", "\", [", parsed)
            parsed = re.sub("': \[", "\": [", parsed)
            parsed = re.sub("\}, '", "}, \"", parsed)
            parsed = re.sub("', \{", "\", {", parsed)
            parsed = re.sub("': \{", "\": {", parsed)

            parsed = re.sub("', '", "\", \"", parsed)
            parsed = re.sub("\", '", "\", \"", parsed)
            parsed = re.sub("': '", "\": \"", parsed)
            parsed = re.sub("': \"", "\": \"", parsed)
            print(parsed)

            parsed = json.loads(parsed)
            sampleCollection.insert_one(parsed)
            print(type(parsed))
            break




    """
    print("main - sys.argv: {0}".format(sys.argv))
    collection = sampleCollection

    value = []
    for i in range(3, len(sys.argv)):
        value.append(sys.argv[i])
    print("main - value: {0}".format(value))

    if sys.argv[2] == "GET":
        get(collection, value)
    """

def get(collection, value):
    print("get - collection: {0}; value: {1}".format(collection, value))

def post(collection, value):
    collection.insert_one(value)

def put():
    pass

def delete():
    pass


setup()

from pymongo import MongoClient
import sys
import json
import re


client = MongoClient("localhost", 27017)

metadataRawDir = "./meta_Kindle_Store.json"

LOGDBNAME = "logs"
LOGCOLLECTIONNAME = "logs"
METADATADBNAME = "metadata"
METADATACOLLECTIONNAME = "metadata"
SAMPLEDBNAME = "sample"
SAMPLECOLLECTIONNAME = "sample"



class MongodbCommon:
    def __init__(self, dbName, collectionName):
        self.dbName = None
        self.collectionName = None


        assert (dbName == LOGDBNAME and collectionName == LOGCOLLECTIONNAME) or \
            (dbName == METADATADBNAME and collectionName == METADATACOLLECTIONNAME) or \
            (dbName == SAMPLEDBNAME and collectionName == SAMPLECOLLECTIONNAME)

        if dbName == LOGDBNAME:
            self.dbName = client.logsDb
            self.collectionName = self.dbName.logsCollection
        elif dbName == METADATADBNAME:
            self.dbName = client.metadataDb
            self.collectionName = self.dbName.metadataCollection
        elif dbName == SAMPLEDBNAME:
            self.dbName = client.sampleDb
            self.collectionName = self.dbName.sampleCollection


    def getOne(self, toQuery):
        self.collectionName.find_one(toQuery)

    def get(self, toQuery):
        self.collectionName.find(toQuery)

    def postOne(self, toInsert):
        self.collectionName.insert_one(toInsert)

    def putOne(self, toQuery, toReplace):
        self.collectionName.update_one(toQuery, toReplace)

    def deleteOne(self, toQuery):
        self.collectionName.delete_one(toQuery)


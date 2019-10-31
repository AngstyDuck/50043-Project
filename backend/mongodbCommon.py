from pymongo import MongoClient
import sys
import json
import re
from config import Config

config = Config()

# [database object, collection object]
collections_databases = {
    "logs": [config.logs, config.logs.logs],
    "metadata": [config.metadata, config.metadata.metadata],
    "test": [config.test, config.test.test]
}

class MongodbCommon:
    def __init__(self, dbName, collectionName):
        self.dbName = None
        self.collectionName = None

        assert dbName == collectionName and dbName in collections_databases.keys()

        self.dbName = collections_databases[dbName][0]
        self.collectionname = collections_databases[dbName][1]


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


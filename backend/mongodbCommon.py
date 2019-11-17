from pymongo import MongoClient
import sys
import json
import re
from config import DevConfig

config = DevConfig()

mongo_client = MongoClient(config.MONGO_HOST, 27017)

# [database object, collection object]
collections_databases = {
    "logs": [mongo_client.logs, mongo_client.logs.logs],
    "metadata": [mongo_client.metadata, mongo_client.metadata.metadata],
    "test": [mongo_client.test, mongo_client.test.test]
}

class MongodbCommon:
    def __init__(self, dbName, collectionName):
        self.dbName = None
        self.collectionName = None

        assert dbName == collectionName and dbName in collections_databases.keys()

        self.dbName = collections_databases[dbName][0]
        self.collectionName = collections_databases[dbName][1]


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

    def dropDb(self):
        mongo_client.drop_database(self.dbName)

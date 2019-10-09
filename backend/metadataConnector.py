from pymongo import MongoClient
import sys


client = MongoClient("localhost", 27017)
metadataDB = client.KindleMetadata
metadataCollection = metadataDB.metadataCollection


def main():
    """
    python3 metadataConnector.py [GET/POST/PUT/DELETE] [column 1 value] [column 2 value] ...
    """
    pass

def get():
    pass

def post():
    pass

def put():
    pass

def delete():
    pass

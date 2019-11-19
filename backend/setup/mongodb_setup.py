import sys
sys.path.insert(1, "../")  # to import mongodbCommon (which is in another folder)

from mongodbCommon import MongodbCommon
import json


METADATADIR = "/home/ubuntu/Desktop/50043-Project-lfs/processed_meta_kindle_exported.json"

metadata = MongodbCommon("metadata", "metadata")
with open(METADATADIR, "r") as readFile:
    for line in readFile:
        jsonDict = json.loads(readFile.readline())

        metadata.postOne(jsonDict)
    print("Doneski")


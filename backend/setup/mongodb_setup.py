import sys
sys.path.insert(1, "../")  # to import mongodbCommon (which is in another folder)

from mongodbCommon import MongodbCommon
import json
import os

dirname = os.path.dirname(__file__)
METADATADIR = os.path.abspath(__file__ + "/../../../../50043-Project-lfs/processed_meta_kindle_exported.json")

metadata = MongodbCommon("metadata", "metadata")
with open(METADATADIR, "r") as readFile:
    for line in readFile:
        jsonDict = json.loads(line)

        metadata.postOne(jsonDict)
    print("Doneski")


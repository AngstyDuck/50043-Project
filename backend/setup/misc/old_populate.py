import sys

import os
dir_path = os.path.dirname(os.path.realpath(__file__))
parent_dir = os.path.abspath(os.path.join(dir_path, '..'))
sys.path.insert(1, parent_dir)

import pymysql
from pandas.io import sql
import pandas as pd
import pymysql
pymysql.install_as_MySQLdb()
import json

from mongodbCommon import MongodbCommon


### Fills up MongoDB
METADATADIR = "./50043-project-lfs/processed_meta_kindle_exported.json"

metadata = MongodbCommon("test", "test")
with open(METADATADIR, "r") as readFile:
    for line in readFile:
        readline = readFile.readline()
        # print("readline: {0}".format(readline), file=sys.stderr)
        jsonDict = json.loads(readline)

        metadata.postOne(jsonDict)
    print("Doneski")


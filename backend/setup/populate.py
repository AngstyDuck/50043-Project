import sys
import pymysql
from pandas.io import sql
import pandas as pd
import pymysql
pymysql.install_as_MySQLdb()
from mongodbCommon import MongodbCommon
import json

from config import Config



### Fills up MySQL server
# filename = "./kindle_reviews.csv"
# amazon = pd.read_csv(filename, index_col = [0], low_memory=False)
# amazon = amazon.drop(["Unnamed: 0.1"],axis =1)

# config = Config()
# con = config.mysql_sqlalchemy_engine.connect()

# amazon.to_sql(name='amazonReviews',con=con,if_exists='replace')

# print('CSV IMPORTED')



### Fills up MongoDB
METADATADIR = "./50043-project-lfs/processed_meta_kindle_exported.json"

metadata = MongodbCommon("test", "test")
with open(METADATADIR, "r") as readFile:
    for line in readFile:
        readline = readFile.readline()
        print("readline: {0}".format(readline), file=sys.stderr)
        jsonDict = json.loads(readline)

        metadata.postOne(jsonDict)
    print("Doneski")


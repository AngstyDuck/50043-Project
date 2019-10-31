import pymysql
from pandas.io import sql
import pandas as pd
import pymysql
pymysql.install_as_MySQLdb()

import sys
sys.path.insert(1, "./..")

from config import Config

# sys.path.insert(1, "./..")
# from mongodbCommon import MongodbCommon
# from mysqlCommon import MysqlCommon



# METADATADIR = "./50043-project-lfs/processed_meta_kindle_exported.json"

# metadata = MongodbCommon("test", "test")
# with open(METADATADIR, "r") as readFile:
#     for line in readFile:
#         jsonDict = json.loads(readFile.readline())

#         metadata.postOne(jsonDict)
#     print("Doneski")

filename = "./kindle_reviews.csv"
amazon = pd.read_csv(filename, index_col = [0])
# amazon = amazon.drop(["Unnamed: 0.1"],axis =1)

config = Config()
con = config.mysql_sqlalchemy_engine.connect()

amazon.to_sql(name='amazonReviews',con=con,if_exists='replace')

print('CSV IMPORTED')

import os
import sys
import pymysql.cursors
from pymongo import MongoClient


PROD_MONGO_HOST = "172.31.43.5"
PROD_MONGO_USERNAME = ""
PROD_MONGO_PASSWORD = ""

PROD_MYSQL_HOST = "172.31.34.192"
PROD_MYSQL_USERNAME = "ubuntu"
PROD_MYSQL_PASSWORD = "password"
PROD_MYSQL_DATABAASE = "temp_database"


# class Config(object):
#     SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
#         'mysql+pymysql://user:password@mysql/AMAZON'
#     SQLALCHEMY_TRACK_MODIFICATIONS = False

class Config:
    def __init__(self, stage):
        if stage == "dev":
            pass
        elif stage == "prod":
            self.MONGO_HOST = PROD_MONGO_HOST
            self.MONGO_USERNAME = PROD_MONGO_USERNAME
            self.MONGO_PASSWORD = PROD_MONGO_PASSWORD

            self.MYSQL_HOST = PROD_MYSQL_HOST
            self.MYSQL_USERNAME = PROD_MYSQL_USERNAME
            self.MYSQL_PASSWORD = PROD_MYSQL_PASSWORD
            self.MYSQL_DATABAASE = PROD_MYSQL_DATABAASE

        self.mongo_client = MongoClient(self.MONGO_HOST, 27017)
        self.mongo_db_sample = self.mongo_client.sample
        self.mongo_collection_sample = self.db_sample.sample

        self.mysql_connection = pymysql.connect(
                    host=self.MYSQL_HOST,
                    user=self.MYSQL_USERNAME,
                    password=self.MYSQL_PASSWORD,
                    db=self.MYSQL_DATABASE,
                    charset="utf8mb4",
                    cursorclass=pymysql.cursors.DictCursor
                )
        self.cursor = self.mysql_connection.cursor()

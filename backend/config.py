import os
import sys
# import pymysql.cursors
# from pymongo import MongoClient
# import sqlalchemy



# class Config:
#     def __init__(self):
#         self.MONGO_HOST = "172.31.43.5"
#         self.MONGO_USERNAME = ""
#         self.MONGO_PASSWORD = ""

#         self.MYSQL_HOST = "172.31.34.192"
#         self.MYSQL_USERNAME = "ubuntu"
#         self.MYSQL_PASSWORD = "password"
#         self.MYSQL_DATABASE = "temp_database"

        
#         self.mongo_client = MongoClient(self.MONGO_HOST, 27017)

#         self.mongo_db_metadata = self.mongo_client.metadata
#         self.mongo_collection_metadata = self.mongo_db_metadata.metadata
        
#         self.mongo_db_logs = self.mongo_client.logs
#         self.mongo_collection_logs = self.mongo_db_logs.logs
        
#         self.mongo_db_test = self.mongo_client.test
#         self.mongo_collection_test = self.mongo_db_test.test

#         self.mysql_pymysql_connection = pymysql.connect(
#                     host=self.MYSQL_HOST,
#                     user=self.MYSQL_USERNAME,
#                     password=self.MYSQL_PASSWORD,
#                     db=self.MYSQL_DATABASE,
#                     charset="utf8mb4",
#                     cursorclass=pymysql.cursors.DictCursor
#                 )
        
#         self.mysql_sqlalchemy_engine = sqlalchemy.create_engine("mysql://{0}:{1}@{2}/{3}".format(
#             self.MYSQL_HOST,
#             self.MYSQL_PASSWORD,
#             self.MYSQL_HOST,
#             self.MYSQL_DATABASE
#         ))

class DevConfig(object):
    MONGO_HOST = "172.31.43.5"
    MONGO_USERNAME = ""
    MONGO_PASSWORD = ""

    MYSQL_HOST = "172.31.34.192"
    MYSQL_USERNAME = "ubuntu"
    MYSQL_PASSWORD = "password"
    MYSQL_DATABASE = "temp_database"

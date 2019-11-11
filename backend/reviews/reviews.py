import os
import sys
from flask import Flask
sys.path.insert(1, "./..")
from config import Config





app = Flask(__name__)

"""
app.config.update(
            MONGO_HOST = self.MONGO_HOST,
            MONGO_USERNAME = self.MONGO_USERNAME,
            MONGO_PASSWORD = self.MONGO_PASSWORD,
            
            MYSQL_HOST = self.MYSQL_HOST,
            MYSQL_USERNAME = self.MYSQL_USERNAME,
            MYSQL_PASSWORD = self.MYSQL_PASSWORD,
            MYSQL_DATABASE = self.MYSQL_DATABASE,
            
            mongo_client = self.mongo_client
            
            mongo_db_metadata = self.mongo_db_metadata
            mongo_collection_metadata = self.mongo_collection_metadata
            
            mongo_db_logs = self.mongo_db_logs
            mongo_collection_logs = self.mongo_collection_logs
            
            mongo_db_test = self.mongo_db_test
            mongo_collection_test = self.mongo_collection_test
            
            mysql_pymysql_connection = self.mysql_pymysql_connection
            
            mysql_sqlalchemy_engine = self.mysql_sqlalchemy_engine
        )
"""

import routes


# from config import Config
# from flask_pymongo import PyMongo
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
#SQL
# app = Flask(__name__)

# app.config.from_object(Config)
# db = SQLAlchemy(app)
# migrate = Migrate(app, db)

#Mongo AMAZONMETADATA

# app.config.from_object(MongoConfig)
# app.config['MONGO_URI'] = "mongodb://mongo:27017/AMAZONMETADATA"
# mongo = PyMongo(app)

#Mongo LOGS

# app.config.from_object(LogConfig)
# logActivity = PyMongo(app)

# from app import routes, models
# import routes



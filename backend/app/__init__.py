import os
# import pymysql.cursors
# from pymongo import MongoClient
# import sqlalchemy

import sys
from flask import Flask
sys.path.insert(1, "./..")
import config


# globally accessible libraries
global mongodb
global sqlalchemy
global pymysql




def create_app():
    """
    App factory
    """
    # initialize core application
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_pyfile("../config.py", silent=False)

    # initialize plugins
    """
    mongodb = MongoClient(config.DevConfig.MONGO_HOST, 27017)
    pymysql = pymysql.connect(
                host=config.DevConfig.MYSQL_HOST,
                user=config.DevConfig.MYSQL_USERNAME,
                password=config.DevConfig.MYSQL_PASSWORD,
                db=config.DevConfig.MYSQL_DATABASE,
                charset="utf8mb4",
                cursorclass=pymysql.cursors.DictCursor
            )
    sqlalchemy = sqlalchemy.create_engine("mysql://{0}:{1}@{2}/{3}".format(
        config.DevConfig.MYSQL_HOST,
        config.DevConfig.MYSQL_PASSWORD,
        config.DevConfig.MYSQL_HOST,
        config.DevConfig.MYSQL_DATABASE
    ))
    """

    with app.app_context():
        from app.modules import books, reviews
        app.register_blueprint(reviews.module)
        # app.register_blueprint(books.module)

        return app



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



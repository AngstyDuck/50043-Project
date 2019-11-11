import os
import pymysql.cursors
from pymongo import MongoClient
import sqlalchemy

import sys
from flask import Flask
sys.path.insert(1, "./..")
sys.path.insert(1, "./app/modules")
import config


# globally accessible libraries
global MongoDB
global SQLAlchemy
global PyMySQL



def create_app():
    """
    App factory
    """
    # initialize core application
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_pyfile("../config.py", silent=False)

    # initialize plugins
    
    MongoDB = MongoClient(config.DevConfig.MONGO_HOST, 27017)
    PyMySQL = pymysql.connect(
                host=config.DevConfig.MYSQL_HOST,
                user=config.DevConfig.MYSQL_USERNAME,
                password=config.DevConfig.MYSQL_PASSWORD,
                db=config.DevConfig.MYSQL_DATABASE,
                charset="utf8mb4",
                cursorclass=pymysql.cursors.DictCursor
            )
    SQLAlchemy = sqlalchemy.create_engine("mysql+pymysql://{0}:{1}@{2}/{3}".format(
        config.DevConfig.MYSQL_HOST,
        config.DevConfig.MYSQL_PASSWORD,
        config.DevConfig.MYSQL_HOST,
        config.DevConfig.MYSQL_DATABASE
    ))
    

    with app.app_context():
        import reviews
        # import app.modules.books
        app.register_blueprint(reviews.module)
        # app.register_blueprint(books.module)

        return app

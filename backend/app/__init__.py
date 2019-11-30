import os
import pymysql.cursors
from pymongo import MongoClient
import sqlalchemy

import sys
from flask import Flask
sys.path.insert(1, "./..")
sys.path.insert(1, "./app/modules")
sys.path.insert(1, "./app")
import config

import logging
from logger import Custom_Request_Logger

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
    app.config["JSONIFY_PRETTYPRINT_REGULAR"] = True  # PRETTY JSON AW YIS

    # add config values
    flask_env = os.environ["FLASK_ENV"]
    if flask_env == "local":
        app.config.from_object("config.Config_local")
    elif flask_env == "remoteDev":
        app.config.from_object("config.Config_remoteDev")

    # initialize db plugins 
    MongoDB = MongoClient(app.config["MONGO_HOST"], 27017)
    PyMySQL = pymysql.connect(
                host=app.config["MYSQL_HOST"],
                user=app.config["MYSQL_USERNAME"],
                password=app.config["MYSQL_PASSWORD"],
                db=app.config["MYSQL_DATABASE"],
                charset="utf8mb4",
                cursorclass=pymysql.cursors.DictCursor
            )
    SQLAlchemy = sqlalchemy.create_engine("mysql+pymysql://{0}:{1}@{2}/{3}".format(
        app.config["MYSQL_HOST"],
        app.config["MYSQL_PASSWORD"],
        app.config["MYSQL_HOST"],
        app.config["MYSQL_DATABASE"]
    ))

    # these objects are named in accordance to how each of their tutorials address them for ease of usage
    app.config.from_mapping(
                MONGODB_CLIENT = MongoDB,
                PYMYSQL_CONNECTION = PyMySQL,
                SQLALCHEMY_ENGINE = SQLAlchemy
            )

    # configure logging (before app initialization)
    custom_logger = Custom_Request_Logger()
    app.logger.setLevel(logging.INFO)
    app.logger.addHandler(custom_logger)
    
    with app.app_context():
        import reviews, books
        app.register_blueprint(reviews.module)
        app.register_blueprint(books.module)

        return app

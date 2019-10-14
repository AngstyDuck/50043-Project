from flask import Flask
from config import Config, MongoConfig

from flask_pymongo import PyMongo


from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


#SQL

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

#Mongo AMAZONMETADATA

app.config.from_object(MongoConfig)

mongo = PyMongo(app)


from app import routes, models



from flask import Flask
from config import Config, MongoConfig,LogConfig
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

#Mongo LOGS

app.config.from_object(LogConfig)
logActivity = PyMongo(app)



from app import routes, models

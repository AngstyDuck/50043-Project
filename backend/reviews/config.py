import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'mysql+pymysql://root:password@localhost/AMAZON'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class MongoConfig(object):
    MONGO_URI = "mongodb://localhost:27017/AMAZONMETADATA"

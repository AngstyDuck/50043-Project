import pymongo

from pymongo import MongoClient

client = MongoClient('mongo',27017)
db = client['AMAZONMETADATA']
amazon = db['AMAZONMETADATA']

with open('./mongo-seed/processed_meta_kindle_exported.json') as f:
    file_data = json.load(f)



amazon.insert_one(file_data)
client.close()

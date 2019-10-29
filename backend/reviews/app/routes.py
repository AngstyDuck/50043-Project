import os
from flask import render_template, make_response,jsonify
from app import app, models #, mongo
import logging
from time import sleep
import sys
from pymongo import MongoClient

client = MongoClient('mongo',43440)
mongo = client.AMAZONMETADATA


# sys.path.insert(1,'./app')
# from mongolog.handlers import MongoHandler
#
# from mongodbCommon import MongodbCommon as mdb
#
#
# logging.basicConfig(filename='./database.log',level=logging.DEBUG,format='%(asctime)s %(levelname)s %(name)s %(threadName)s : %(message)s')
# # logging.getLogger('logs').addHandler(MongoHandler.to(db='logs', collection='logs'))
# # logging.setLevel(logging.DEBUG)
#
# from pymongo import MongoClient
# from pymongo import ASCENDING
# import datetime
#
# client = MongoClient('mongo',4545)
# db = client.logs
# log_collection = db.logs
# log_collection.ensure_index([("timestamp", ASCENDING)])


# def log(msg):
#     """Log `msg` to MongoDB log"""
#     entry = {}
#     entry['name'] = 'logs'
#     entry['timestamp'] = datetime.datetime.utcnow()
#     entry['msg'] = msg
#     log_collection.insert(entry)

@app.route('/check/<index>', methods = ['GET'])
def displayData(index):
    results = models.Reviews.query.filter_by(index = index)
    reviews = []
    for result in results:
        reviews.append(str(result.id))
    # app.logger.info('Processing SQL request')
    # log('Processing SQL request')
    return str(reviews[0])

@app.route("/home/<type>/<asin>")
def displayMeta(asin,type):
    # online_users = mongo.db.users.find({"online": True})
    try:
        metadata = mongo.AMAZONMETADATA.find({'asin': asin})
        results = []
        for d in metadata:
            results.append(d[type])
        # app.logger.info('Processing MONGO request')
        # log('Processing MONGO request')
        return f'{results[0]} displayed'
    except Exception as e:
        # app.logger.info('Error 404')
        # log('Error 404')
        return str(e)
#
# @app.route('/log')
# def stream():
#     def generate():
#         with open('database.log') as f:
#             while True:
#                 yield f.read()
#                 sleep(0.5)
#
#     return app.response_class(generate(), mimetype='text/plain')
#
# @app.route('/savelog')
# def storeLog():
#     logMongo = mdb('logs', 'logs')
#     logging = logMongo.getOne('')
#     return str(logging)


'''
Features not implemented yet
'''

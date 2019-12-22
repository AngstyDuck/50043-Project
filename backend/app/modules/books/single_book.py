#from app import sqlalchem
from flask import jsonify, request
#from sqlalchemy import func
import sys
import json
import copy
import time
import random
from datetime import datetime
from flask import Flask
from flask import current_app as app
from app.logger import request_log_wrapper


def _single_book(asin):
    """
    Returns 1 book with given asin 
    """

    time.sleep(random.random()*2)
    print("ping - _single_book")
    asin = str(asin)
    query = "SELECT avg(overall) FROM {0} GROUP BY asin HAVING asin=\'{1}\'".format(app.config["MYSQL_TABLE_REVIEWS"], asin)
    avgRatingInt = 0
    output = {}

    connection = app.config["PYMYSQL_CONNECTION"]
    with connection.cursor() as cursor:
        cursor.execute(query)
        query_result = cursor.fetchone()

        if query_result is not None:
            avgRating = query_result['avg(overall)']
            avgRatingInt = float(avgRating)
        else:
            avgRatingInt = 0

    connectionMongo = app.config["MONGODB_CLIENT"]
    mongodb = connectionMongo['metadata']
    metadata = mongodb['metadata']

    mongo_result = metadata.find_one({"asin": asin})

    if mongo_result is not None:
        final_related_list = []
        if 'related' in mongo_result:
            related = mongo_result['related']
            related_list = []

            for i in related:
                for j in related[i]:
                    related_list.append(j)

            related_results = metadata.find( { 'asin': { '$in': related_list } } )

            for k in related_results:
                temp = {}
                temp['asin'] = k['asin']
                temp['imUrl'] = k['imUrl']
                final_related_list.append(temp)

        inner = {}
        inner['asin'] = mongo_result['asin']

        if 'price' in mongo_result:
            inner['price'] = mongo_result['price']
        else:
            inner['price'] = None

        if avgRatingInt is not None:
            inner['averageRating'] = round(avgRatingInt,2)
        else:
            inner['averageRating'] = None

        if 'imUrl' in mongo_result:
            inner['imUrl'] = mongo_result['imUrl']
        else:
            inner['imUrl'] = None

        inner['related'] = final_related_list

        inner['categories'] = mongo_result['categories']

        output['book'] = inner

    else:
        output['book'] = {}

    # for logging received requests
    log_msg = request_log_wrapper(request)
    app.logger.info(log_msg)

    return jsonify(output)

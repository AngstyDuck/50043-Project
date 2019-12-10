from flask import jsonify, request
import sys
import json
# import copy
# from datetime import datetime
from flask import Flask
from flask import current_app as app

from app.logger import request_log_wrapper

def _filter_books():

    print("ping - _filter_books")
    start = request.args.get("start_list")  # currently unused
    _end = request.args.get("end_list")  # currently unused
    filtertext = request.args.get("filtertext")
    limit = 20
    output = {}
    print("start: {0}; end: {1}; filtertext: {2}".format(start, _end, filtertext))

    # declare clients for mongo & mysql
    mongo = app.config["MONGODB_CLIENT"]
    metadata = mongo.metadata.metadata

    connection = app.config["PYMYSQL_CONNECTION"]


    # get asin & categories to search for filtertext
    cat_search_list = metadata.find( {}, { '_id':0,'asin':1,'categories':1 } )
    matches = []
    for j in cat_search_list:
        asin = j['asin']
        categories = j['categories']

        # search filtertext in categories (nested list)
        found = False
        for cat_list in categories:
            for category in cat_list:
                if filtertext.lower() in category.lower():
                    matches.append(asin)
                    found = True
                    break
            if found: break
        if len(matches) == limit: break
    print("Found {0} matches: {1}".format(len(matches), matches))


    # get books from database
    books = []
    for asin in matches:
        temp_book = {}
        json_book = metadata.find_one( { 'asin': asin }, { '_id':0,'title':1,'asin':1,'imUrl':1,'categories':1 } )

        temp_book['asin'] = json_book['asin']

        if 'title' in json_book:
            temp_book['title'] = json_book['title']
        else:
            temp_book['title'] = None

        if 'imUrl' in json_book:
            temp_book['imUrl'] = json_book['imUrl']
        else:
            temp_book['imUrl'] = None

        temp_book['categories'] = json_book['categories']

        # averageRating
        # query = "SELECT avg(overall) FROM {0} GROUP BY asin HAVING asin=\'{1}\'".format(app.config["MYSQL_TABLE_REVIEWS"], asin)
        # connection = app.config["PYMYSQL_CONNECTION"].cursor()
        # with connection as cursor:
            # cursor.execute(query)
            # query_result = cursor.fetchone()
            # if query_result:
                # averageRating = query_result["avg(overall)"]
                # temp_book['averageRating'] = float(averageRating)
            # else:
                # temp_book['averageRating'] = 0
        # cursor.close()

        # add book to books
        books.append(temp_book)

    output['books'] = books
    print("filtered!")

    # for logging received requests
    log_msg = request_log_wrapper(request)
    app.logger.info(log_msg)

    return jsonify(output)



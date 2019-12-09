from flask import jsonify,request
import sys
import json
# import copy
# from datetime import datetime
from flask import Flask
from flask import current_app as app

from app.logger import request_log_wrapper

def _search_books():
    print("ping - _search_books")
    start = request.args.get("start_list")  # currently unused
    _end = request.args.get("end_list")  # currently unused
    searchtext = request.args.get("searchtext")
    filtertext = request.args.get("filtertext")
    limit = 60
    output = {}
    print("start: {0}; end: {1}; searchtext: {2}; filtertext: {3}".format(start, _end, searchtext, filtertext))

    # declare clients for mongo & mysql
    mongo = app.config["MONGODB_CLIENT"]
    metadata = mongo.metadata.metadata

    connection = app.config["PYMYSQL_CONNECTION"]


    ## STEP 1: Search & filter, get asin of matched book
    # (a) get asin & title to search for searchtext (& categories to search for filtertext if present)
    if filtertext:
        met_data = metadata.find( {}, { '_id':0,'asin':1,'title': 1,'categories':1 } )
    else:
        met_data = metadata.find( {}, { '_id':0,'asin':1,'title': 1 } )

    matches = []
    matches_cat = []
    for j in met_data:

        # (b) get asin & title (& categories) from query
        asin = j['asin']

        if 'title' in j:
            title = j['title']
        else:
            title = None

        if 'categories' in j:
            categories = j['categories']
        else:
            categories = None

        # (c) search for searchtext in title
        if title:
            # use casefold for cases of non-Latin characters
            if searchtext.casefold() in title.casefold():

                # (d) check if category matches filtertext (if present)
                if categories:
                    found = False
                    for cat_list in categories:
                        for category in cat_list:
                            if filtertext.lower() in category.lower():
                                found = True
                                break
                        if found: break

                    # if searchtext and filtertext matches, add to matches
                    if found: matches.append(asin)
                else:
                    matches.append(asin)

                if len(matches) == limit: break

    print("Found {0} matches: {1}".format(len(matches), matches))


    ## STEP 2: get desired fields from asin
    books = []
    categorys = []

    # (a) get books from database
    for asin in matches:
        temp_book = {}
        json_book = metadata.find_one( { 'asin': asin }, { '_id':0,'title':1,'asin':1,'imUrl':1,'categories':1 } )

        # (b) grab desired fields
        temp_book['asin'] = json_book['asin']

        temp_book['title'] = json_book['title']

        if 'imUrl' in json_book:
            temp_book['imUrl'] = json_book['imUrl']
        else:
            temp_book['imUrl'] = None

        temp_book['categories'] = json_book['categories']

        # (c) calculate averageRating
        query = "SELECT avg(overall) FROM {0} GROUP BY asin HAVING asin=\'{1}\'".format(app.config["MYSQL_TABLE_REVIEWS"], asin)
        connection = app.config["PYMYSQL_CONNECTION"].cursor()
        with connection as cursor:
            cursor.execute(query)
            query_result = cursor.fetchone()
            if query_result:
                averageRating = query_result["avg(overall)"]
                temp_book['averageRating'] = float(averageRating)
            else:
                temp_book['averageRating'] = 0
        cursor.close()

        # (d) add book to books
        books.append(temp_book)

        # (e) get categories from current book
        for cat_list in temp_book['categories']:
            for category in cat_list:
                if category not in categorys:
                    categorys.append(category)

        # (f) format categorys
        categorys2 = []
        for category in categorys:
            temp_cat = {}
            temp_cat['category'] = category
            categorys2.append(temp_cat)

    output['books'] = books
    # output['categories'] = categorys2

    # for logging received requests
    log_msg = request_log_wrapper(request)
    app.logger.info(log_msg)

    return jsonify(output)



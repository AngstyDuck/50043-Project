import random
from flask import jsonify, request
from flask import current_app as app
import numpy as np

def _main_top_row_books():
    """
    Returns 15 books to populate top row of front-page
    """
    asins = ["B0002IQ15S", "B000F83TEQ", "B000FA5RE4", "B000FA5UXC", "B000FA5SHK", "B000FA5M6M", "B000FA5PV4", "B000FA5MQ2", "B000FA5KJQ", "B000FA66XU", "B000FA5ZEG", "B000FA5TOM", "B000FA5TF6", "B000FA5V2C", "B000FA61JY"]
    # declare pymysql client
    connection = app.config["PYMYSQL_CONNECTION"]

    # declare pymongo client
    mongo = app.config["MONGODB_CLIENT"]
    metadata = mongo.metadata.metadata

    finaldict = {}
    outerlist = []
    outerlist_best = []

    met_data = metadata.find( { 'asin': { '$in' : asins } }, { '_id':0,'title':1,'asin':1,'imUrl':1,'categories':1} )

    for j in met_data:
        count = 0
        temp = {}

        if 'title' in j:
            temp['title'] = j['title']

        temp['asin'] = j['asin']

        # averageRating = db.session.query(func.avg(amazonreviews.overall)).group_by(amazonreviews.asin).filter_by(asin=j['asin']).scalar()

        # pymysql query
        # query = "SELECT AVG(overall) FROM {0} WHERE asin=\'{1}\'".format(app.config["MYSQL_TABLE_REVIEWS"], temp['asin'])
        # with connection.cursor() as cursor:
            # print("query: {0}".format(query))
            # cursor.execute(query)
            # query_result = cursor.fetchone()
            # averageRating = query_result["AVG(overall)"]
            # if averageRating:
                # averageRating = float(averageRating)
                # temp['averageRating'] = averageRating
            # else:
                # temp['averageRating'] = 0
        # cursor.close()

        if 'imUrl' in j:
            temp['imUrl'] = j['imUrl']
        else:
            temp['imUrl'] = None

        temp['categories'] = j['categories']

        if len(outerlist) < 10:
            outerlist.append(temp)
        else:
            outerlist_best.append(temp)

    finaldict['related'] = outerlist
    finaldict['best'] = outerlist_best

    return(jsonify(finaldict))

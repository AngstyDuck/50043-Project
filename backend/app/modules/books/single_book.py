from app import sqlalchem
from flask import jsonify
from sqlalchemy import func
import sys
import json
import copy
from datetime import datetime
from flask import Flask
from flask import current_app as app

def _single_book(asin):
    query = "SELECT avg(overall) FROM {0} GROUP BY asin WHERE asin=\'{1}\'".format(app.config["MYSQL_TABLE_REVIEWS"], str(asin))
   '''
    averageRating = sqlalchem.session.query(func.avg(amazonreviews.overall)).group_by(amazonreviews.asin).filter_by(asin=asin).scalar()
    met_data = metadata.find_one({"asin": asin})

    final_related_list = []
    if 'related' in met_data:
        related = met_data['related']
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


    output = {}
    inner = {}
    inner['asin'] = met_data['asin']

    if 'price' in met_data:
        inner['price'] = met_data['price']
    else:
        inner['price'] = None

    if averageRating is not None:
        inner['averageRating'] = round(float(averageRating),2)
    else:
        inner['averageRating'] = None

    if 'imUrl' in met_data:
        inner['imUrl'] = met_data['imUrl']
    else:
        inner['imUrl'] = None

    inner['related'] = final_related_list

    inner['catergories'] = met_data['categories']

    output['book'] = inner

    print(output)

    return jsonify(output)
'''

   return (type(query)), query

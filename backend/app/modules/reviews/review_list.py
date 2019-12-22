import sys
import json
import copy
from datetime import datetime
from flask import Flask, request
from flask import current_app as app
from app.logger import request_log_wrapper


def _review_list(asin):
    """
    Returns a list of reviews for a book
    """
    
    print("ping - _review_list")
    # asin_number = request.args.get("asin_number")
    asin_number = asin
    query = "SELECT * FROM {0} WHERE asin=\'{1}\'".format(app.config["MYSQL_TABLE_REVIEWS"], str(asin_number))
    connection = app.config["PYMYSQL_CONNECTION"].cursor()
    with connection as cursor:
        cursor.execute(query)
        query_result = cursor.fetchall()
        query_result_edited = copy.deepcopy(query_result)

        for i in query_result_edited:
            # change datatype of column 'helpful' from string to list
            # e.g. from "[0, 0]" to [0, 0] of datatype 'list'
            helpful_val = i["helpful"]
            helpful_val = helpful_val.split(", ")
            helpful_val[0] = int(helpful_val[0][1:])
            helpful_val[1] = int(helpful_val[1][:-1])
            i["helpful"] = helpful_val

            # change value reviewTime to match format "month date, year"
            reviewTime_val = int(i["unixReviewTime"])
            reviewTime_val = datetime.fromtimestamp(reviewTime_val)
            reviewTime_val = reviewTime_val.strftime("%B %d, %Y")
            i["reviewTime"] = reviewTime_val

            # remove unnecessary columns
            del i["unixReviewTime"]
            del i["id"]

        output = {"reviews": query_result_edited}
        output = json.dumps(output, sort_keys=True, indent=4)

    cursor.close()

    # for logging received requests
    log_msg = request_log_wrapper(request)
    app.logger.info(log_msg)

    return output

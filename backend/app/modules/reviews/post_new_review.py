from flask import request
from datetime import datetime
from flask import current_app as app
from app.logger import request_log_wrapper


def _post_new_review():
    """
    Posts new review on a book
    """
    print("ping - _post_new_review")
    body = request.json
    
    temp_val = []
    temp_val.append("'{0}'".format(body["asin"]))  # asin - expected str
    temp_val.append("'[0, 0]'")  # helpful - HARDCODED
    temp_val.append(str(body["overall"]))  # overall - expected int
    temp_val.append("'{0}'".format(body["reviewText"]))  # reviewText - expected str
    temp_val.append("'2019-11-17 00:00:00'")  # reviewTime - HARDCODED
    temp_val.append("'{0}'".format(body["reviewerName"]))  # reviewerName - expected str
    temp_val.append("'{0}'".format(body["summary"]))  # summary - expected str
    temp_val.append(str(datetime.timestamp(datetime.now())))  # unixReviewTime - CODED
    temp_val = ",".join(temp_val)

    query = "INSERT INTO {0} (asin, helpful, overall, reviewText, reviewTime, reviewerName, summary, unixReviewTime) VALUES ({1})".format(app.config["MYSQL_TABLE_REVIEWS"], temp_val)

    # print("------ query: {0}".format(query))
    connection = app.config["PYMYSQL_CONNECTION"]
    with connection.cursor() as cursor:
        cursor.execute(query)
        query_result = cursor.fetchall()
        print(query_result)
    connection.commit()

    # for logging received requests
    log_msg = request_log_wrapper(request)
    app.logger.info(log_msg)

    return {"message": "OK"}

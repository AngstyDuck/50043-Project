from flask import current_app as app
import logging
import sys


"""
The custom logger is based off a class of logger that python inherently provides. It is customised to add entries to the database whenever a new request is made.
"""

class Custom_Request_Logger(logging.Handler):
    def __init__(self):
        logging.Handler.__init__(self, logging.NOTSET)

    def emit(self, value):
        # print("log type: {0}".format(type(value)))
        # print("from logger: {0}".format(value.msg), file=sys.stderr)
        connection = app.config["PYMYSQL_CONNECTION"]
        query = "INSERT INTO logs (log_msg) VALUES (\'{0}\')".format(value.msg)
        print("----- query: {0}".format(query))
        with connection.cursor() as cursor:
            cursor.execute(query)
            query_result = cursor.fetchone()
            # print("query_result: {0}".format(query_result))
        connection.commit()

def request_log_wrapper(rq):
    """
    Adapted from Common Log Format
    https://en.wikipedia.org/wiki/Common_Log_Format
    """
    url = str(rq.full_path)
    http_method = str(rq.method)
    source_ip = str(rq.remote_addr)

    return "REQUEST LOG - {0} {1} {2} HTTP/1.0 200".format(source_ip, http_method, url)



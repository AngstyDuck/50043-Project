from flask import current_app as app
import logging
import sys


class Custom_Request_Logger(logging.Handler):
    def __init__(self):
        logging.Handler.__init__(self, logging.NOTSET)

    def emit(self, value):
        print("log type: {0}".format(type(value)))
        print("from logger: {0}".format(value.msg), file=sys.stderr)
        connection = app.config["PYMYSQL_CONNECTION"]
        query = "INSERT INTO logs (log_msg) VALUES (\'{0}\')".format(value.msg)
        with connection.cursor() as cursor:
            cursor.execute(query)
            query_result = cursor.fetchone()
            print("query_result: {0}".format(query_result))
        connection.commit()

def request_log_wrapper(rq):
        url = str(rq.full_path)
        http_method = str(rq.method)
        query_params = str(rq.args)
        data_body = str(rq.json)
        source_ip = str(rq.remote_addr)

        return "REQUEST LOG- url:{0}; http_method: {1}; query_params: {2}; data_body: {3}; source_ip: {4}".format(url, http_method, query_params, data_body, source_ip)


import sys
import pymysql.cursors
from config import Config

config = Config()

tables = {}

class MysqlCommon:
    def __init__(self, tableName):
        self.table = tableName
        

    def show_tables(self):
        """
        Prints all tables
        """
        try:
            connection = config.mysql_connection
            with connection.cursor() as cursor:
                query = "SHOW TABLES"
                cursor.execute(query)
                result = cursor.fetchone()
                print("Result: {0}".format(result), file=sys.stderr)  # the file parameter ensures that print is displayed when run by flask app
                return str(result)
        except Exception as e:
            print("ERROR: {0}".format(e), file=sys.stderr)
        finally:
            connection.close()

    def custom_query(self, query):
        """
        Executes custom query
        """
        try:
            connection = config.mysql_connection
            with connection.cursor() as cursor:
                cursor.execute(query)
        except Exception as e:
            print("ERROR: {0}".format(e), file=sys.stderr)
        finally:
            connection.close()

    # def insert_one(self, row):
    #     """
    #     Insert one row to table

    #     row is a list object containing elements of the row (in order)
    #     """
    #     try:
    #         connection = config.mysql_connection
    #         with connection.cursor() as cursor:
    #             query = "INSERT INTO {0} VALUES ({1})".format(self.table, list_to_string(row))
    #             cursor.execute(query)

    #         connection.commit()
    #     except Exception as e:
    #         print("ERROR: {0}".format(e), file=sys.stderr)
    #     finally:
    #         connection.close()

    # def list_to_string(self, input_list):
    #     """
    #     input: [1,2,3]
    #     output: '1,2,3'
    #     """
    #     output = ""
    #     for i in input_list:
    #         output += (i + ",")

    #     # remove the "," at the end
    #     if len(output) >= 3:
    #         return output[:-1]
    #     else:
    #         return output

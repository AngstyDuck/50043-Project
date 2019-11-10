import json
import pymysql
from pandas.io import sql
import pandas as pd
import pymysql
pymysql.install_as_MySQLdb()
# from sqlalchemy import create_engine

filename = 'Test.csv'

amazon = pd.read_csv(filename, index_col = [0])
amazon = amazon.drop(["Unnamed: 0.1"],axis =1)
# with open(filename) as json_file:
#     data = json_file.readlines()
#     data = list(map(json.loads, data))
#
# amazon = pd.DataFrame(data)
#
# print(amazon)
# print(amazon.columns)



db = pymysql.connect("localhost","root","root")

#db.cursor().execute('create database if not exists AMAZON')

# sqlQuery = ['use AMAZON']
# for i in sqlQuery:
#     db.cursor().execute(i)

from sqlalchemy import create_engine

engine = create_engine('mysql://root:root@localhost/AMAZON')
con = engine.connect()
amazon.to_sql(name='amazonReviews',con=con,if_exists='replace')

print('CSV IMPORTED')




















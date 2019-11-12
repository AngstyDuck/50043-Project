import json
import pymysql
from pandas.io import sql
import pandas as pd
import pymysql
pymysql.install_as_MySQLdb()

filename = '.csv'

amazon = pd.read_csv(filename, index_col = [0])
amazon = amazon.drop(["Unnamed: 0.1"],axis =1)


db = pymysql.connect("localhost","ubuntu","password")

from sqlalchemy import create_engine

engine = create_engine('mysql://ubuntu:password@localhost/AMAZON')
con = engine.connect()
amazon.to_sql(name='amazonReviews',con=con,if_exists='replace')

print('CSV IMPORTED')




















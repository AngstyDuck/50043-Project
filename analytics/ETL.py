MONGO_HOST = "18.139.108.110"
MONGO_USERNAME = ""
MONGO_PASSWORD = ""

MYSQL_HOST = "54.169.82.238"
MYSQL_USERNAME = "root"
MYSQL_PASSWORD = "password"
MYSQL_DATABASE = "amazon"
MYSQL_TABLE_REVIEWS = "amazonreviews"

import csv
import mysql.connector
from mysql.connector import errorcode
from pymongo import MongoClient
import json

def connectMySQL():
	#connection
	config = {'user': MYSQL_USERNAME,
	'password': MYSQL_PASSWORD,
	'host': MYSQL_HOST,
	'database': MYSQL_DATABASE,
	'raise_on_warnings': True
	}

	connection = mysql.connector.connect(**config)
	query = "SELECT asin,reviewText FROM {0}".format(MYSQL_TABLE_REVIEWS)
	cursor = connection.cursor()
	print("Successfully connected to mysql")
	cursor.execute(query)
	result = cursor.fetchall()
	cursor.close()

	f = open("mysql.csv","w")
	for i in result:
		f.write(str(i).strip("()")+"\n")

	f.close()
	print("Finished")
	# return("Billio Is Awesome")

def connectMongo():
	mongo_client = MongoClient(MONGO_HOST, 27017)
	metadata = mongo_client.metadata.metadata
	met_data = metadata.find({}, {'asin':1,'price':1, '_id':0})
	f = open("mongo.json","w")
	for j in (met_data):
		if ('price' in j):
			f.write(json.dumps(j)+"\n")
	f.close()

	print('finished importing MongoDB data')
connectMongo()
connectMySQL()

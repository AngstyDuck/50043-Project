#!/bin/bash

echo "STARTING DOWNLOAD MONGO AND SQL DATA"

python3.7 ./analysis/etl.py

echo "PUTTING DATA INTO HADOOP"

hadoop fs -mkdir /input/
hadoop fs -put /input/mysql.csv
hadoop fs -put /input/mongo.json

echo "STARTING ANALYSIS"

export PYSPARK_PYTHON=python3.7

python3.7 ./analysis/analytics.py

echo "FINISHED ANALYSIS"

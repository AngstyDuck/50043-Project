#!/bin/bash

# Insert reviews into mysql
echo "Inserting book reviews into mysql..."
mysql -u root -p < ~/Desktop/50043-Project/backend/setup/mysql_setup.sql

# Insert metadata into mongodb
# echo "Inserting metadata into mongo..."
# source ../venvBackend/bin/activate  # use existing python virtual environment to execute the subsequent file
# python3 mongodb_setup.py

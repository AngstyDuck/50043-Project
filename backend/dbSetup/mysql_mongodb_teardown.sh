#!/bin/bash

# Removing reviews from  mysql
echo "Removing book reviews into mysql..."
mysql -u root -p < ./mysql_teardown.sql

# Removing metadata from mongo
# source ../venvBackend/bin/activate  # use existing python virtual environment to execute the subsequent file
# python3 mongodb_teardown.py



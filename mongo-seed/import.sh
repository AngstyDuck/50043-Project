#! /bin/bash

mongod --port 43440
mongoimport --host mongo --db AMAZONMETADATA --collection AMAZONMETADATA --type json --file /mongo-seed/processed_meta_kindle_exported.json --jsonArray

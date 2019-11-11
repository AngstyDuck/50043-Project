#! /bin/bash
mongoimport --host 172.18.0.2 --port 43074 --db AMAZON --collection AMAZONMETADATA --type json --file /mongo-seed/processed_meta_kindle_exported.json

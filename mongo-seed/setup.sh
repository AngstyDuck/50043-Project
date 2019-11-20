#! /bin/bash
mongo --host mongoproj<<EOF
use admin;
db.auth('root', '123456');
use AMAZON;
db.createUser({user:'root',pwd:'123456',roles:[{role:'readWrite',db:'test'}]});
db.createCollection("AMAZONMETADATA");
EOF
mongoimport --host mongoproj --db AMAZON --collection AMAZONMETADATA --type json --file /mongo-seed/processed_meta_kindle_exported.json

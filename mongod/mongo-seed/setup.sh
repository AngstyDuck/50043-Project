#! /bin/bash
mongoimport --host mongod --db AMAZON --collection AMAZONMETADATA --type json --file ./docker-entrypoint-initdb.d/processed_meta_kindle_exported.json




# db.createUser({ user: "admin", pwd: "123456", roles: ["userAdminAnyDatabase"] }
# mongo --host mongoproj<<EOF
# use admin;
# db.auth('root', '123456');
#
# db.createUser({user:'root',pwd:'123456',roles:[{role:'readWrite',db:'AMAZON'}]});
#
# use AMAZON;
# db.createCollection("AMAZONMETADATA");
# EOF
# mongoimport --host mongoproj --db AMAZON --collection AMAZONMETADATA --type json --file /mongo-seed/processed_meta_kindle_exported.json

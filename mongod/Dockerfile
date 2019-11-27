FROM docker.io/mongo:3.2


ADD ./mongo-seed/init-mongo.js /tmp/
ADD ./mongo-seed/processed_meta_kindle_exported.json /docker-entrypoint-initdb.d

RUN mongo AMAZON /tmp/init-mongo.js
RUN mongoimport --host mongod --db AMAZON --collection AMAZONMETADATA --type json --file ./docker-entrypoint-initdb.d/processed_meta_kindle_exported.json

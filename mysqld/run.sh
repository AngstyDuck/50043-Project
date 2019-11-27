#!/bin/bash
mysql -uuser -ppassword --max_allowed_packet=1073741824 AMAZON < ./docker-entrypoint.initdb.d/amazon.sql

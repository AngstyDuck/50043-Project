#!/bin/bash

:`
# Installing normal admins
apt update
apt install -y vim git
`

# Cloning prof's repo and pulling data
# git clone https://github.com/dinhtta/istd50043_project.git ~/Desktop/500043-Prof
# chmod 777 ~/Desktop/500043-Prof/scripts/get_data.sh
# ~/Desktop/500043-Prof/scripts/get_data.sh

# Installing MySQL
# apt install -y mysql-server
# mysql_secure_installation --host=::1 --port=3307 --password=1234

# Installing MongoDB
apt install -y mongodb

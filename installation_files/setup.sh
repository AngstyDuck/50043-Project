#!/bin/bash


# Installing normal admins
apt update
apt install -y vim


# Cloning prof's repo and pulling data
git clone https://github.com/dinhtta/istd50043_project.git ~/Desktop/500043-Prof
chmod 777 ~/Desktop/500043-Prof/scripts/get_data.sh
~/Desktop/500043-Prof/scripts/get_data.sh

# Installing MySQL
apt install -y mysql-server
mysql_secure_installation --host=::1 --port=3307 --password=1234

# Installing MongoDB
wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | sudo apt-key add -
echo "deb [ arch=amd64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.2.list
apt-get update
apt-get install -y mongodb-org


#!/bin/bash


##### FOR MYSQL AND MONGO SETUP AND TEAR DOWN

# Installing misc packages
apt update


# installing git-lfs
curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
apt-get install -y git-lfs
git-lfs install


# Installing MySQL
apt install -y mysql-server
mysql_secure_installation


# Installing MongoDB
wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | sudo apt-key add -
echo "deb [ arch=amd64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.2.list
apt-get install -y mongodb-org
service mongod start


# to install mongodb compass
dpkg -i installation_files/mongodb-compass_1.19.12_amd64.deb
apt-get install -f -y


# mysql client (for testing)
apt install -y mysql-client-core-5.7


# Cloning metadata (with the correct format) from LFS repo
git clone https://github.com/SolsticeDante/50043-Project-lfs.git ~/Desktop/50043-Project-lfs


##### FOR MISC PACKAGES
apt-get install -y python3-venv curl


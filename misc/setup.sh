#!/bin/bash


# Installing misc packages
# apt update
# apt install -y vim curl


# installing git-lfs
# curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
# apt-get install -y git-lfs
# git lfs install


# Cloning metadata (with the correct format) from LFS repo
# git clone https://github.com/SolsticeDante/50043-Project-lfs.git ~/Desktop/50043-Project-lfs


# Cloning profs repo and pulling data
# git clone https://github.com/dinhtta/istd50043_project.git ~/Desktop/50043-Prof
# chmod 777 ~/Desktop/50043-Prof/scripts/get_data.sh
# ~/Desktop/50043-Prof/scripts/get_data.sh
# rm -rf meta_Kindle_Store.json


# Installing MySQL
# apt install -y mysql-server


# Installing MongoDB
# wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | sudo apt-key add -
# echo "deb [ arch=amd64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.2.list
# apt-get install -y mongodb-org
# service mongod start


# Install python mondules
# apt-get install -y python3 python3-pip
# apt-get install -y python3-venv
# python3 -m venv backend/venv
# source backend/venv/bin/activate
# pip3 install -r backend/requirements.txt


# to install mongodb compass
# dpkg -i installation_files/mongodb-compass_1.19.12_amd64.deb
# apt-get install -f -y


# Insert kindle metadata into mongodb
# echo "Inserting kindle metadata into mongodb..."
# python3 ./installation_files/metadataFill.py

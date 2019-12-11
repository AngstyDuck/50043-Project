#!/bin/bash
sudo apt-get update
sudo apt-get install gnupg
sudo apt-get install wget
sudo apt-get install curl
# installing git-lfs
curl -s https://packagecloud.io/install/repositories/github/git-lfs/script.deb.sh | sudo bash
sudo apt-get install -y git-lfs
sudo git-lfs install


echo '>>>>>>>>>>>>>>> Cloning Repository'
git clone https://github.com/SolsticeDante/50043-Project.git
cd 50043-Project/
git checkout deploy
cd ..
echo '>>>>>>>>>>>>>>> Finished Cloning Repository'

echo '>>>>>>>>>>>>>>> Getting metadata.json'
#
git clone https://github.com/SolsticeDante/50043-Project-lfs.git
cd 50043-Project-lfs/
cd ..
sudo wget https://databaseprojectic.s3-ap-southeast-1.amazonaws.com/processed_meta_kindle_exportedNew.json -O metadata.json
echo '>>>>>>>>>>>>>>> Successfully get metadata.json'

sudo apt install mongodb-org

wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | sudo apt-key add -

echo "deb [ arch=amd64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.2.list

sudo apt-get update

sudo apt-get install -y mongodb-org

echo "mongodb-org hold" | sudo dpkg --set-selections
echo "mongodb-org-server hold" | sudo dpkg --set-selections
echo "mongodb-org-shell hold" | sudo dpkg --set-selections
echo "mongodb-org-mongos hold" | sudo dpkg --set-selections
echo "mongodb-org-tools hold" | sudo dpkg --set-selections


sudo service mongod start

echo '>>>>>>>>>>>>>>> Importing Metadata'

mongoimport --db metadata --collection metadata --file metadata.json

echo '>>>>>>>>>>>>>>> Metadata Imported'

echo '>>>>>>>>>>>>>>> Changing Config'
cd /etc/

sudo sed -i -e 's/127.0.0.1/0.0.0.0/g' mongod.conf

echo '>>>>>>>>>>>>>>> Config Changed'

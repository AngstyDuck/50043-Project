#!/bin/bash


echo ' -> Cloning the github repository from SolsticeDante' 

sudo apt update
git clone https://github.com/SolsticeDante/50043-Project.git
cd 50043-Project/
git checkout deploy

echo ' -> Starting MYSQL Installation' 

mysqlRootPass="$(password)"

echo ' -> Removing previous mysql server installation'
systemctl stop mysqld.service && yum remove -y mysql-community-server && rm -rf /var/lib/mysql && rm -rf /var/log/mysqld.log && rm -rf /etc/my.cnf

echo ' -> Installing mysql server (community edition)'
yum localinstall -y https://dev.mysql.com/get/mysql57-community-release-el7-7.noarch.rpm
yum install -y mysql-community-server

echo ' -> Starting mysql server (first run)'
systemctl enable mysqld.service
systemctl start mysqld.service
tempRootDBPass="`grep 'temporary.*root@localhost' /var/log/mysqld.log | tail -n 1 | sed 's/.*root@localhost: //'`"

echo ' -> Setting up new mysql server root password'
systemctl stop mysqld.service
rm -rf /var/lib/mysql/*logfile*
wget -O /etc/my.cnf "https://my-site.com/downloads/mysql/512MB.cnf"
systemctl start mysqld.service
mysqladmin -u root --password="$tempRootDBPass" password "$mysqlRootPass"
mysql -u root --password="$mysqlRootPass" -e <<-EOSQL
    DELETE FROM mysql.user WHERE User='';
    DROP DATABASE IF EXISTS test; 
    DELETE FROM mysql.db WHERE Db='test' OR Db='test\\_%'; 
    DELETE FROM mysql.user where user != 'mysql.sys'; 
    CREATE USER 'root'@'%' IDENTIFIED BY '${mysqlRootPass}';
    GRANT ALL ON *.* TO 'root'@'%' WITH GRANT OPTION;
    FLUSH PRIVILEGES;
EOSQL
systemctl status mysqld.service
echo " -> MySQL server installation completed, root password: $mysqlRootPass";



echo ' -> Starting MongoDb Installation' 

sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 9DA31620334BD75D9DCB49F368818C72E52529D4
echo "deb [ arch=amd64 ] https://repo.mongodb.org/apt/ubuntu bionic/mongodb-org/4.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.0.list
sudo apt-get update -y
sudo apt-get install mongodb-org -y
sudo mkdir -p /data/db
sudo chown -R $USER /data/db 
sudo chmod -R go+w /data/db
echo " -> MongoDB installed"










#!/bin/bash
sudo apt-get update
sudo apt-get install -y expect
sudo apt install sed
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

echo '>>>>>>>>>>>>>>> Starting MYSQL installation'
sudo apt-get install wget
sudo apt install mysql-server -y


echo '>>>>>>>>>>>>>>> Getting amazon.sql'
#
git clone https://github.com/SolsticeDante/50043-Project-lfs.git
cd 50043-Project-lfs/
cd ..
# sudo wget https://github.com/SolsticeDante/50043-Project-lfs/blob/master/amazon.sql -O amazon.sql
sudo wget https://databaseprojectic.s3-ap-southeast-1.amazonaws.com/amazon_new.sql -O amazon.sql
echo '>>>>>>>>>>>>>>> Successfully get amazon.sql'

MYSQL_ROOT_PASSWORD='password'
MYSQL=$(grep 'temporary password' /var/log/mysqld.log | awk '{print $11}')

SECURE_MYSQL=$(expect -c "

set timeout 10
spawn mysql_secure_installation

expect \"Enter password for user root:\"
send \"$MYSQL\r\"
expect \"New password:\"
send \"$MYSQL_ROOT_PASSWORD\r\"
expect \"Re-enter new password:\"
send \"$MYSQL_ROOT_PASSWORD\r\"
expect \"Change the password for root ?\ ((Press y\|Y for Yes, any other key for No) :\"
send \"y\r\"
send \"$MYSQL\r\"
expect \"New password:\"
send \"$MYSQL_ROOT_PASSWORD\r\"
expect \"Re-enter new password:\"
send \"$MYSQL_ROOT_PASSWORD\r\"
expect \"Do you wish to continue with the password provided?\(Press y\|Y for Yes, any other key for No) :\"
send \"y\r\"
expect \"Remove anonymous users?\(Press y\|Y for Yes, any other key for No) :\"
send \"y\r\"
expect \"Disallow root login remotely?\(Press y\|Y for Yes, any other key for No) :\"
send \"n\r\"
expect \"Remove test database and access to it?\(Press y\|Y for Yes, any other key for No) :\"
send \"y\r\"
expect \"Reload privilege tables now?\(Press y\|Y for Yes, any other key for No) :\"
send \"y\r\"
expect eof
")

echo $SECURE_MYSQL

echo '>>>>>>>>>>>>>>> Finished Installing mysql'

sudo mysql <<EOF
SELECT user,authentication_string,plugin,host FROM mysql.user;
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';
FLUSH PRIVILEGES;
SELECT user,authentication_string,plugin,host FROM mysql.user;
exit
EOF

mysql -u root -ppassword <<EOF
CREATE DATABASE IF NOT EXISTS amazon;
USE amazon;
EOF


mysql -u root -ppassword amazon < ./amazon.sql

echo '>>>>>>>>>>>>>>> Successfully imported AMAZON'
echo '>>>>>>>>>>>>>>> Configuring Credentials'
cd /etc/mysql/mysql.conf.d/
# sudo replace "bind-address " "#bind-address " -- mysqld.cnf

sudo sed -i -e 's/bind/#bind/g' mysqld.cnf

echo '>>>>>>>>>>>>>>> Changed config'

echo '>>>>>>>>>>>>>>> Flushing Privilleges'

mysql -u root -ppassword<<EOF
GRANT ALL PRIVILEGES ON *.* TO 'root'@'%' IDENTIFIED BY 'password';
EOF

echo '>>>>>>>>>>>>>>> Finished Flushing Privilleges'

echo '>>>>>>>>>>>>>>> Restarting sql'

sudo service mysql restart

echo '>>>>>>>>>>>>>>> Restarted sql'

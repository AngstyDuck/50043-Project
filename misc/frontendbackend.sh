backend_ip=$1
mysql_ip=$2
mongo_ip=$3
sudo apt-get update
sudo apt-get install apt-transport-https ca-certificates curl gnupg-agent software-properties-common -y
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"
sudo apt-get install docker-ce docker-ce-cli containerd.io -y
sudo curl -L "https://github.com/docker/compose/releases/download/1.25.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose
sudo apt-get install docker.io -y
git clone https://github.com/SolsticeDante/50043-Project.git
cd 50043-Project/
git checkout develop
sed -i "s/BACKEND_IP_ADDR/$backend_ip/" frontend/ebook/src/store/store.js
sed -i "s/MYSQL_IP/$mysql_ip/" backend/config.py
sed -i "s/MONGO_IP/$mongo_ip/" backend/config.py
# Add more sed for chaning of ip for backend
sudo docker-compose build
screen -dm bash -c "sudo docker-compose up"
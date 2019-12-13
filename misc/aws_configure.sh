#!/bin/bash


SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"
echo $SCRIPTPATH

# PATH="/usr/local/bin:$PATH"

apt update
apt install -y jq
apt-get update
apt-get install -y python3-pip

: '
# format of credentials.json
{
	"access_key_id": "123",
	"secret_access_key": "456"
}
'


aws configure <<EOF
$(cat "${SCRIPTPATH}/credentials.json" | jq -r ".access_key_id")
$(cat "${SCRIPTPATH}/credentials.json" | jq -r ".secret_access_key")
"ap-southeast-1"
"json"
y
EOF


# /home/xubuntu/.config/flintrock/config.yaml
sudo -H pip3 install flintrock
sed "s/TO_REPLACEE/${HOME}\/flint_cluster.pem/g" "${SCRIPTPATH}/config.yaml" > "${hHOME}/.config/flintrock/"

export AWS_ACCESS_KEY_ID=$(cat "${SCRIPTPATH}/credentials.json" | jq -r ".access_key_id")
export AWS_SECRET_ACCESS_KEY=$(cat "${SCRIPTPATH}/credentials.json" | jq -r ".secret_access_key")
echo $AWS_ACCESS_KEY_ID

flintrock launch sample-cluster

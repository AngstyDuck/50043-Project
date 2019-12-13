#!/bin/bash


SCRIPTPATH="$( cd "$(dirname "$0")" ; pwd -P )"
echo $SCRIPTPATH
PATH="/usr/local/bin:$PATH"
# apt update
apt install -y jq

aws configure <<EOF
$(cat "${SCRIPTPATH}/aws_config.json" | jq -r ".access_key_id")
$(cat "${SCRIPTPATH}/aws_config.json" | jq -r ".secret_access_key")
"ap-southeast-1"
"json"
y
EOF

# /home/xubuntu/.config/flintrock/config.yaml
sudo -H pip3 install flintrock
cp "${SCRIPTPATH}/config.yaml" "${HOME}/.config/flintrock/config.yaml"

export AWS_ACCESS_KEY_ID=$(cat "${SCRIPTPATH}/aws_config.json" | jq -r ".access_key_id")
export AWS_SECRET_ACCESS_KEY=$(cat "${SCRIPTPATH}/aws_config.json" | jq -r ".secret_access_key")
echo $AWS_ACCESS_KEY_ID

flintrock launch sample-cluster

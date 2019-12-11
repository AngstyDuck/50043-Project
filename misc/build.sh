echo 'Creating 3 VMs'
instances_json=`aws ec2 run-instances --image-id ami-061eb2b23f9f8839c --count 3 --instance-type t2.medium --key-name key1 --security-group-ids sg-e7cb1999`
instance_id_frontendbackend=`echo $instances_json | python3 -c "import sys, json; print(json.load(sys.stdin)['Instances'][0]['InstanceId'])"`
instance_id_mysql=`echo $instances_json | python3 -c "import sys, json; print(json.load(sys.stdin)['Instances'][1]['InstanceId'])"`
instance_id_mongodb=`echo $instances_json | python3 -c "import sys, json; print(json.load(sys.stdin)['Instances'][2]['InstanceId'])"`
echo 'Waiting for VMs to spin up, waiting for 35s'
sleep '35' 
echo 'Querying IP address'
public_ip_frontendbackend=`aws ec2 describe-instances --instance-id $instance_id_frontendbackend | python3 -c "import sys, json; print(json.load(sys.stdin)['Reservations'][0]['Instances'][0]['PublicIpAddress'])"`
public_ip_mysql=`aws ec2 describe-instances --instance-id $instance_id_mysql | python3 -c "import sys, json; print(json.load(sys.stdin)['Reservations'][0]['Instances'][0]['PublicIpAddress'])"`
public_ip_mongodb=`aws ec2 describe-instances --instance-id $instance_id_mongodb | python3 -c "import sys, json; print(json.load(sys.stdin)['Reservations'][0]['Instances'][0]['PublicIpAddress'])"`
public_dns_frontendbackend=`aws ec2 describe-instances --instance-id $instance_id_frontendbackend | python3 -c "import sys, json; print(json.load(sys.stdin)['Reservations'][0]['Instances'][0]['PublicDnsName'])"`
public_dns_mysql=`aws ec2 describe-instances --instance-id $instance_id_mysql | python3 -c "import sys, json; print(json.load(sys.stdin)['Reservations'][0]['Instances'][0]['PublicDnsName'])"`
public_dns_mongodb=`aws ec2 describe-instances --instance-id $instance_id_mongodb | python3 -c "import sys, json; print(json.load(sys.stdin)['Reservations'][0]['Instances'][0]['PublicDnsName'])"`
echo "frontend ip: $public_ip_frontendbackend"
chmod 400 key1.pem
echo 'SSH into mysql'
ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -i "key1.pem" ubuntu@$public_dns_mysql 'bash -s' < mysql_install.sh
echo 'SSH into mongodb'
ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -i "key1.pem" ubuntu@$public_dns_mongodb 'bash -s' < mongodb_setup.sh
echo 'SSH into frontend/backend'
ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -i "key1.pem" ubuntu@$public_dns_frontendbackend 'bash -s' < frontendbackend.sh $public_ip_frontendbackend $public_ip_mysql $public_ip_mongodb
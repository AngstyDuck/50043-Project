instance_id=`aws ec2 run-instances --image-id ami-061eb2b23f9f8839c --count 1 --instance-type t2.micro --key-name key1 --security-group-ids sg-e7cb1999 | python3 -c "import sys, json; print(json.load(sys.stdin)['Instances'][0]['InstanceId'])"`
echo 'Waiting for VM to spin up'
sleep '40' 
aws ec2 associate-address --allocation-id eipalloc-0051798c2bac2680b --instance-id $instance_id
public_dns_name=`aws ec2 describe-instances --instance-id $instance_id | python3 -c "import sys, json; print(json.load(sys.stdin)['Reservations'][0]['Instances'][0]['PublicDnsName'])"`
chmod 400 key1.pem
ssh -o UserKnownHostsFile=/dev/null -o StrictHostKeyChecking=no -i "key1.pem" ubuntu@$public_dns_name 'bash -s' < frontendbackend.sh -yes
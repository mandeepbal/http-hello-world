import boto3

client = boto3.resource('ec2')

secgrp = client.create_security_group(
  GroupName='nginx-sg',
  Description='Security Group for NGINX Server. Open only 80 to the world.'
)

nginx = ec2.create_instances(
  ImageId='ami-0d4cfd66',
  MinCount='1',
  MaxCount='1',
  InstanceType='t2.micro',
  SecurityGroups=[secgrp.name]
)



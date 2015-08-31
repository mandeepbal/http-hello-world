import boto3
import time
import httplib
import base64

client = boto3.resource('ec2')

#vpc = ec2.create_vpc(CidrBlock='10.0.0.0/24')
#subnet = vpc.create_subnet(CidrBlock='10.0.0.0/25')
#gateway = ec2.create_internet_gateway()
#gateway.attach_to_vpc(VpcId=vpc.id)

secgrp = client.create_security_group(
  GroupName='nginx-sg'+time.strftime("%Y%m%d%H%M%S"),
  Description='Security Group for NGINX Server.'
)
secgrp.authorize_ingress(
    IpProtocol='tcp',
    FromPort=80,
    ToPort=80,
    CidrIp='0.0.0.0/0'
)
print("SecurityGroup Name:"+secgrp.group_name+" id:"+secgrp.group_id)

startupscript = open('user-data.sh', 'r').read()
encoded_userdata = base64.b64encode(startupscript)

nginx = client.create_instances(
  ImageId='ami-0d4cfd66',
  MinCount=1,
  MaxCount=1,
  InstanceType='t2.micro',
  SecurityGroups=[secgrp.group_name],
  UserData=encoded_userdata
)
print("waiting for instance to start...instance_id:"+nginx[0].id)
nginx[0].wait_until_running()
nginx = client.Instance(nginx[0].id)

conn = httplib.HTTPConnection(nginx.public_ip_address)
conn.request("GET", "/")
h1 = conn.getresponse()
print h1.read()

print("URL of webpage: http://"+nginx.public_ip_address)

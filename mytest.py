import boto3
import time
import httplib
import base64

# Create ec2 resource
client = boto3.resource('ec2')

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
print("waiting for nginx to install, configure, and start ...instance_id:")
time.sleep(60)
print("URL of webpage: http://"+nginx.public_ip_address)

conn = httplib.HTTPConnection(nginx.public_ip_address)
conn.request("GET", "/")
httpresponse = conn.getresponse()
httpresponse = httpresponse.read()

if 'Automation for the People' in httpresponse :
    print("Page Succesfully Created!!")
else:
    print("Failed to create webpage!!")
    nginx.terminate()

# Serve a Static Page
## Requirements to Execute `startup.py`
  * Linux/Mac machine with the following software installed:
    * [Python](https://www.python.org/downloads/)
    * [pip](https://pip.pypa.io/en/latest/installing.html#install-pip)
    * [Boto3 (AWS Python SDK)](https://aws.amazon.com/sdk-for-python/)
  * AWS Account
    * Create IAM user with ec2 Full Access and create API keys
    * Make sure you have a default VPC set for the AWS Account
      * Also make sure your default subnet will Auto-assign Public IP
    * Create the 2 files below on your machine and modify the credentials file to reflect YOUR_ACCESS_KEY and YOUR_SECRET_KEY

###### `~/.aws/credentials` file
```
[default]
aws_access_key_id = YOUR_ACCESS_KEY
aws_secret_access_key = YOUR_SECRET_KEY
```

###### `~/.aws/config` file
```
[default]
region=us-east-1
```

## Execution instructions
```
git clone https://github.com/mandeepbal/http-hello-world.git
cd http-hello-world
python startup.py
```

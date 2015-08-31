# Serve a Static Page
## Requirements to Execute `startup.py`
  * Linux/Mac machine with the following software installed:
    * [Python](https://www.python.org/downloads/)
    * [pip](https://pip.pypa.io/en/latest/installing.html#install-pip)
    * [Boto3 (AWS Python SDK)](https://aws.amazon.com/sdk-for-python/)
  * AWS Account with API credentials
    * Create `~/.aws/credentials` file below with your credenitals
```
[default]
aws_access_key_id = YOUR_ACCESS_KEY
aws_secret_access_key = YOUR_SECRET_KEY
```
    * Create `~/.aws/config` file below with your credenitals
```
[default]
region=us-east-1
```
## Execution instructions
```
git clone https://github.com/mandeepbal/http-hello-world.git
cd http-hello-world
python mytest.py
```

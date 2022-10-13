import json
import boto3
AWS_REGION = "us-west-1"

ec2 = boto3.client('ec2', region_name=AWS_REGION)
response = ec2.describe_vpcs()
for val in response['Vpcs']:
    print(val['VpcId'])


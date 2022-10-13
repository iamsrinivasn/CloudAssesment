import json
import boto3

# Set AWS Region
AWS_REGION = "us-west-1"
ec2 = boto3.client('ec2', region_name=AWS_REGION)

# List all VPCs in the selected Region
print("")
print("1. List all VPCs in the selected Region")
desc_vpcs = ec2.describe_vpcs()
for vpc in desc_vpcs['Vpcs']:
    print(vpc['VpcId']+" "+vpc['CidrBlock'])

# List all Subnet in the selected Region
print("")
print("2. List all Subnet in the selected Region")
desc_subs = ec2.describe_subnets()
for subnet in desc_subs['Subnets']:
    print(subnet['VpcId']+" "+subnet['SubnetId']+" "+subnet['CidrBlock']+" "+subnet['AvailabilityZone'])

# List all Internet Gateways in the selected Region
print("")
print("2. List all IGW in the selected Region")
desc_igws = ec2.describe_internet_gateways()
for igw in desc_igws['InternetGateways']:
    print(igw['Attachments'][0]['VpcId']+" "+igw['InternetGatewayId'])




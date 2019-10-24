#Listing SG which are open to world on any port
import boto3
def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name='us-east-1')
    regions = ec2.describe_regions()
    for reg in regions['Regions']:
        print('Connecting to region {}'.format(reg['RegionName']))
        sg_client = boto3.client('ec2', region_name = reg['RegionName'])
        sgs = sg_client.describe_security_groups()
        for sg in sgs['SecurityGroups']:
            for ip_rule in sg['IpPermissions']:
                try:
                    for iprange in ip_rule['IpRanges']:
                        if iprange['CidrIp'] == '0.0.0.0/0':
                            print(reg['RegionName'],'|',sg['GroupName'],'|',ip_rule)
                except Exception as error:
                    print(error)






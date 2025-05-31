import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name='ap-southeast-5')

    filters = [
        {'Name': 'tag:Servidor', 'Values': ['ChipinventorDevel']},
        {'Name': 'instance-state-name', 'Values': ['stopped']}
    ]

    response = ec2.describe_instances(Filters=filters)

    to_start = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            to_start.append(instance['InstanceId'])

    if to_start:
        ec2.start_instances(InstanceIds=to_start)
        print("Instâncias iniciadas:", to_start)
    else:
        print("Nenhuma instância para iniciar.")

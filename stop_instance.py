import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2', region_name='selecione a região')

    filters = [
        {'Name': 'tag:crie sua tag', 'Values': ['dê um valor à sua tag']},
        {'Name': 'instance-state-name', 'Values': ['running']}
    ]

    response = ec2.describe_instances(Filters=filters)

    to_stop = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            to_stop.append(instance['InstanceId'])

    if to_stop:
        ec2.stop_instances(InstanceIds=to_stop)
        print("Instâncias paradas:", to_stop)
    else:
        print("Nenhuma instância para parar.")

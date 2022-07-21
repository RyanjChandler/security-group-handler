import boto3

def lambda_handler(event, context):
    #handling json from the event and grabbing security group.
    client = boto3.client('ec2')
    print(event)
    eventid = event['detail']['instance-id']
    describe = client.describe_instances(
        Filters=[
            {
                'Name': 'instance-id',
                'Values': [
                    eventid,
                ],
            },
        ],
    )
    try:
        securitygroup = describe['Reservations'][0]['Instances'][0]['SecurityGroups'][0]['GroupId']
        print (securitygroup)

    except:
        print ("failed to get security group")
        exit(1)
    #grabbing parameter of approved security group.
    client = boto3.client('ssm')
    response = client.get_parameter(
    Name='box-1'
    )
    print (response)
    sgfinal = response['Parameter']['Value']
    print(sgfinal)
    snscheck = boto3.client('sns')
    if sgfinal == securitygroup:
        print ("ec2 is using approved security group")
        exit(0)
    elif sgfinal != securitygroup:
        snsmessage = 'The EC2 ' + eventid + ' is using an unsecured security group, please audit!'
        snsresponse = snscheck.publish(
        TopicArn='arn:aws:sns:us-west-2:964928031140:security-team',
        Message=snsmessage,
        Subject='unsecured ec2!'
        )
        print (snsresponse)
import boto3
import time
client = boto3.client('ssm')
response = client.send_command(
	InstanceIds=['i-0bf8758b4a8d55a52'],
	DocumentName='AWS-RunShellScript',
	Parameters={
		'commands':['TOKEN=`curl -X PUT "http://169.254.169.254/latest/api/token" -H "X-aws-ec2-metadata-token-ttl-seconds: 21600"` \
&& curl -H "X-aws-ec2-metadata-token: $TOKEN" -v http://169.254.169.254/latest/meta-data/ami-id']
	}
)
command_id = response['Command']['CommandId']
print(command_id)
#command_id = context.aws_request_id
time.sleep(10)
output = client.get_command_invocation(
      CommandId=command_id,
      InstanceId="i-0bf8758b4a8d55a52"
    )
print(output)

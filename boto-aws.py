import boto3
# run 'aws configure' first to set your AWS credentials and region

print("Stato ambiente dev: ")
client = boto3.client('ec2')
conn = boto3.resource('ec2')
instances = conn.instances.filter()
for instance in instances:
    if instance.state["Name"] == "running":
        print (instance.id, instance.state, instance.instance_type)
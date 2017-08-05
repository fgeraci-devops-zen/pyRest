import boto3

access_key = "AKIAJZD2NFAY3PYHIQ3A"
secret_key = "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"

print("Stato ambiente dev: ")
client = boto3.client('ec2')
conn = boto3.resource('ec2')
instances = conn.instances.filter()
for instance in instances:
    if instance.state["Name"] == "running":
        print (instance.id, instance.state, instance.instance_type)
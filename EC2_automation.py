import boto3 as bt
import time
session = bt.session.Session(region_name="ap-south-1")
print(session.region_name)
ec2 = session.resource("ec2")

"""def create_key_pair():
    key_pair = ec2.create_key_pair(KeyName="DemoKeyPair2")"""

count=0
instances = ec2.instances.filter()
for i in instances:
    if i.state["Name"]== 'running':
        print(i.id,i.instance_type)
        count+=1
print("no. of instances running: {}".format(count))

if count>0:
    print("{} EC2 instance/s are already running:skipping now".format(count))
    pass
else:
    #create_key_pair()
    instance = ec2.create_instances(ImageId="ami-079b5e5b3971bd10d",
                                 MinCount=1,
                                 MaxCount=1,
                                 InstanceType="t2.micro",
                                 KeyName="DemoKeyPair")
    time.sleep(10)
#   print(instance)
    print(f"instance id of recently created instance: {instance[0].id}")

for i in instances:
    if i.state["Name"]=="running":
        time.sleep(10)
        i.terminate()
        time.sleep(10)
        print(f"instance with id: {i.id} is terminated now")




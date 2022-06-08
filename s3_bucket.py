import boto3 as bt
import time

session = bt.session.Session(region_name="us-east-1")
print(session.region_name)
s3_client = session.client("s3")
#bucket = s3_client.create_bucket(Bucket="meghalitest")
response = s3_client.list_buckets()
print(response)
for bucket in response["Buckets"]:
    print(bucket)

objects = s3_client.list_objects_v2(Bucket='meghalitest')
print(objects["KeyCount"])

response1 = s3_client.delete_bucket(Bucket='meghalitest')
time.sleep(10)
print("the bucket has been deleted successfully")

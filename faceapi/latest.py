import boto3
from botocore.vendored import requests

    
bucket = "palisade8033"
runtime_client = boto3.client('runtime.sagemaker')
    
get_last_modified = lambda obj: int(obj['LastModified'].strftime('%s'))
s3 = boto3.client('s3')
objs = s3.list_objects_v2(Bucket=bucket)['Contents']
latest_obj = [obj['Key'] for obj in sorted(objs, key=get_last_modified, reverse=True)][0]
print(latest_obj)





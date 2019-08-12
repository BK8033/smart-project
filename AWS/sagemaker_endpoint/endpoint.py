import json
import boto3


bucket = "sagemaker-us-west-2-334381301451"
endpoint_name = "deployed-image-classificationml-t2"
runtime_client = boto3.client('runtime.sagemaker')


def lambda_handler(event, context):
# TODO implement
    get_last_modified = lambda obj: int(obj['LastModified'].strftime('%s'))
    s3 = boto3.client('s3')
    objs = s3.list_objects_v2(Bucket=bucket)['Contents']
    latest_obj = [obj['Key'] for obj in sorted(objs, key=get_last_modified, reverse=True)][0]
#print(latest)


    s3 = boto3.resource('s3')
my_bucket = s3.Bucket(bucket)
    test_key = latest_obj
    s3.Bucket(bucket).download_file(test_key, '/tmp/test_data.jpg')

    with open('/tmp/test_data.jpg', 'rb') as f:
    payload = f.read()
payload = bytearray(payload)
    response = runtime_client.invoke_endpoint(EndpointName = endpoint_name,
            ContentType = 'application/x-image',
            Body = payload)

    result = response['Body'].read().decode('ascii')
    print('Predicted label is {}.'.format(result))

    if float(result[0]) - float(result[1]) >0:
    print("aaa")
    return True
    else:
    return False

    return True

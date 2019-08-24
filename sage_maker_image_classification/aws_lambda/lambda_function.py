import boto3
from botocore.vendored import requests

    
#bucket = "upload8033"
#endpoint_name = "deployed-image-classificationml-t2"
#runtime_client = boto3.client('runtime.sagemaker')


def lambda_handler(event, context):
    # TODO implement
    
    request.get("http://18.266.66.232:5365/upload")
        
    """get_last_modified = lambda obj: int(obj['LastModified'].strftime('%s'))
    s3 = boto3.client('s3')
    objs = s3.list_objects_v2(Bucket=bucket)['Contents']
    latest_obj = [obj['Key'] for obj in sorted(objs, key=get_last_modified, reverse=True)][0]
    print(latest_obj)
    
    
    s3 = boto3.resource('s3')
    my_bucket = s3.Bucket(bucket)
    
    s3.Bucket(bucket).download_file(latest_obj, '/tmp/test_data.jpg')
    
    with open('/tmp/test_data.jpg', 'rb') as f:
        payload = f.read()
        payload = bytearray(payload)
        response = runtime_client.invoke_endpoint(EndpointName = endpoint_name,
                                         ContentType = 'application/x-image',
                                         Body = payload)
                                         
        result = response['Body'].read().decode('ascii')
        print('Predicted label is {}.'.format(result))
        result=result.split(',')
        print(result)
        result[0]=result[0].replace("[","")
        result[0]=result[0].replace(" ","")
        result[1]=result[1].replace("]","")
        result[1]=result[1].replace(" ","")
        
        print(float(result[0]))
        print(float(result[1]))
        
       
        
        if float(result[0]) - float(result[1]) >0:
            requests.get("http://52.43.95.248:5365/condi")
            return False
        else:
            
            return True"""
        
    return True

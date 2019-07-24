import boto3

s3 = boto3.client('s3')
filename = 'a.txt'
bucket_name = 'palisade5365'

s3.upload_file(filename,bucket_name,filename)

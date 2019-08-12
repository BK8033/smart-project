import boto3

    
bucket = "palisade5365"
    
get_last_modified = lambda obj: int(obj['LastModified'].strftime('%s'))
s3 = boto3.client('s3')
objs = s3.list_objects_v2(Bucket=bucket)['Contents']
for i in range(1,256):
#    o = '{:0:03d}'.format(i)
#    o = f'{n:03}'
    o=str(i).zfill(3)
    print(o)





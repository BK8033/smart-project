import boto3
import face
import json
import csv
import array as arr
wr = csv.writer(open('data_sleep.csv','w'))

bucket = "palisade5365"
#open(file_name,'w') as cs
s3 = boto3.client('s3')
objs = s3.list_objects_v2(Bucket=bucket)['Contents']
#########################
'''
for obj in objs:
    file_name = obj['Key']
    print(file_name[4:7])
'''   
#########################
fi = 'data.csv'
col=['index','eyeLeftOuter','eyeLeftInner','eyeLeftTop','eyeLeftBottom',
    'eyeRightOuter','eyeRightInner','eyeRightTop','eyeRightBottom',
    'upperLipTop','upperLipBottom','underLipTop','underLipBottom','mouthLeft','mouthRight',
    'eyebrowLeftInner','eyebrowLeftOuter','eyebrowRightInner','eyebrowRightOuter',
    'pitch','roll','yaw']
emo_col = ['neutral','anger','happiness','disgust','sadness']
for i in range(1,169):
    file_name = 'sleep/'+ str(i).zfill(3) + '.jpg'
    #print(file_name)
    res = face.getFace(file_name)
    #print(res.json())
    print('----------',str(i).zfill(3),'------------')
    if not res.json():
        data = [str(i).zfill(3)]
        data = data + [0]*44
        print('Cannot Found Face')
    else:
        land = res.json()[0]['faceLandmarks']
        exp = res.json()[0]['faceAttributes']['exposure']
        att = res.json()[0]['faceAttributes']['headPose']
        emo = res.json()[0]['faceAttributes']['emotion']
        data = [str(i).zfill(3)]
#        print('level: ', exp['exposureLevel'], ', value: ', exp['value'])
   #     print('type: ', type(exp['value']))
        for i in range(1,19):
            data = data + [land[col[i]]['x']]
            data = data + [land[col[i]]['y']]

        for i in range(19,22):
            data = data + [att[col[i]]]
        
        data = data + [emo['neutral'], emo['anger'],emo['happiness'],emo['disgust'],emo['sadness']]
        data = data + [exp['value']]

    wr.writerow(data)
    

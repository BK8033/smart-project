import boto3
import face
import json
import csv

wr = csv.writer(open('data.csv','w'))

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
emo_col = ['neutral','anger','happiness','disgust','sadness']
wr.writerow(col)   
for i in range(1,265):
#for obj in objs:
#    file_name = 'pic/00' + str(i) + '.jpg'
#    file_name = obj['Key']
#    print(file_name)
#    file_name = 'pic/030.jpg'
    file_name = 'pic/'+ str(i).zfill(3) + '.jpg'
#    print(file_name)
    res = face.getFace(file_name)
    land = res.json()[0]['faceLandmarks']
    att = res.json()[0]['faceAttributes']
    emo = att['emotion']
#    print(json.dumps(res.json()[0],indent=2))
#    print(col[9])i
#    print(json.dumps(res.json()[0]['faceLandmarks'],indent=2))
#    print(json.dumps(res.json()[0]['faceAttributes'],indent=2))
#    print(res.json()[0]['faceLandmarks'].keys())
    print('----------',file_name[4:7],'------------')
    dat = [file_name[4:7],land[col[1]]['x'],land[col[1]]['y'],land[col[2]]['x'],land[col[2]]['y'],land[col[3]]['x'],land[col[3]]['y'],land[col[4]]['x'],land[col[4]]['y'],
        land[col[5]]['x'],land[col[5]]['y'],land[col[6]]['x'],land[col[6]]['y'],land[col[7]]['x'],land[col[7]]['y'],land[col[8]]['x'],land[col[8]]['y'],
        emo[emo_col[0]],emo[emo_col[1]],emo[emo_col[2]],emo[emo_col[3]],emo[emo_col[4]]]
#    write1(fi,col,json.dumps(res.json()[0]['faceLandmarks']))
    wr.writerow(dat)

       

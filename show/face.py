import requests
import json
import boto3

bucket = "palisade5365"
get_last_modified = lambda obj: int(obj['LastModified'].strftime('%s'))
s3 = boto3.client('s3')

subscription_key = '88f31bd2bc4d4773bdf0de12142fbd3c'
assert subscription_key

face_api_url = 'https://koreacentral.api.cognitive.microsoft.com/face/v1.0/detect'



headers = {'Ocp-Apim-Subscription-Key': subscription_key}

params = {
    'returnFaceId': 'true',
    'returnFaceLandmarks': 'true',
    'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
}

def isSick():
    objs = s3.list_objects_v2(Bucket=bucket)['Contents']
    latest_obj = [obj['Key'] for obj in sorted(objs, key=get_last_modified, reverse=True)][0]
    image_url = 'https://palisade5365.s3.ap-northeast-2.amazonaws.com/' + latest_obj
    print('file = ',latest_obj)
    response = requests.post(face_api_url, params=params,
                             headers=headers, json={"url": image_url})
    condition=1
#    print(type(response.status_code))
#    print(response.json())
    if response.status_code == 400:
        print('error occured')
        return -1
    if response.json():
        land = response.json()[0]['faceLandmarks']
        emo = response.json()[0]['faceAttributes']['emotion']
        print(emo)
        ang = emo['anger']
        neutral = emo['neutral']
        happ = emo['happiness']
        disg = emo['disgust']
        elt = land['eyeLeftTop']
        elb = land['eyeLeftBottom']
        ert = land['eyeRightTop'] 
        erb = land['eyeRightBottom']
        lei = land['eyeLeftInner']['x']-land['eyeLeftOuter']['x']
        rei = land['eyeRightOuter']['x']-land['eyeRightInner']['x']
        left_width = float(land['eyeLeftInner']['x'])-float(land['eyeLeftOuter']['x'])
        right_width = float(land['eyeRightOuter']['x'])-float(land['eyeRightInner']['x'])
        width = (left_width + right_width)/2
        
        threshold = 6;
        
                
        left_dif = float(elb['y'])-float(elt['y'])
        right_dif = float(erb['y'])-float(ert['y'])
        dif = (left_dif + right_dif)/2

        print('width = ',width,', height = ',dif, ', threshold = ', (width/dif)*2)
        #############################

        ##############################
        if disg > 0.01 or ang >0.1:
            print('Prediction: Sick')
            return 3
        else:
            if (width/dif)*2 > threshold and dif < 16 :
                print('Prediction: sleep')
                return 4
            else:
                print('Prediction: Normal')
                return 2
        ################################
    else:
        print('Cannot found face')
        return -1

import requests
import json
import boto3

bucket = "palisade5365"
get_last_modified = lambda obj: int(obj['LastModified'].strftime('%s'))
s3 = boto3.client('s3')

subscription_key = 'b1afff0faa3840fa83f270ec0f532a08'
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
#    print(response.text)
    try:
        land = response.json()[0]['faceLandmarks']
        emo = response.json()[0]['faceAttributes']['emotion']
    #    print(emo)
        ang = emo['anger']
        neutral = emo['neutral']
        happ = emo['happiness']
        elt = land['eyeLeftTop']
        elb = land['eyeLeftBottom']
        ert = land['eyeRightTop'] 
        erb = land['eyeRightBottom']
        lei = land['eyeLeftInner']['x']-land['eyeLeftOuter']['x']
        rei = land['eyeRightOuter']['x']-land['eyeRightInner']['x']
        left_width = float(land['eyeLeftInner']['x'])-float(land['eyeLeftOuter']['x'])
        right_width = float(land['eyeRightOuter']['x'])-float(land['eyeRightInner']['x'])
        width = (left_width + right_width)/2
#        print('aaa')
        threshold = (rei+lei)/4;
                
#        print('left width: ', left_width, ', right_width: ', right_width)
        print('width = ', width, ',  thres = ',threshold)
        left_dif = float(elb['y'])-float(elt['y'])
        right_dif = float(elb['y'])-float(elt['y'])
        dif = (left_dif + right_dif)/2
        print('letf: ', left_dif, ',   r: ', right_dif, ',    thr: ', threshold)
        if happ > 0.5:
            print('Prediction: Normal')
            return 0
        elif neutral + happ < 0.7:
            print('Prediction: Sick')
            return 1
        elif dif < threshold:
            print('Prediction: Sleep')
            return 2
        else:
            print('Prediction: Normal')
            return 0
    except Exception:
        print('Cannot found face')

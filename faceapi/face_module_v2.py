import requests
import json

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
    idx = input('Enter Number(1:normal, 2:abnormal, 3:sleep) >> ')
    condi = ''

    if idx == '1':
       condi = 'normal'
    elif idx == '2':
        condi = 'sick'
    else:
        condi = 'sleep'

    image_url = 'https://palisade5365.s3.ap-northeast-2.amazonaws.com/ts/seok/' + condi + '/3.jpg'

    response = requests.post(face_api_url, params=params,
                             headers=headers, json={"url": image_url})
    land = response.json()[0]['faceLandmarks']
    emo = response.json()[0]['faceAttributes']['emotion']
    ang = emo['anger']
    neutral = emo['neutral']
#    print('neu: ', neutral
    for key in emo.keys():
        print(key, ':', emo[key])
#    print(emo.keys())
    elt = land['eyeLeftTop']
    elb = land['eyeLeftBottom']
    ert = land['eyeRightTop'] 
    erb = land['eyeRightBottom']
    left_dif = float(elb['y'])-float(elt['y'])
    right_dif = float(elb['y'])-float(elt['y'])


import requests
import json

subscription_key = 'b1afff0faa3840fa83f270ec0f532a08'
assert subscription_key

face_api_url = 'https://koreacentral.api.cognitive.microsoft.com/face/v1.0/detect'



headers = {'Ocp-Apim-Subscription-Key': subscription_key}

params = {
        'returnFaceId': 'true',
            'returnFaceLandmarks': 'false',
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
    
    emo = response.json()[0]['faceAttributes']['emotion']

    emo_neu = emo['neutral']

    if emo_neu < 0.9:
        return True
    else:
        return False
    


import requests
import json
import boto3

bucket = "palisade5365"
get_last_modified = lambda obj: int(obj['LastModified'].strftime('%s'))
s3 = boto3.client('s3')

subscription_key = '88f31bd2bc4d4773bdf0de12142fbd3c'
assert subscription_key

face_api_url = 'https://koreacentral.api.cognitive.microsoft.com/face/v1.0/detect'



#headers = {'Ocp-Apim-Subscription-Key': subscription_key, 'Content-Type':'application/json'}
headers = {'Ocp-Apim-Subscription-Key': subscription_key, 'Content-Type':'application/octet-stream'}


params = {
        'returnFaceId': 'true',
            'returnFaceLandmarks': 'true',
                'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
}

def getFace():
    image_url = 'https://palisade5365.s3.ap-northeast-2.amazonaws.com/' + 'normal/001.jpg'

    dat = open('/home/ubuntu/byeongkwan/local_send/001.jpg','rb')
    response = requests.post(face_api_url, params=params,
                             headers=headers, data=dat)
                             #headers=headers, json={"url": image_url})
    return response
'''    
    try:
        land = response.json()[0]['faceLandmarks']
        emo = response.json()[0]['faceAttributes']['emotion']
    #    print(emo)
        ang = emo['anger']
        neutral = emo['neutral']
        elt = land['eyeLeftTop']
        elb = land['eyeLeftBottom']
        ert = land['eyeRightTop'] 
        erb = land['eyeRightBottom']
        left_dif = float(elb['y'])-float(elt['y'])
        right_dif = float(elb['y'])-float(elt['y'])
        if neutral < 0.5:
            print('Prediction: Sick')
            return 1
        elif left_dif < 20 and right_dif < 20:
            print('Prediction: Sleep')
            return 2
        else:
            print('Prediction: Normal')
            return 0
    except Exception:
        print('Cannot found face')
        '''


dat = open('/home/ubuntu/byeongkwan/local_send/001.jpg','rb')
print(dat)
#res = getFace()
#print(json.dumps(res.json(),indent=4))

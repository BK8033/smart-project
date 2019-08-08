import requests
import json

subscription_key = 'b1afff0faa3840fa83f270ec0f532a08'
assert subscription_key

face_api_url = 'https://koreacentral.api.cognitive.microsoft.com/face/v1.0/detect'

#image_url = 'https://sagemaker-us-west-2-334381301451.s3-us-west-2.amazonaws.com/face.jpg'
#image_url = 'https://palisade5365.s3.ap-northeast-2.amazonaws.com/KakaoTalk_20190802_121022653.jpg' 
image_url = 'https://palisade5365.s3.ap-northeast-2.amazonaws.com/KakaoTalk_20190802_121830804.jpg'

headers = {'Ocp-Apim-Subscription-Key': subscription_key}

params = {
        'returnFaceId': 'true',
            'returnFaceLandmarks': 'true',
                'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion',
}

response = requests.post(face_api_url, params=params,
                         headers=headers, json={"url": image_url})

#print(json.dumps(response.json(), indent = 4))
#emo = response.json()[0]['faceAttributes']['emotion']

print(json.dumps(response.json(), indent=4))

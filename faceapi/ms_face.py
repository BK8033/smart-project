import requests
import json

subscription_key = 'b1afff0faa3840fa83f270ec0f532a08'
assert subscription_key

face_api_url = 'https://koreacentral.api.cognitive.microsoft.com/face/v1.0/detect'

#image_url = 'https://sagemaker-us-west-2-334381301451.s3-us-west-2.amazonaws.com/abnormal2/20190711_102915_005.jpg'
image_url = 'http://photo.jtbc.joins.com/news/2016/07/04/20160704171307899.jpg'


headers = {'Ocp-Apim-Subscription-Key': subscription_key}

params = {
        'returnFaceId': 'true',
            'returnFaceLandmarks': 'false',
                'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
}

response = requests.post(face_api_url, params=params,
                         headers=headers, json={"url": image_url})
print('Answer..')
print(response.json()[0]['faceAttributes']['emotion'])
#print(response.json())

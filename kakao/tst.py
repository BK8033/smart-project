import requests

URL = 'https://api.solapi.com/messages/v4/send'

parameter = {'Authorizatio':'NCS3CFAYW7TVC6EP', 'message':'TEST #1'}

res = requests.post(URL, params = parameter)

print(res.text)

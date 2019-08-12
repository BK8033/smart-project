import requests

url = 'http://127.0.0.1:5365/test'
condi = input('ENTER ANY NUMBER >> ')

res = requests.get(url,params = {'condi':int(condi)})

print(res)

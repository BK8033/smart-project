import requests

url = 'http://127.0.0.1:5365/test'


condi = 0
res = requests.get(url)

res = requests.get(url,params = {'condi':int(condi)})

print(res)

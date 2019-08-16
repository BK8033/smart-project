import requests

url = 'http://127.0.0.1:5365/upload'
condi = input('ENTER ANY NUMBER >> ')
res = requests.get(url)
'''
res = requests.get(url,params = {'condi':int(condi)})
'''
print(res)

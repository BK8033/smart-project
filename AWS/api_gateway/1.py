import requests

URL = 'http://52.43.95.248:5001/pi'

params = {'number': 10}
try:
    res = requests.get(URL,timeout = 5)
except Exception as ex:
    print(ex)
print(res.text)

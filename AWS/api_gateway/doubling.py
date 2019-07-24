import requests

URL = 'https://5bfvz316rj.execute-api.us-west-2.amazonaws.com/prod/tst'

params = {'number': 10}

res = requests.get(URL, params = params)

print(res.text)

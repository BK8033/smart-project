import requests
import time
#url = 'https://5bfvz316rj.execute-api.us-west-2.amazonaws.com/prod/whois?number=1'
url = 'http://166.104.167.22:21000/OnLed'

#n = input('Enter the number: ')
st = time.time()
#params['number'] = n
params = {'name':'12'}
print('start..')
#res = requests.get(url, params = params)
rest = requests.post(url, json = params)
#res = requests.post(url)

#print(rest.text)
print('time = ', time.time()-st)

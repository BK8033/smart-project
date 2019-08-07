import requests
from urllib.parse import urlencode, quote_plus, unquote

#url = 'https://5bfvz316rj.execute-api.us-west-2.amazonaws.com/prod/whois?number=1'
#url = 'http://166.104.167.22:21000/OnLed'
url = 'http://apis.data.go.kr/B552657/ErmctInfoInqireService/getEmrrmRltmUsefulSckbdInfoInqire'
key = 'DMbhCCZSytC0q3lJ7S%2F8oOvGQrunh7pysqKbDMfe7MFgxHS80avJhGYqOSWkF5iIhMf%2BL4RE%2B976NfIvSp30EA%3D%3D'
#key = 'pqqz%2B02naMh%2FJh28pVJ0iP7Pz2cJNDUzWTBs1JaBZzMI4d8Lz4my6TqHba8tFCSFKW2BurZLnAhfDIqg1oYrCg%3D%3D'
#param = {'ServiceKey' : 'DMbhCCZSytC0q3lJ7S%2F8oOvGQrunh7pysqKbDMfe7MFgxHS80avJhGYqOSWkF5iIhMf%2BL4RE%2B976NfIvSp30EA%3D%3D',
param = {'ServiceKey' : unquote(key),
    'ServiceKey' : '-', 'pageNo' : '1','numOfRows' : '10', 'HPID' : 'A0000028', 'QN' : '삼성병원', 'Q0' : '서울특별시', 'Q1' : '강남구' }

print('start..')
#res = requests.get(url, params = params)
#rest = requests.get(url+'?'+urlencode(param, quote_via=quote_plus))
rest = requests.get(url,params=param)
#res = requests.post(url)
print(rest.text)
#print(rest.text)
#print('time = ', time.time()-st)


from urllib2 import Request, urlopen
from urllib import urlencode, quote_plus

url = 'http://apis.data.go.kr/B552657/HsptlAsembySearchService/getHsptlMdcncLcinfoInqire'
queryParams = '?' + urlencode({ quote_plus('ServiceKey') : 'DMbhCCZSytC0q3lJ7S%2F8oOvGQrunh7pysqKbDMfe7MFgxHS80avJhGYqOSWkF5iIhMf%2BL4RE%2B976NfIvSp30EA%3D%3D', quote_plus('') : '' })

request = Request(url + queryParams)
request.get_method = lambda: 'GET'
response_body = urlopen(request).read()
print(response_body)

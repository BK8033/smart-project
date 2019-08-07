import requests
import json
from pprint import pprint
import xml.etree.ElementTree as elemTree

lati = '37.558214'
longi = '127.046238'
server_key = 'DMbhCCZSytC0q3lJ7S%2F8oOvGQrunh7pysqKbDMfe7MFgxHS80avJhGYqOSWkF5iIhMf%2BL4RE%2B976NfIvSp30EA%3D%3D'
normal_key = 'pqqz%2B02naMh%2FJh28pVJ0iP7Pz2cJNDUzWTBs1JaBZzMI4d8Lz4my6TqHba8tFCSFKW2BurZLnAhfDIqg1oYrCg%3D%3D'

url_1 = 'http://apis.data.go.kr/B552657/ErmctInfoInqireService/getEmrrmRltmUsefulSckbdInfoInqire'
url_2 = 'http://apis.data.go.kr/B552657/ErmctInfoInqireService/getEgytLcinfoInqire'

url_1 = url_1 + '?ServiceKey=' + normal_key
url_2 = url_2 + '?ServiceKey=' + normal_key
#url = url + '&STAGE1=서울특별시&STAGE2=성동구&pageNo=1'
#url = url + '&WGS84_LON=' + longi + '&WGS84_LAT=' +lati
res = requests.get(url_1)

root = elemTree.fromstring(res.text)

#print(root.find("body").text)
#print(res.text)
print(root.text)



body = root.find("body").find("items").find("item")
items = root.find("body").find("items")
for i in items:
    print(i.find("dutyName").text)


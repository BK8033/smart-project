import tst_nugu
import tst_face
import requests

emer_url = 'http://127.0.0.1:5365/condi'
while True:
    condi = tst_face.isSick()
    
    if condi == 1:
        print('It seems occupant is sick')
        params={'code':'1'}
        res = requests.get(emer_url, params=params)
    elif condi == 2:
        print('It seems occupant is sleep')
        params={'code':'2'}
        res = requests.get(emer_url, params=params)
    else:
        print('It is OK')  


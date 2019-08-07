##############################################
#누구에게 신호를 보냄

##############################################
import requests

URL = 'http://102.168.0.5'  #라즈베리파이 IP주소가 들어가야함

params = {'number': 10}

def toNUGU():
    try:
        res = requests.get(URL, params = params,timeout = 3)
        return [True,res]
    except requests.exceptions.Timeout:
#        print('NUGU IS NOT CONNECTED')
        return [False,'0']


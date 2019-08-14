import webbrowser
import requests
import time


get_url = 'http://18.236.66.232:5365/blink'
stream_url = 'http://172.20.10.2:8090/?action=stream'
kmap_url = 'http://18.236.66.232:8033/map'
while True:
    response = requests.get(url)
    condi = response.json()['condition']
    if condi == 5:
        webbrowser.open(stream_url)
        webbrowser.open(kmap_url)

    time.sleep(0.1)
       



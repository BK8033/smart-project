import cv2
import boto3
import time
import requests
from datetime import datetime

file_n = 1
bucket_name ="palisade5365"
s3 = boto3.client('s3')

img = cv2.VideoCapture(2)
url = 'http://18.236.66.232:5365/upload'
i = 0
        
while True:   
    if img.isOpened()==True:
        ret, frame = img.read()
        filename =  datetime.today().strftime('%Y-%m-%d-%H:%M:%S')+ ".jpg"
        cv2.imwrite(filename,frame)
        s3.upload_file(filename,bucket_name,"pic/"+filename,ExtraArgs={'ACL':'public-read'})
        print(filename+" sended")
        
        requests.get(url)
        file_n+=1
        if file_n >10:
            break


    else:
        print 'img is not opened'
        break



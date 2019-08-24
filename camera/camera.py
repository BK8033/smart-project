import cv2
import boto3
import time
import os
import requests
from datetime import datetime
import threading

img = cv2.VideoCapture(0)
lock = threading.Lock()


bucket_name ="palisade5365"
s3 = boto3.client('s3',
        aws_access_key_id = "AKIAU3WVNX3F76F7IZ4T",
        aws_secret_access_key = "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" 
        #aws_session_token = "
        )
url = 'http://18.236.66.232:5365/upload'
file_n = 1

def cam():
    global lock, ret, frame
    print ("cam start")
    while True:
        with lock:
            print ("cam lock in")
            ret, frame = img.read()
        #time.sleep(0.2)

        #print 'cam release lock'
        
def upload():
    print ("upload start")
    global lock, ret, frame, file_n


    while True:
        if img.isOpened()==True:
            with lock:
                #print 'upload lock in'
                ret, frame = img.read()
                filename =  datetime.today().strftime('%Y-%m-%d-%H:%M:%S')+ ".jpg"
                cv2.imwrite(filename,frame)
                print (filename + " sended")

            #print 'upload release lock'
                s3.upload_file(filename,bucket_name,"pic/"+filename,ExtraArgs={'ACL':'public-read'})
                requests.get(url)

            #time.sleep(0.7)
            
            file_n+=1
            if file_n > 1000:

                print ("finish")
                break

        else:
            print ("img is not opened")
            return 


if __name__=='__main__':
    t1 = threading.Thread(target=upload)
    t2 = threading.Thread(target=cam)
    t1.start()
    t2.start()


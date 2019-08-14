from flask import Flask, request
import json
import sys
import tst_face as tf
import threading
import time
app = Flask(__name__)

#########################################################
#                                                       #
#                   [Condition]                         #
#                                                       #
#                                                       #
#       1: 아프다고 생각하는 경우                       #
#       2: 잔다고 생각하는 경우                         #
#       3: 1-> 아프지 않는 경우                         #
#       4: 2-> 몇분 잔다고 했을 경우                    #
#       5: 사람이 최종적으로 아프다고 했을 경우         # 
#       6: NUGU에서 답변 없을 경우                      #
#                                                       # 
#                                                       # 
#                                                       # 
#                                                       # 
#                   [Flag]                              #
#                                                       # 
#       1: 쓰레드 시작                                  # 
#       2: 타이머 끝나서 위기상황                       #
#       3: NUGU가 괜찮다는 신호를 보냄                  #
#                                                       #      
#                                                       # 
#                                                       # 
#                                                       # 
#                                                       # 
#                                                       # 
#                                                       # 
#                                                       # 
#                                                       # 
#                                                       # 
#########################################################


global condition
global flag
global sec
global nugu_wait_time
condition = 0
flag = 0
nugu_wait_time = 15
sec = -1

'''
###############################################
#   Threading                                 #
###############################################
'''
def myTimer():
    global flag,nugu_wait_time,condition
    flag = 1
    time.sleep(nugu_wait_time)
    if flag != 3:
        print('No signal from NUGU')
        condition = 6
    flag=2


global ti
ti = threading.Thread(target = myTimer)

@app.route('/bcare', methods = ['GET'])
def bluceCB():
    global condition
    return {'condition':condition}

@app.route('/realEmer', methods = ['GET'])
def reCB():
    global condition
    condition = 5
    return {'condition': 'OK'}

@app.route('/digitalpost',methods = ['GET'])
def digitalCB():
    global condition
    return {'condition': condition}

@app.route('/pirequest', methods = ['GET'])
def toPI():
    '''
    ###################################
    #       get global parameters     #
    ###################################
    '''
    global condition
    global sec
    global flag
    global ti
    
    '''
    ###################################
    #       making response           #
    ###################################
    '''
    output = {}
    output['code'] = int(condition)
    
 
    cmd = int(condition)


    if cmd == 4:
        print('rasp got sleep signal')
        output['sec'] = sec
        sec = -1
    elif cmd == 1:
        ti.start()
        print('thread start')

    '''
    #########################################################
    #       if pi get not 0 condition initialize            #
    #########################################################
    '''

    if condition != 0 and condition != 6:
        condition = 0
  


    return output
    

@app.route('/upload', methods = ['GET'])
def uploadCB():
    global condition
    condition = tf.isSick()
    print('present state:', condition) 
    output = {'code':'200'}
    return output

@app.route('/test',methods =['GET'])
def testCB():
    global condition
    condition = request.args.get('condi')
    codition = int(condition)
    output = {'code':'200'}
    return json.dumps(output)
'''
#####################################################
#           NUGU                                    #
#####################################################
'''

@app.route('/SEATDOWN',methods = ['POST'])
def sleepCB():    
    
    ############DO NOT THIS AREA########################
    global sec
    global condition
    condition = 4
    req = request.json
    response = {}
    act = req['action']['parameters']
    response['version'] = req['version']
    response['resultCode'] = 'OK'
    #####################################

    sec = act['TIME']['value']
    output = {'TIMEVALUE': sec}
    print('NUGU siganl, ', sec, ' sleep')  
    response['output'] = output
    json_data = json.dumps(response)
    return json_data


@app.route('/EMERGENCYSITUATION',methods = ['POST'])
def emerCB():
    global flag
    if flag == 2:
        print('Emergency happened!')
    elif flag == 1:
        flag = 3
    req = request.json
    response = {}
    response['version'] = req['version']
    response['resultCode'] = 'OK'
  
  #  response['output'] = output
    json_data = json.dumps(response)
    return json_data


    
if __name__ == '__main__':
	app.run(host='0.0.0.0', port = 5365 ,debug=True)

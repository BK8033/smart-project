from flask import Flask, request
import json
import sys
import tst_face as tf

app = Flask(__name__)

global condition
condition = 0
global sec
sec = -1

@app.route('/pirequest', methods = ['GET'])
def toPI():
    global condition
    global sec

    output = {}
    output['code'] = condition
#    print('condi type =',type(condition))
    if condition == 4:
        print('rasp got sleep signal')
        output['sec'] = sec
        sec = -1
    elif condition == 3:
        ##########################

        #   WHEN OCCUPANT SICK   #

        ##########################
        print(3)

    if condition != 0:
    #    print('Pi get signal')
        condition = 0
    return output
    

@app.route('/upload', methods = ['GET'])
def uploadCB():
    global condition
    condition = tf.isSick()
    print('present state:', condition) 
    output = {'code':'200'}
    return output

@app.route('/SEATDOWN',methods = ['POST'])
def sleepCB():    
    
    ####################################
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
def seatdownCB():
    print('emer fcn call')




    
if __name__ == '__main__':
	app.run(host='0.0.0.0', port = 5365 ,debug=True)

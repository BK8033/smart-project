from flask import Flask, request
import json
import sys

app = Flask(__name__)

global condition
condition = False

@app.route('/condi',methods = ['GET'])
def condiCB():
    global condition
    print('emergency signal in')
    condition = True
    res = {}
    res['code'] = '200'
    json_data = json.dumps(res)
    return json_data
   

@app.route('/pirequest', methods = ['GET'])
def toPI():
    global condition
    output = {'condition':condition}
    if condition == True:
        print('emer signal out')
        condition = False
    return output
    




if __name__ == '__main__':
	app.run(host='0.0.0.0', port = 5365 ,debug=True)

from flask import Flask, request
import json
import sys

app = Flask(__name__)

global condition
condition = 0

@app.route('/condi',methods = ['GET'])
def condiCB():
    global condition
    condition = request.args.get('code')
    req = request.json
    res = {}
    res['code'] = '200'
    json_data = json.dumps(res)
    return json_data
  

@app.route('/pirequest', methods = ['GET'])
def toPI():
    global condition
    output = {'code':condition}
    if condition != 0:
        print('Pi get signal')
        condition = 0
    return output
    




if __name__ == '__main__':
	app.run(host='0.0.0.0', port = 5365 ,debug=True)

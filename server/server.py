from flask import Flask, request
import json
import sys

app = Flask(__name__)

global sec
sec = -1

@app.route('/SEATDOWN',methods = ['POST'])
def dataFromNugu():

	#### DO NOT THIS AREA ####
	global sec
	req = request.json
	response = {}
	act = req['action']['parameters']
	response['version'] = req['version']
	response['resultCode'] = 'OK'
	##########################

	#print(act)
	#sys.stdout.flush()
	sec = act['TIME']['value']
	output = {'TIMEVALUE': sec }
	response['output'] = output
	json_data = json.dumps(response)
	return json_data


@app.route('/pirequest', methods = ['GET'])
def toPI():
	global  sec
	output = {'SEC':sec}
	#print(output)
	#sys.stdout.flush()
	sec = -1
	return output




if __name__ == '__main__':
	app.run(host='0.0.0.0', port = 5001 ,debug=True)

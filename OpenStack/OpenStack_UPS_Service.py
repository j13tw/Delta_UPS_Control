#!/usr/bin/python
import requests
import json
import os, sys
import socket
from flask import Flask
from flask import render_template
from decimal import getcontext, Decimal

app = Flask(__name__)

connect = ''
systemMode = 0
inputLine = 0
inputFreq = 0
inputVolt = 0
outputLine = 0
outputFreq = 0
outputVolt = 0
outputWatt = 0
outputAmp = 0
outputPersent = 0
lastBattery_Year = 0
lastBattery_Mon = 0
lastBattery_Day = 0
nextBattery_Year = 0
nextBattery_Mon = 0
nextBattery_Day = 0
hostname = ''
port = ''

def connectDevice():
	global hostname, port
	global connect, systemMode
	global inputLine, inputFreq, inputVolt
	global outputLine, outputFreq, outputVolt, outputWatt, outputAmp, outputPersent
	global lastBattery_Year, lastBattery_Mon, lastBattery_Day
	global nextBattery_Year, nextBattery_Mon, nextBattery_Day
	
	hostname = '10.0.0.164'					#chang to your service IP
	port = '5000'							#chang to your service Port
	localOS = os.system('uname 2>&1 >/var/tmp/os.txt')
	if(localOS == 0):
		response = os.system('ping -c 1 ' + hostname + ' &>/var/tmp/ping.txt')
#		os.system('clear')
	else:
		response = os.system('ping -n 1 ' + hostname + ' 2>&1 >ping.txt')
#		os.system('cls')

	if response == 0:						# check network sevice & server is on
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		result = sock.connect_ex((hostname, int(port)))
		if result == 0:
			sock.close()
			distance = 'http://' + hostname + ':' + port
			r = requests.get(distance)
			value = r.content.decode('utf-8')	# get return json value
			key = json.loads(value)
	#		print (json.dumps(key , sort_keys=True, indent=4, separators=(',', ': ')))	# show on the all split json format
	#		change the json key to local temp value
			connect = key['connect']
			lastBattery = key['battery'][0]
			nextBattery = key['battery'][1]
			inputStatus = key['input'][0]
			outputStatus = key['output'][0]
			inputLine = inputStatus['inputLine']
			inputFreq = inputStatus['inputFreq']
			inputVolt = inputStatus['inputVolt']
			systemMode = outputStatus['systemMode']
			outputLine = outputStatus['outputLine']
			outputFreq = outputStatus['outputFreq']
			outputVolt = outputStatus['outputVolt']
			outputAmp = outputStatus['outputAmp']
			outputWatt = outputStatus['outputWatt']
			outputPersent = outputStatus['outputPersent']
			lastBattery_Year = lastBattery['lastBattery_Year']
			lastBattery_Mon = lastBattery['lastBattery_Mon']
			lastBattery_Day = lastBattery['lastBattery_Day']
			nextBattery_Year = nextBattery['nextBattery_Year']
			nextBattery_Mon = nextBattery['nextBattery_Mon']
			nextBattery_Day = nextBattery['nextBattery_Day']
		else:
		   	print ('http://' + hostname +':' + port + ' Service Port Found !')
	else:
	  	print ('http://', hostname, ' Server IP Not Found !')

@app.route("/")
def dashBoard():
	global hostname, port
	global connect, systemMode
	global inputLine, inputFreq, inputVolt
	global outputLine, outputFreq, outputVolt, outputWatt, outputAmp, outputPersent
	global lastBattery_Year, lastBattery_Mon, lastBattery_Day
	global nextBattery_Year, nextBattery_Mon, nextBattery_Day
	connectDevice()
	return render_template('mainBoard.html', \
		 		hostname = hostname, \
		 		port = port, \
		 		serName = str(connect), \
		 		inputVolt = inputVolt, \
		 		inputFreq = inputFreq, \
		 		inputLine = inputLine, \
		 		systemMode = str(systemMode), \
				outputLine = outputLine, \
				outputVolt = outputVolt, \
				outputAmp = Decimal(outputAmp)*1, \
		 		outputPersent = outputPersent, \
		 		outputWatt = int(outputWatt)/1000, \
		 		outputFreq = outputFreq, \
		 		lastBattery_Year = lastBattery_Year, \
		 		lastBattery_Mon = lastBattery_Mon, \
		 		lastBattery_Day = lastBattery_Day, \
		 		nextBattery_Year = nextBattery_Year, \
		 		nextBattery_Mon = nextBattery_Mon, \
		 		nextBattery_Day = nextBattery_Day, \
		 		)

if __name__ == "__main__":
#	app.run(debug = True)
	app.run(host = "0.0.0.0")
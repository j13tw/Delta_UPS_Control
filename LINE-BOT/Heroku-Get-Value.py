#!/usr/bin/python
import requests
import json
import os, sys
import socket
from flask import Flask, request
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
outputPercent = 0
batteryHealth = ''
batteryStatus = ''
batteryCharge_Mode = ''
batteryVolt = 0
batteryTemp = 0
batteryRemain_Percent = 0
lastBattery_Year = 0
lastBattery_Mon = 0
lastBattery_Day = 0
nextBattery_Year = 0
nextBattery_Mon = 0
nextBattery_Day = 0

@app.route('/LineBot', methods=['POST', 'GET'])
def LineBot():
	global connect, systemMode
	global inputLine, inputFreq, inputVolt
	global outputLine, outputFreq, outputVolt, outputWatt, outputAmp, outputPercent
	global batteryHealth, batteryStatus, batteryCharge_Mode
	global batteryVolt, batteryTemp, batteryRemain_Percent
	global lastBattery_Year, lastBattery_Mon, lastBattery_Day
	global nextBattery_Year, nextBattery_Mon, nextBattery_Day

	if request.method == 'POST':
		r = request.json
		tmp = json.dumps(r)
		key = json.loads(tmp)
		print (key)
		connect = key['connect']
		status = key['battery'][0]['status'][0]
		batteryHealth = status['batteryHealth']
		batteryStatus = status['batteryStatus']
		batteryCharge_Mode = status['batteryCharge_Mode']
		batteryVolt = status['batteryVolt']
		batteryTemp = status['batteryTemp']
		batteryRemain_Percent = status['batteryRemain_Percent']
		lastBattery = key['battery'][1]
		nextBattery = key['battery'][2]
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
		outputPercent = outputStatus['outputPercent']
		lastBattery_Year = lastBattery['lastBattery_Year']
		lastBattery_Mon = lastBattery['lastBattery_Mon']
		lastBattery_Day = lastBattery['lastBattery_Day']
		nextBattery_Year = nextBattery['nextBattery_Year']
		nextBattery_Mon = nextBattery['nextBattery_Mon']
		nextBattery_Day = nextBattery['nextBattery_Day']
		return 'OK !'
	else:
		return render_template('mainBoard.html', \
		 		serName = str(connect), \
		 		inputVolt = inputVolt, \
		 		inputFreq = inputFreq, \
		 		inputLine = inputLine, \
		 		systemMode = str(systemMode), \
				outputLine = outputLine, \
				outputVolt = outputVolt, \
				outputAmp = Decimal(outputAmp)*1, \
		 		outputPercent = outputPercent, \
		 		outputWatt = int(outputWatt)/1000, \
		 		outputFreq = outputFreq, \
		 		batteryHealth = batteryHealth, \
		 		batteryStatus = batteryStatus, \
		 		batteryCharge_Mode = batteryCharge_Mode, \
		 		batteryVolt = batteryVolt, \
		 		batteryTemp = batteryTemp, \
		 		batteryRemain_Percent = batteryRemain_Percent, \
		 		lastBattery_Year = lastBattery_Year, \
		 		lastBattery_Mon = lastBattery_Mon, \
		 		lastBattery_Day = lastBattery_Day, \
		 		nextBattery_Year = nextBattery_Year, \
		 		nextBattery_Mon = nextBattery_Mon, \
		 		nextBattery_Day = nextBattery_Day, \
		 		)

	

#		print (json.dumps(key , sort_keys=True, indent=4, separators=(',', ': ')))	# show on the all split json format
#		change the json key to local temp value
	

@app.route('/show', methods=['GET'])
def show():
	global connect, systemMode
	global inputLine, inputFreq, inputVolt
	global outputLine, outputFreq, outputVolt, outputWatt, outputAmp, outputPercent
	global batteryHealth, batteryStatus, batteryCharge_Mode
	global batteryVolt, batteryTemp, batteryRemain_Percent
	global lastBattery_Year, lastBattery_Mon, lastBattery_Day
	global nextBattery_Year, nextBattery_Mon, nextBattery_Day

	

if __name__ == '__main__':
#	app.run(debug = True)
	app.run(host = '127.0.0.1', port=5001, debug = True)
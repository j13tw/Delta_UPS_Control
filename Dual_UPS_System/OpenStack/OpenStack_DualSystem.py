#!/usr/bin/python
import requests
import json
import os, sys
import socket
from flask import Flask, request
from flask import render_template
from decimal import getcontext, Decimal

app = Flask(__name__)

ups_Life_A = ''
serialName_A = ''
systemMode_A = 0
inputLine_A = 0
inputFreq_A = 0
inputVolt_A = 0
outputLine_A = 0
outputFreq_A = 0
outputVolt_A = 0
outputWatt_A = 0
outputAmp_A = 0
outputPercent_A = 0
batteryHealth_A = ''
batteryStatus_A = ''
batteryCharge_Mode_A = ''
batteryRemain_Min_A = ''
batteryRemain_Sec_A = ''
batteryVolt_A = 0
batteryTemp_A = 0
batteryRemain_Percent_A = 0
lastBattery_Year_A = 0
lastBattery_Mon_A = 0
lastBattery_Day_A = 0
nextBattery_Year_A = 0
nextBattery_Mon_A = 0
nextBattery_Day_A = 0
ups_Life_B = ''
serialName_B = ''
systemMode_B = 0
inputLine_B = 0
inputFreq_B = 0
inputVolt_B = 0
outputLine_B = 0
outputFreq_B = 0
outputVolt_B = 0
outputWatt_B = 0
outputAmp_B = 0
outputPercent_B = 0
batteryHealth_B = ''
batteryStatus_B = ''
batteryCharge_Mode_B = ''
batteryRemain_Min_B = ''
batteryRemain_Sec_B = ''
batteryVolt_B = 0
batteryTemp_B = 0
batteryRemain_Percent_B = 0
lastBattery_Year_B = 0
lastBattery_Mon_B = 0
lastBattery_Day_B = 0
nextBattery_Year_B = 0
nextBattery_Mon_B = 0
nextBattery_Day_B = 0
hostname = ''
port = ''
hostHealth = ''



@app.route('/', methods=['POST', 'GET'])
def dashBoard():
	global hostname, port, hostHealth
	global serialName_A, systemMode_A, ups_Life_A
	global inputLine_A, inputFreq_A, inputVolt_A
	global outputLine_A, outputFreq_A, outputVolt_A, outputWatt_A, outputAmp_A, outputPercent_A
	global batteryHealth_A, batteryStatus_A, batteryCharge_Mode_A
	global batteryRemain_Min_A, batteryRemain_Sec_A, batteryVolt_A, batteryTemp_A, batteryRemain_Percent_A
	global lastBattery_Year_A, lastBattery_Mon_A, lastBattery_Day_A
	global nextBattery_Year_A, nextBattery_Mon_A, nextBattery_Day_A
	global serialName_B, systemMode_B, ups_Life_B
	global inputLine_B, inputFreq_B, inputVolt_B
	global outputLine_B, outputFreq_B, outputVolt_B, outputWatt_B, outputAmp_B, outputPercent_B
	global batteryHealth_B, batteryStatus_B, batteryCharge_Mode_B
	global batteryRemain_Min_B, batteryRemain_Sec_B, batteryVolt_B, batteryTemp_B, batteryRemain_Percent_B
	global lastBattery_Year_B, lastBattery_Mon_B, lastBattery_Day_B
	global nextBattery_Year_B, nextBattery_Mon_B, nextBattery_Day_B
	
	hostname = '10.0.0.164'					#chang to your service IP
	port = '5000'							#chang to your service Port
	localOS = os.system('uname 2>&1 >/var/tmp/os.txt')
	if(localOS == 0):
		response = os.system('ping -c 1 ' + hostname + ' 2>&1 >/var/tmp/ping.txt')
#		os.system('clear')
	else:
		response = os.system('ping -n 1 ' + hostname + ' 2>&1 >ping.txt')
#		os.system('cls')

	if response == 0:						# check network sevice & server is on
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		result = sock.connect_ex((hostname, int(port)))
		if result == 0:
			sock.close()
		else:
		   	print ('http://' + hostname +':' + port + ' Service Port Found !')
		   	hostHealth = 'Port Error'
	else:
	  	print ('http://', hostname, ' Server IP Not Found !')
	  	hostHealth = 'IP Error'

	try:
		if request.method == 'POST':
			r = request.json
			value = r.content.decode('utf-8')	# get return json value
			key = json.loads(value)
	#		print (json.dumps(key , sort_keys=True, indent=4, separators=(',', ': ')))	# show on the all split json format
	#		change the json key to local temp value
			ups_Life_A = key['ups_Life_A']
			serialName_A = key['connect_A']
			status_A = key['battery_A'][0]['status'][0]
			batteryHealth_A = status_A['batteryHealth_A']
			batteryStatus_A = status_A['batteryStatus_A']
			batteryCharge_Mode_A = status_A['batteryCharge_Mode_A']
			batteryRemain_Min_A = status_A['batteryRemain_Min_A']
			batteryRemain_Sec_A = status_A['batteryRemain_Sec_A']
			batteryVolt_A = status_A['batteryVolt_A']
			batteryTemp_A = status_A['batteryTemp_A']
			batteryRemain_Percent_A = status_A['batteryRemain_Percent_A']
			lastBattery_A = key['battery_A'][1]
			nextBattery_A = key['battery_A'][2]
			inputStatus_A = key['input_A'][0]
			outputStatus_A = key['output_A'][0]
			inputLine_A = inputStatus_A['inputLine_A']
			inputFreq_A = inputStatus_A['inputFreq_A']
			inputVolt_A = inputStatus_A['inputVolt_A']
			systemMode_A = outputStatus_A['systemMode_A']
			outputLine_A = outputStatus_A['outputLine_A']
			outputFreq_A = outputStatus_A['outputFreq_A']
			outputVolt_A = outputStatus_A['outputVolt_A']
			outputAmp_A = outputStatus_A['outputAmp_A']
			outputWatt_A = outputStatus_A['outputWatt_A']
			outputPercent_A = outputStatus_A['outputPercent_A']
			lastBattery_Year_A = lastBattery_A['lastBattery_Year_A']
			lastBattery_Mon_A = lastBattery_A['lastBattery_Mon_A']
			lastBattery_Day_A = lastBattery_A['lastBattery_Day_A']
			nextBattery_Year_A = nextBattery_A['nextBattery_Year_A']
			nextBattery_Mon_A = nextBattery_A['nextBattery_Mon_A']
			nextBattery_Day_A = nextBattery_A['nextBattery_Day_A']
			ups_Life_B = key['ups_Life_B']
			serialName_B = key['connect_B']
			status_B = key['battery_B'][0]['status'][0]
			batteryHealth_B = status_B['batteryHealth_B']
			batteryStatus_B = status_B['batteryStatus_B']
			batteryCharge_Mode_B = status_B['batteryCharge_Mode_B']
			batteryRemain_Min_B = status_B['batteryRemain_Min_B']
			batteryRemain_Sec_B = status_B['batteryRemain_Sec_B']
			batteryVolt_B = status_B['batteryVolt_B']
			batteryTemp_B = status_B['batteryTemp_B']
			batteryRemain_Percent_B = status_B['batteryRemain_Percent_B']
			lastBattery_B = key['battery_B'][1]
			nextBattery_B = key['battery_B'][2]
			inputStatus_B = key['input_B'][0]
			outputStatus_B = key['output_B'][0]
			inputLine_B = inputStatus_B['inputLine_B']
			inputFreq_B = inputStatus_B['inputFreq_B']
			inputVolt_B = inputStatus_B['inputVolt_B']
			systemMode_B = outputStatus_B['systemMode_B']
			outputLine_B = outputStatus_B['outputLine_B']
			outputFreq_B = outputStatus_B['outputFreq_B']
			outputVolt_B = outputStatus_B['outputVolt_B']
			outputAmp_B = outputStatus_B['outputAmp_B']
			outputWatt_B = outputStatus_B['outputWatt_B']
			outputPercent_B = outputStatus_B['outputPercent_B']
			lastBattery_Year_B = lastBattery_B['lastBattery_Year_B']
			lastBattery_Mon_B = lastBattery_B['lastBattery_Mon_B']
			lastBattery_Day_B = lastBattery_B['lastBattery_Day_B']
			nextBattery_Year_B = nextBattery_B['nextBattery_Year_B']
			nextBattery_Mon_B = nextBattery_B['nextBattery_Mon_B']
			nextBattery_Day_B = nextBattery_B['nextBattery_Day_B']
			hostHealth = 'Alive'
			return 'OK !'
	except:
		return render_template('mainBoard.html', \
		 		hostname = hostname, \
		 		port = port, \
		 		hostHealth = hostHealth, \
		 		serName_A = serialName_A, \
		 		inputVolt_A = inputVolt_A, \
		 		inputFreq_A = inputFreq_A, \
		 		inputLine_A = inputLine_A, \
		 		systemMode_A = str(systemMode_A), \
				outputLine_A = outputLine_A, \
				outputVolt_A = outputVolt_A, \
				outputAmp_A = Decimal(outputAmp_A)*1, \
		 		outputPercent_A = outputPercent_A, \
		 		outputWatt_A = outputWatt_A, \
		 		outputFreq_A = outputFreq_A, \
		 		batteryHealth_A = batteryHealth_A, \
		 		batteryStatus_A = batteryStatus_A, \
		 		batteryCharge_Mode_A = batteryCharge_Mode_A, \
		 		batteryRemain_Min_A = batteryRemain_Min_A, \
		 		batteryRemain_Sec_A = batteryRemain_Sec_A, \
		 		batteryVolt_A = batteryVolt_A, \
		 		batteryTemp_A = batteryTemp_A, \
		 		batteryRemain_Percent_A = batteryRemain_Percent_A, \
		 		lastBattery_Year_A = lastBattery_Year_A, \
		 		lastBattery_Mon_A = lastBattery_Mon_A, \
		 		lastBattery_Day_A = lastBattery_Day_A, \
		 		nextBattery_Year_A = nextBattery_Year_A, \
		 		nextBattery_Mon_A = nextBattery_Mon_A, \
		 		nextBattery_Day_A = nextBattery_Day_A, \
		 		serName_B = serialName_B, \
				inputVolt_B = inputVolt_B, \
				inputFreq_B = inputFreq_B, \
				inputLine_B = inputLine_B, \
				systemMode_B = str(systemMode_B), \
				outputLine_B = outputLine_B, \
				outputVolt_B = outputVolt_B, \
				outputAmp_B = Decimal(outputAmp_B)*1, \
				outputPercent_B = outputPercent_B, \
				outputWatt_B = outputWatt_B, \
				outputFreq_B = outputFreq_B, \
				batteryHealth_B = batteryHealth_B, \
				batteryStatus_B = batteryStatus_B, \
				batteryCharge_Mode_B = batteryCharge_Mode_B, \
				batteryRemain_Min_B = batteryRemain_Min_B, \
				batteryRemain_Sec_B = batteryRemain_Sec_B, \
				batteryVolt_B = batteryVolt_B, \
				batteryTemp_B = batteryTemp_B, \
				batteryRemain_Percent_B = batteryRemain_Percent_B, \
				lastBattery_Year_B = lastBattery_Year_B, \
				lastBattery_Mon_B = lastBattery_Mon_B, \
				lastBattery_Day_B = lastBattery_Day_B, \
				nextBattery_Year_B = nextBattery_Year_B, \
				nextBattery_Mon_B = nextBattery_Mon_B, \
				nextBattery_Day_B = nextBattery_Day_B, \
		 		)

if __name__ == '__main__':
#	app.run(debug = True)
	app.run(host = '0.0.0.0', port=5000)
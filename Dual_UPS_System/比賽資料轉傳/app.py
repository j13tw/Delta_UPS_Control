#!/usr/bin/python3.6
import requests
import json
import os, sys
import socket
from flask import Flask
from flask_restful import Resource, Api

hostname = '127.0.0.1'				#chang to your service IP
port = '8080'							#chang to your service Port

app = Flask(__name__)
api = Api(app)

class jsonReturn(Resource):
	def get(self):
		response = os.system('ping -c 1 ' + hostname)
		print(response)
		if (response == 0):
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			result = sock.connect_ex((hostname, int(port)))
			if result == 0:
				sock.close()
				distance = 'http://' + hostname + ':' + port
				#r = requests.get(distance)
				#print(r.content)
				#value = r.content.decode('utf-8')	
				resp = '{"connect_B": "/dev/ttyUSB1 (\\u7a97\\u6236)", "ups_Life_A": "onLine(\\u5728\\u7dda)", "connect_A": "/dev/ttyUSB0 (\\u7246\\u58c1)", "input_B": {"inputVolt_B": "217.0", "inputLine_B": "1", "inputFreq_B": "59.9"}, "battery_B": {"nextChange": {"nextBattery_Day_B": "22", "nextBattery_Year_B": "2020", "nextBattery_Mon_B": "3"}, "status": {"batteryCharge_Mode_B": "Boost charging (\\u5feb\\u901f\\u5145\\u96fb)", "batteryRemain_Percent_B": "100", "batteryRemain_Min_B": "None By Charging (\\u5145\\u96fb\\u4e2d)", "batteryVolt_B": "272", "batteryTemp_B": "33", "batteryStatus_B": "OK (\\u826f\\u597d)", "batteryHealth_B": "Good (\\u826f\\u597d)", "batteryRemain_Sec_B": "None By Charging (\\u5145\\u96fb\\u4e2d)"}, "lastChange": {"lastBattery_Day_B": "22", "lastBattery_Mon_B": "3", "lastBattery_Year_B": "2017"}}, "output_B": {"systemMode_B": "Normal", "outputWatt_B": "3.514", "outputLine_B": "1", "outputVolt_B": "221.0", "outputFreq_B": "59.9", "outputAmp_B": "15.9005", "outputPercent_B": "41"}, "output_A": {"outputPercent_A": "37", "outputLine_A": "1", "outputFreq_A": "59.9", "systemMode_A": "Normal", "outputAmp_A": "14.2658", "outputVolt_A": "222.0", "outputWatt_A": "3.167"}, "battery_A": {"nextChange": {"nextBattery_Mon_A": "3", "nextBattery_Year_A": "2020", "nextBattery_Day_A": "22"}, "status": {"batteryRemain_Min_A": "None By Charging (\\u5145\\u96fb\\u4e2d)", "batteryStatus_A": "OK (\\u826f\\u597d)", "batteryTemp_A": "36", "batteryHealth_A": "Good (\\u826f\\u597d)", "batteryCharge_Mode_A": "Boost charging (\\u5feb\\u901f\\u5145\\u96fb)", "batteryRemain_Percent_A": "100", "batteryRemain_Sec_A": "None By Charging (\\u5145\\u96fb\\u4e2d)", "batteryVolt_A": "270"}, "lastChange": {"lastBattery_Year_A": "2017", "lastBattery_Mon_A": "3", "lastBattery_Day_A": "22"}}, "ups_Life_B": "onLine(\\u5728\\u7dda)", "input_A": {"inputVolt_A": "217.0", "inputLine_A": "1", "inputFreq_A": "59.9"}}'
				return json.loads(resp)
			else:
				resp = '{"message":' + '"connect-error" }'
				return json.loads(resp)
		else:
			resp = '{"message":' + '"network-error"}'
			json.loads(resp)

data =  '{"message" : ' + '"network-error"}'
api.add_resource(jsonReturn, '/')

if __name__ == '__main__':
#	app.run(debug = True)
	app.run(host = '0.0.0.0', port=8080)
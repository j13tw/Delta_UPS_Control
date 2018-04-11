#!/usr/bin/python3.6
import requests
import json
import os, sys
import socket


hostname = '10.0.0.164'					#chang to your service IP
port = '5000'							#chang to your service Port

localOS = os.system('uname 2>&1 >/var/tmp/os.txt')
if(localOS == 0):
	response = os.system('ping -c 1 ' + hostname + ' &>/var/tmp/ping.txt')
#	os.system('clear')
else:
	response = os.system('ping -n 1 ' + hostname + ' 2>&1 >ping.txt')
#	os.system('cls')

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
		status = key['battery'][0]['status'][0]
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
		outputPersent = outputStatus['outputPersent']
		batteryHealth = status['batteryHealth']
		batteryStatus = status['batteryStatus']
		batteryCharge_Mode = status['batteryCharge_Mode']
		batteryRemain_Min = status['batteryRemain_Min']
		batteryRemain_Sec = status['batteryRemain_Sec']
		batteryTemp = status['batteryTemp']
		lastBattery_Year = lastBattery['lastBattery_Year']
		lastBattery_Mon = lastBattery['lastBattery_Mon']
		lastBattery_Day = lastBattery['lastBattery_Day']
		nextBattery_Year = nextBattery['nextBattery_Year']
		nextBattery_Mon = nextBattery['nextBattery_Mon']
		nextBattery_Day = nextBattery['nextBattery_Day']
#####################################################################################################################################
		print('Service IP : http://' + hostname + ':' + port)																		#
		print('USB 連接位置 : ' + connect)																							#
		print('-----------------------------------------')																			#
		print ('輸入線路 : ' + str(inputLine) + ' 號線路')																			#
		print ('輸入頻率 : ' + str(inputFreq) + ' Hz')																				#
		print ('輸入電壓 : ' + str(inputVolt) + ' V')																				#
		print('-----------------------------------------') 																			#
		print ('輸出狀態 : '+ systemMode)																							#
		print ('輸出線路 : ' + str(outputLine) + ' 號線路')																			#
		print ('輸出頻率 : ' + str(outputFreq) + ' Hz')																				#
		print ('輸出電壓 : ' + str(outputVolt) + ' V')																				#
		print ('輸出電流 : ' + outputAmp + 'A')																						#
		print ('輸出瓦特 : ' + str(int(outputWatt)/1000) + ' KW')																	#
		print ('輸出負載比 : ' + str(outputPersent) + ' %')																			#
		print('-----------------------------------------')																			#
		print ('電池健康度 : ' + batteryHealth)																						#
		print ('電池狀態 : ' + batteryStatus)																						#
		print ('充電模式 : ' + batteryCharge_Mode)																					#
		print ('電池電壓 : %3.1f V' %batteryVolt)																					#
		print ('輸出剩餘時間(分) : ' + batteryRemain_Min)																			#
		print ('輸出剩餘時間(秒) : ' + batteryRemain_Sec)																			#
		print ('電量剩餘百分比 : ' + str(batteryRemain_Percent) + ' %')																#
		print ('UPS 內部溫度 : ' + str(batteryTemp) + ' °C')																		#
		print('-----------------------------------------')																			#
		print ('電池更換時間 : ' + str(lastBattery_Year) + ' 年 ' + str(lastBattery_Mon) + ' 月 ' + str(lastBattery_Day) + ' 日')	#
		print ('下次更換時間 : ' + str(nextBattery_Year) + ' 年 ' + str(nextBattery_Mon) + ' 月 ' + str(nextBattery_Day) + ' 日')	#
#####################################################################################################################################
		sys.exit(0)
	else:
	   	print ('http://' + hostname +':' + port + ' Service Port Found !')
	   	sys.exit(1)   
else:
  	print ('http://', hostname, ' Server IP Not Found !')
  	sys.exit(1)
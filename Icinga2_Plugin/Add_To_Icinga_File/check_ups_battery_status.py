#!/usr/bin/python3.6
import requests
import json
import os, sys
import socket


hostname = '10.0.0.164'					#chang to your service IP
port = '5000'							#chang to your service Port

localOS = os.system('uname 2>&1 >/var/tmp/os.txt')
if(localOS == 0):
	response = os.system('ping -c 1 ' + hostname + ' 2>&1 >/var/tmp/ping.txt')
else:
	response = os.system('ping -n 1 ' + hostname + ' 2>&1 >ping.txt')

if response == 0:						# check network sevice & server is on
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	result = sock.connect_ex((hostname, int(port)))
	if result == 0:
		sock.close()
		distance = 'http://' + hostname + ':' + port
		r = requests.get(distance)
		value = r.content.decode('utf-8')	# get return json value
		key = json.loads(value)
		outputStatus = key['battery'][0]['status'][0]
		batteryStatus = outputStatus['batteryStatus']
		if batteryStatus == 'Low (低電量)':
			print ("Battery Status : "+ batteryStatus + "(Please Charge battery or Close Service now !)")
			sys.exit(3)
		elif batteryStatus == 'Depleted (耗盡)':
			print ("Battery Status : "+ batteryStatus + "(The Battery has no any power !)")
			sys.exit(3)
		else:
			print ("Battery Status : "+ batteryStatus)
			sys.exit(0)
	else:
	   	print ('http://' + hostname +':' + port + ' Service Port Found !')
	   	sys.exit(2)   
else:
  	print ('http://', hostname, ' Server IP Not Found !')
  	sys.exit(2)
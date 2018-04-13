#!/usr/bin/python3.6
import requests
import json
import os, sys
import socket


hostname = '10.0.0.197'					#chang to your service IP
port = '5000'							#chang to your service Port

localOS = os.system('uname 2>&1 >/var/tmp/os.txt')
if(localOS == 0):
	response = os.system('ping -c 1 ' + hostname + ' 2>&1 >/var/tmp/ping.txt')
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
		outputStatus = key['output_A'][0]
		systemMode = outputStatus['systemMode_A']
		if systemMode == "Normal":
			print ("System Status : "+ systemMode + " (AC plug-in)")
			sys.exit(0)
		if systemMode == "Battery":
			print ("System Status : "+ systemMode + " (call user close service !)")
			sys.exit(1)
		if systemMode == "Other":
			print ("System Status : "+ systemMode)
			sys.exit(2)
		if systemMode == "No output":
			print ("System Status : "+ systemMode)
			sys.exit(3)
	else:
	   	print ('http://' + hostname +':' + port + ' Service Port Found !')
	   	sys.exit(2)   
else:
  	print ('http://', hostname, ' Server IP Not Found !')
  	sys.exit(2)
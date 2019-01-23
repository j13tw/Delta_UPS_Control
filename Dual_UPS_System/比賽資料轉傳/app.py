#!/usr/bin/python3.6
import requests
import json
import os, sys
import socket
from flask import Flask
from flask_restful import Resource, Api

hostname = '10.0.0.197'					#chang to your service IP
port = '5000'							#chang to your service Port

app = Flask(__name__)
api = Api(app)

class jsonReturn(Resource):
	def get(self):
		response = os.system('ping -c 1 ' + hostname + ' 2>&1 > ./ping.txt')
		print(response)
		print('{"message"' + ":" + '"connect"}')
		if (response == 1):
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			result = sock.connect_ex((hostname, int(port)))
			if result == 0:
				sock.close()
				distance = 'http://' + hostname + ':' + port
				r = requests.get(distance)
				print(r.content)
				value = r.content.decode('utf-8')	
				resp = '{"message":' + '"connect"}'
				return json.loads(value)
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
	app.run(host = '0.0.0.0', port=3000)
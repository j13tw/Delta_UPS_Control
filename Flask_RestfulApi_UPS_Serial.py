#!/usr/bin/python3.6
from flask import Flask
from flask_restful import Resource, Api
from flask import render_template
from decimal import getcontext, Decimal

import serial, time

app = Flask(__name__)
api = Api(app)

serialName = ''
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
batteryRemain_Min = ''
batteryRemain_Sec = ''
batteryVolt = 0
batteryTemp = 0
batteryRemain_Percent = 0
lastBattery_Year = 0
lastBattery_Mon = 0
lastBattery_Day = 0
nextBattery_Year = 0
nextBattery_Mon = 0
nextBattery_Day = 0

def connectDevice():
	getcontext().prec = 6
	with serial.Serial('COM8', 2400, timeout=1) as ser:			# select which your protocol & link path on UPS
		if(ser.isOpen()):
			global serialName
			global systemMode
			global inputLine, inputFreq, inputVolt
			global outputLine, outputFreq, outputVolt, outputWatt, outputAmp, outputPercent
			global batteryHealth, batteryStatus, batteryCharge_Mode
			global batteryRemain_Min, batteryRemain_Sec, batteryVolt, batteryTemp, batteryRemain_Percent
			global lastBattery_Year, lastBattery_Mon, lastBattery_Day
			global nextBattery_Year, nextBattery_Mon, nextBattery_Day
			serialName = ser.name
			print('USB 連接位置 : ' + serialName)             	# check which port was really used
			print('-----------------------------------------')
		#	--> STI 輸入資料
			ser.write(b'~00P000STI')                       		# write a UPS RS232 format string
		#	ser.write(bytes(b'~00D0101;600;2190'))   			# Return data format 1 Test
		#	ser.write(bytes('~00D0101;600;2190', 'UTF-8'))		# Return data format 2 Test
			s = ser.read(30)        							# read up to return data 30 bytes (timeout)
		#	print(s)
			countLine = ''
			s = s.decode('ascii')								# decode UPS return string format
		# 	print(s)
			tmp = str(s).split(';')								# split data by ';' on data format
		# 	print (tmp)
			i = 0
			for j in tmp[0]:
		 		if  i >= 7:
		 			countLine += str(j) 
		 		i = i + 1
			i = 0
			inputLine = int(countLine)
			inputFreq = float(tmp[1])/10
			inputVolt = float(tmp[2])/10
			print ('輸入線路 : ' + str(inputLine) + ' 號線路')
			print ('輸入頻率 : ' + str(inputFreq) + ' Hz')
			print ('輸入電壓 : ' + str(inputVolt) + ' V')
			print('-----------------------------------------')
			time.sleep(1)
		#	--> STO
			ser.write(b'~00P000STO')
		#	ser.write(b'~00D0230;600;1;2210;;03169;037')
			s = ser.read(30)
			countMode = ''
			s = s.decode('ascii')
		# 	print(s)
			tmp = str(s).split(';')
		# 	print (tmp)
			i = 0
			for j in tmp[0]:
				if  i >= 7:
					countMode += str(j) 
				i = i + 1
			i = 0
		# 	print(countMode)
			mode = int(countMode)
			systemMode = ''
			if mode == 0:
		 		systemMode = 'Normal'
			if mode == 1:
			 	systemMode = 'Battery'
			if mode == 2:
		 		systemMode = 'Bypass(3phase Reserve Power Path)'
			if mode == 3:
			 	psystemMode = 'Reducing'
			if mode == 4:
		 		systemMode = 'Boosting'
			if mode == 5:
			 	systemMode = 'Manual Bypass'
			if mode == 6:
		 		systemMode = 'Other'
			if mode == 7:
		 		systemMode = 'No output'
			outputFreq = float(tmp[1])/10
			outputLine = int(tmp[2])
			outputVolt = float(tmp[3])/10
			outputWatt = int(tmp[5])
			outputAmp = float(outputWatt/outputVolt)
			outputAmp = Decimal(outputAmp)*1
			outputPercent = int(tmp[6])
			print ('輸出狀態 : '+ systemMode)
			print ('輸出線路 : ' + str(outputLine) + ' 號線路')
			print ('輸出頻率 : ' + str(outputFreq) + ' Hz')
			print ('輸出電壓 : %3.1f V' %outputVolt)
			print ('輸出電流 : %3.3f A' %outputAmp)
			print ('輸出瓦特 : ' + str(outputWatt/1000) + ' KW')
			print ('輸出負載比 : ' + str(outputPercent) + ' %')
			print('-----------------------------------------')
			time.sleep(1)
		#	--> STB 輸入資料
			ser.write(b'~00P000STB')
		#	ser.write(b'~00D0250;0;1;;;000;2720;;031;100')
			s = ser.read(40)
			batteryCount = ''
			s = s.decode('ascii')
		#	print(s)
			tmp = str(s).split(';')
		#	print (tmp)
			i = 0
			for j in tmp[0]:
				if  i >= 7:
					batteryCount += str(j) 
				i = i + 1
			i = 0
			if batteryCount == '0':
				batteryHealth = 'Good (良好)'
			if batteryCount == '1':
				batteryHealth = 'Weak (虛弱)'
			if batteryCount == '2':
				batteryHealth = 'Replace (需更換)'
			batteryCount = tmp[1]
			if batteryCount == '0':
				batteryStatus = 'OK (良好)'
			if batteryCount == '1':
				batteryStatus = 'Low (低電量)'
			if batteryCount == '2':
				batteryStatus = 'Depleted (耗盡)'
			batteryCount = tmp[1]
			if batteryCount == '0':
				batteryCharge_Mode = 'Floating charging (微量充電)'
			if batteryCount == '1':
				batteryCharge_Mode = 'Boost charging (快速充電)'
			if batteryCount == '2':
				batteryCharge_Mode = 'Resting (休眠)'
			if batteryCount == '3':
				batteryCharge_Mode = 'Discharging (未充電)'
			if tmp[3] != '':
				batteryRemain_Sec = tmp[3] + ' sec(秒)'
			else:
				batteryRemain_Sec = 'None By Charging (充電中)'
			if tmp[4] != '':
				batteryRemain_Min = tmp[4] + ' min(分)'
			else:
				batteryRemain_Min = 'None By Charging (充電中)'
			batteryVolt = float(tmp[6])/10
			batteryVolt = Decimal(batteryVolt)*1
			batteryTemp = int(tmp[8])
			batteryRemain_Percent = int(tmp[9])
			print ('電池健康度 : ' + batteryHealth)
			print ('電池狀態 : ' + batteryStatus)
			print ('充電模式 : ' + batteryCharge_Mode)
			print ('電池電壓 : %3.1f V' %batteryVolt)
			print ('輸出剩餘時間(分) : ' + batteryRemain_Min)
			print ('輸出剩餘時間(秒) : ' + batteryRemain_Sec)
			print ('電量剩餘百分比 : ' + str(batteryRemain_Percent) + ' %')
			print ('UPS 內部溫度 : ' + str(batteryTemp) + ' °C')
			print('-----------------------------------------')
			time.sleep(1)
		# 	--> BRD
			ser.write(b'~00P000BRD')
		#	ser.write(b'~00D01720170322;20200322')
			s = ser.read(30)
			countLastDate = ''
			s = s.decode('ascii')
		#	print(s)
			tmp = str(s).split(';')
		#	print (tmp)
			i = 0
			for j in tmp[0]:
		 		if  i >= 7:
		 			countLastDate += str(j) 
		 		i = i + 1
			i = 0
			lasteDate = int(countLastDate)
			lastBattery_Year = int(lasteDate/10000)
			lastBattery_Mon = int(lasteDate/100) - lastBattery_Year*100
			lastBattery_Day = lasteDate - lastBattery_Mon*100 - lastBattery_Year*10000
			nextDate = int(tmp[1])
			nextBattery_Year = int(nextDate/10000)
			nextBattery_Mon = int(nextDate/100) - nextBattery_Year*100
			nextBattery_Day = nextDate - nextBattery_Mon*100 - nextBattery_Year*10000
			print ('電池更換時間 : ' + str(lastBattery_Year) + ' 年 ' + str(lastBattery_Mon) + ' 月 ' + str(lastBattery_Day) + ' 日')
			print ('下次更換時間 : ' + str(nextBattery_Year) + ' 年 ' + str(nextBattery_Mon) + ' 月 ' + str(nextBattery_Day) + ' 日')
			ser.close()             # close port
			time.sleep(1)
		else:
			print('Port Open Error!')
class jsonReturn(Resource):
 	def get(self):
 		connectDevice()
 		global serialName, systemMode
 		global inputLine, inputFreq, inputVolt
 		global outputLine, outputFreq, outputVolt, outputWatt, outputAmp, outputPercent
 		global batteryHealth, batteryStatus, batteryCharge_Mode
 		global batteryRemain_Min, batteryRemain_Sec, batteryVolt, batteryTemp, batteryRemain_Percent
 		global lastBattery_Year, lastBattery_Mon, lastBattery_Day
 		global nextBattery_Year, nextBattery_Mon, nextBattery_Day
 		return { 'connect' : serialName, \
 		         'input' : [{ 'inputLine' : str(inputLine), 'inputFreq' : str(inputFreq), 'inputVolt' : str(inputVolt) }], \
 		         'output' : [{ 'systemMode' : systemMode, 'outputLine' : str(outputLine), 'outputFreq' : str(outputFreq), 'outputVolt' : str(outputVolt), 'outputAmp' : str(outputAmp), 'outputWatt' : str(outputWatt), 'outputPercent' : str(outputPercent)}], \
 		         'battery' : [{ 'status' : [{ 'batteryHealth' : batteryHealth, 'batteryStatus' : batteryStatus, 'batteryCharge_Mode' : batteryCharge_Mode, 'batteryRemain_Min' : batteryRemain_Min, 'batteryRemain_Sec' : batteryRemain_Sec, 'batteryVolt' : str(batteryVolt), 'batteryTemp' : str(batteryTemp), 'batteryRemain_Percent' : str(batteryRemain_Percent)}]}, \
 		         { 'lastBattery_Year' : str(lastBattery_Year), 'lastBattery_Mon' : str(lastBattery_Mon), 'lastBattery_Day' : str(lastBattery_Day)}, { 'nextBattery_Year' : str(nextBattery_Year), 'nextBattery_Mon' : str(nextBattery_Mon), 'nextBattery_Day' : str(nextBattery_Day)}]}		
api.add_resource(jsonReturn, '/')
 
@app.route('/show')
def dashBoard():
	global serialName, systemMode
	global inputLine, inputFreq, inputVolt
	global outputLine, outputFreq, outputVolt, outputWatt, outputAmp, outputPercent
	global batteryHealth, batteryStatus, batteryCharge_Mode
	global batteryRemain_Min, batteryRemain_Sec, batteryVolt, batteryTemp, batteryRemain_Percent
	global lastBattery_Year, lastBattery_Mon, lastBattery_Day
	global nextBattery_Year, nextBattery_Mon, nextBattery_Day
	connectDevice()
	return render_template('mainBoard.html', \
		 		serName = serialName, \
		 		inputVolt = inputVolt, \
		 		inputFreq = inputFreq, \
		 		inputLine = inputLine, \
		 		systemMode = str(systemMode), \
				outputLine = outputLine, \
				outputVolt = outputVolt, \
				outputAmp = Decimal(outputAmp)*1, \
		 		outputPercent = outputPercent, \
		 		outputWatt = outputWatt/1000, \
		 		outputFreq = outputFreq, \
		 		batteryHealth = batteryHealth, \
		 		batteryStatus = batteryStatus, \
		 		batteryCharge_Mode = batteryCharge_Mode, \
		 		batteryRemain_Min = batteryRemain_Min, \
		 		batteryRemain_Sec = batteryRemain_Sec, \
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

if __name__ == '__main__':
#	app.run(debug = True)
	app.run(host = '0.0.0.0')

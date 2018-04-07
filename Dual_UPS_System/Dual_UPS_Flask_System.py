#!/usr/bin/python3.6
import serial, time
from flask import Flask
from flask_restful import Resource, Api
from flask import render_template
from decimal import getcontext, Decimal
from serial import SerialException

app = Flask(__name__)
api = Api(app)

UPS_Life_A = ''
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
UPS_Life_B = ''
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

def connectDevice():
	global serialName_A, systemMode_A, UPS_Life_A
	global inputLine_A, inputFreq_A, inputVolt_A
	global outputLine_A, outputFreq_A, outputVolt_A, outputWatt_A, outputAmp_A, outputPercent_A
	global batteryHealth_A, batteryStatus_A, batteryCharge_Mode_A
	global batteryRemain_Min_A, batteryRemain_Sec_A, batteryVolt_A, batteryTemp_A, batteryRemain_Percent_A
	global lastBattery_Year_A, lastBattery_Mon_A, lastBattery_Day_A
	global nextBattery_Year_A, nextBattery_Mon_A, nextBattery_Day_A
	global serialName_B, systemMode_B, UPS_Life_B
	global inputLine_B, inputFreq_B, inputVolt_B
	global outputLine_B, outputFreq_B, outputVolt_B, outputWatt_B, outputAmp_B, outputPercent_B
	global batteryHealth_B, batteryStatus_B, batteryCharge_Mode_B
	global batteryRemain_Min_B, batteryRemain_Sec_B, batteryVolt_B, batteryTemp_B, batteryRemain_Percent_B
	global lastBattery_Year_B, lastBattery_Mon_B, lastBattery_Day_B
	global nextBattery_Year_B, nextBattery_Mon_B, nextBattery_Day_B
	getcontext().prec = 6
	portAcess_A = False
	try:
		ser = serial.Serial('/dev/ttyUSB0', 2400, timeout=1)
		portAcess_A = True
		UPS_Life_A = 'onLine(在線)'
	except:
		print ("USB Port A Open Error !")
		portAcess_A = False	
		UPS_Life_A = 'offLine(離線)'
	if(portAcess_A):
		serialName_A = ser.name + " (左)"
		print('-----------------------------------------')
		print('USB 連接位置 : ' + serialName_A)             	# check which port was really used
		print('-----------------------------------------')
	#	--> STI 輸入資料
	#	ser.write(b'~00P000STI')                       		# write a UPS RS232 format string
		ser.write(b'~00D0101;600;2190')   			# Return data format 1 Test
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
		inputLine_A = int(countLine)
		inputFreq_A = float(tmp[1])/10
		inputVolt_A = float(tmp[2])/10
		print ('輸入線路 : ' + str(inputLine_A) + ' 號線路')
		print ('輸入頻率 : ' + str(inputFreq_A) + ' Hz')
		print ('輸入電壓 : ' + str(inputVolt_A) + ' V')
		print('-----------------------------------------')
		time.sleep(1)
	#	--> STO
	#	ser.write(b'~00P000STO')
		ser.write(b'~00D0230;600;1;2210;;03169;037')
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
		systemMode_A = ''
		if mode == 0:
	 		systemMode_A = 'Normal'
		if mode == 1:
		 	systemMode_A = 'Battery'
		if mode == 2:
	 		systemMode_A = 'Bypass(3phase Reserve Power Path)'
		if mode == 3:
		 	psystemMode_A = 'Reducing'
		if mode == 4:
	 		systemMode_A = 'Boosting'
		if mode == 5:
		 	systemMode_A = 'Manual Bypass'
		if mode == 6:
	 		systemMode_A = 'Other'
		if mode == 7:
	 		systemMode_A = 'No output'
		outputFreq_A = float(tmp[1])/10
		outputLine_A = int(tmp[2])
		outputVolt_A = float(tmp[3])/10
		outputWatt_A = int(tmp[5])
		outputAmp_A = float(outputWatt_A/outputVolt_A)
		outputAmp_A = Decimal(outputAmp_A)*1
		outputPercent_A = int(tmp[6])
		print ('輸出狀態 : '+ systemMode_A)
		print ('輸出線路 : ' + str(outputLine_A) + ' 號線路')
		print ('輸出頻率 : ' + str(outputFreq_A) + ' Hz')
		print ('輸出電壓 : %3.1f V' %outputVolt_A)
		print ('輸出電流 : %3.3f A' %outputAmp_A)
		print ('輸出瓦特 : ' + str(outputWatt_A/1000) + ' KW')
		print ('輸出負載比 : ' + str(outputPercent_A) + ' %')
		print('-----------------------------------------')
		time.sleep(1)
	#	--> STB 輸入資料
	#	ser.write(b'~00P000STB')
		ser.write(b'~00D0250;0;1;;;000;2720;;031;100')
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
			batteryHealth_A = 'Good (良好)'
		if batteryCount == '1':
			batteryHealth_A = 'Weak (虛弱)'
		if batteryCount == '2':
			batteryHealth_A = 'Replace (需更換)'
		batteryCount = tmp[1]
		if batteryCount == '0':
			batteryStatus_A = 'OK (良好)'
		if batteryCount == '1':
			batteryStatus_A = 'Low (低電量)'
		if batteryCount == '2':
			batteryStatus_A = 'Depleted (耗盡)'
		batteryCount = tmp[2]
		if batteryCount == '0':
			batteryCharge_Mode_A = 'Floating charging (微量充電)'
		if batteryCount == '1':
			batteryCharge_Mode_A = 'Boost charging (快速充電)'
		if batteryCount == '2':
			batteryCharge_Mode_A = 'Resting (休眠)'
		if batteryCount == '3':
			batteryCharge_Mode_A = 'Discharging (未充電)'
		if tmp[3] != '':
			batteryRemain_Sec_A = tmp[3] + ' sec(秒)'
		else:
			batteryRemain_Sec_A = 'None By Charging (充電中)'
		if tmp[4] != '':
			batteryRemain_Min_A = tmp[4] + ' min(分)'
		else:
			batteryRemain_Min_A = 'None By Charging (充電中)'
		batteryVolt_A = float(tmp[6])/10
		batteryVolt_A = Decimal(batteryVolt_A)*1
		batteryTemp_A = int(tmp[8])
		batteryRemain_Percent_A = int(tmp[9])
		print ('電池健康度 : ' + batteryHealth_A)
		print ('電池狀態 : ' + batteryStatus_A)
		print ('充電模式 : ' + batteryCharge_Mode_A)
		print ('電池電壓 : %3.1f V' %batteryVolt_A)
		print ('輸出剩餘時間(分) : ' + batteryRemain_Min_A)
		print ('輸出剩餘時間(秒) : ' + batteryRemain_Sec_A)
		print ('電量剩餘百分比 : ' + str(batteryRemain_Percent_A) + ' %')
		print ('UPS 內部溫度 : ' + str(batteryTemp_A) + ' °C')
		print('-----------------------------------------')
		time.sleep(1)
	# 	--> BRD
	#	ser.write(b'~00P000BRD')
		ser.write(b'~00D01720170322;20200322')
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
		lastBattery_Year_A = int(lasteDate/10000)
		lastBattery_Mon_A = int(lasteDate/100) - lastBattery_Year_A*100
		lastBattery_Day_A = lasteDate - lastBattery_Mon_A*100 - lastBattery_Year_A*10000
		nextDate = int(tmp[1])
		nextBattery_Year_A = int(nextDate/10000)
		nextBattery_Mon_A = int(nextDate/100) - nextBattery_Year_A*100
		nextBattery_Day_A = nextDate - nextBattery_Mon_A*100 - nextBattery_Year_A*10000
		print ('電池更換時間 : ' + str(lastBattery_Year_A) + ' 年 ' + str(lastBattery_Mon_A) + ' 月 ' + str(lastBattery_Day_A) + ' 日')
		print ('下次更換時間 : ' + str(nextBattery_Year_A) + ' 年 ' + str(nextBattery_Mon_A) + ' 月 ' + str(nextBattery_Day_A) + ' 日')
		print('-----------------------------------------')
		ser.close()             # close port
		time.sleep(1)

	portAcess_B = False
	try:
        ser = serial.Serial('/dev/ttyUSB1', 2400, timeout=1)                    # select which your p$
        portAcess_B = True
        UPS_Life_B = 'onLine(在線)'
	except:
        portAcess_B = False
        UPS_Life_B = 'offLine(離線)'
	if(portAcess_B):
		serialName_B = ser.name+ " (右)"
		print('USB 連接位置 : ' + serialName_B)             	# check which port was really used
		print('-----------------------------------------')
	#	--> STI 輸入資料
	#	ser.write(b'~00P000STI')                       		# write a UPS RS232 format string
		ser.write(bytes(b'~00D0101;600;2190'))   			# Return data format 1 Test
	#	ser.write(bytes('~00D0101;600;2190', 'UTF-8'))		# Return data format 2 Test
		s = ser.read(30)        							# read up to return data 30 bytes (timeout)
		countLine = ''
		s = s.decode('ascii')								# decode UPS return string format
	#	print(s)
		tmp = str(s).split(';')								# split data by ';' on data format
	# 	print (tmp)
		i = 0
		for j in tmp[0]:
	 		if  i >= 7:
	 			countLine += str(j) 
	 		i = i + 1
		i = 0
		inputLine_B = int(countLine)
		inputFreq_B = float(tmp[1])/10
		inputVolt_B = float(tmp[2])/10
		print ('輸入線路 : ' + str(inputLine_B) + ' 號線路')
		print ('輸入頻率 : ' + str(inputFreq_B) + ' Hz')
		print ('輸入電壓 : ' + str(inputVolt_B) + ' V')
		print('-----------------------------------------')
		time.sleep(1)
	#	--> STO
	#	ser.write(b'~00P000STO')
		ser.write(b'~00D0230;600;1;2210;;03169;037')
		s = ser.read(30)
		countMode = ''
		s = s.decode('ascii')
	#	print(s)
		tmp = str(s).split(';')
	# 	print (tmp)
		i = 0
		for j in tmp[0]:
			if  i >= 7:
				countMode += str(j) 
			i = i + 1
		i = 0
	#	print(countMode)
		mode = int(countMode)
		systemMode_B = ''
		if mode == 0:
	 		systemMode_B = 'Normal'
		if mode == 1:
		 	systemMode_B = 'Battery'
		if mode == 2:
	 		systemMode_B = 'Bypass(3phase Reserve Power Path)'
		if mode == 3:
		 	psystemMode_B = 'Reducing'
		if mode == 4:
	 		systemMode_B = 'Boosting'
		if mode == 5:
		 	systemMode_B = 'Manual Bypass'
		if mode == 6:
	 		systemMode_B = 'Other'
		if mode == 7:
	 		systemMode_B = 'No output'
		outputFreq_B = float(tmp[1])/10
		outputLine_B = int(tmp[2])
		outputVolt_B = float(tmp[3])/10
		outputWatt_B = int(tmp[5])
		outputAmp_B = float(outputWatt_B/outputVolt_B)
		outputAmp_B = Decimal(outputAmp_B)*1
		outputPercent_B = int(tmp[6])
		print ('輸出狀態 : '+ systemMode_B)
		print ('輸出線路 : ' + str(outputLine_B) + ' 號線路')
		print ('輸出頻率 : ' + str(outputFreq_B) + ' Hz')
		print ('輸出電壓 : %3.1f V' %outputVolt_B)
		print ('輸出電流 : %3.3f A' %outputAmp_B)
		print ('輸出瓦特 : ' + str(outputWatt_B/1000) + ' KW')
		print ('輸出負載比 : ' + str(outputPercent_B) + ' %')
		print('-----------------------------------------')
		time.sleep(1)
	#	--> STB 輸入資料
	#	ser.write(b'~00P000STB')
		ser.write(b'~00D0250;0;1;;;000;2720;;031;100')
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
			batteryHealth_B = 'Good (良好)'
		if batteryCount == '1':
			batteryHealth_B = 'Weak (虛弱)'
		if batteryCount == '2':
			batteryHealth_B = 'Replace (需更換)'
		batteryCount = tmp[1]
		if batteryCount == '0':
			batteryStatus_B = 'OK (良好)'
		if batteryCount == '1':
			batteryStatus_B = 'Low (低電量)'
		if batteryCount == '2':
			batteryStatus_B = 'Depleted (耗盡)'
		batteryCount = tmp[2]
		if batteryCount == '0':
			batteryCharge_Mode_B = 'Floating charging (微量充電)'
		if batteryCount == '1':
			batteryCharge_Mode_B = 'Boost charging (快速充電)'
		if batteryCount == '2':
			batteryCharge_Mode_B = 'Resting (休眠)'
		if batteryCount == '3':
			batteryCharge_Mode_B = 'Discharging (未充電)'
		if tmp[3] != '':
			batteryRemain_Sec_B = tmp[3] + ' sec(秒)'
		else:
			batteryRemain_Sec_B = 'None By Charging (充電中)'
		if tmp[4] != '':
			batteryRemain_Min_B = tmp[4] + ' min(分)'
		else:
			batteryRemain_Min_B = 'None By Charging (充電中)'
		batteryVolt_B = float(tmp[6])/10
		batteryVolt_B = Decimal(batteryVolt_B)*1
		batteryTemp_B = int(tmp[8])
		batteryRemain_Percent_B = int(tmp[9])
		print ('電池健康度 : ' + batteryHealth_B)
		print ('電池狀態 : ' + batteryStatus_B)
		print ('充電模式 : ' + batteryCharge_Mode_B)
		print ('電池電壓 : %3.1f V' %batteryVolt_B)
		print ('輸出剩餘時間(分) : ' + batteryRemain_Min_B)
		print ('輸出剩餘時間(秒) : ' + batteryRemain_Sec_B)
		print ('電量剩餘百分比 : ' + str(batteryRemain_Percent_B) + ' %')
		print ('UPS 內部溫度 : ' + str(batteryTemp_B) + ' °C')
		print('-----------------------------------------')
		time.sleep(1)
	# 	--> BRD
	#	ser.write(b'~00P000BRD')
		ser.write(b'~00D01720170322;20200322')
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
		lastBattery_Year_B = int(lasteDate/10000)
		lastBattery_Mon_B = int(lasteDate/100) - lastBattery_Year_B*100
		lastBattery_Day_B = lasteDate - lastBattery_Mon_B*100 - lastBattery_Year_B*10000
		nextDate = int(tmp[1])
		nextBattery_Year_B = int(nextDate/10000)
		nextBattery_Mon_B = int(nextDate/100) - nextBattery_Year_B*100
		nextBattery_Day_B = nextDate - nextBattery_Mon_B*100 - nextBattery_Year_B*10000
		print ('電池更換時間 : ' + str(lastBattery_Year_B) + ' 年 ' + str(lastBattery_Mon_B) + ' 月 ' + str(lastBattery_Day_B) + ' 日')
		print ('下次更換時間 : ' + str(nextBattery_Year_B) + ' 年 ' + str(nextBattery_Mon_B) + ' 月 ' + str(nextBattery_Day_B) + ' 日')
		ser.close()             # close port
		time.sleep(1)
class jsonReturn(Resource):
 	def get(self):
 		connectDevice()
 		global serialName_A, systemMode_A, UPS_Life_A
 		global inputLine_A, inputFreq_A, inputVolt_A
 		global outputLine_A, outputFreq_A, outputVolt_A, outputWatt_A, outputAmp_A, outputPercent_A
 		global batteryHealth_A, batteryStatus_A, batteryCharge_Mode_A
 		global batteryRemain_Min_A, batteryRemain_Sec_A, batteryVolt_A, batteryTemp_A, batteryRemain_Percent_A
 		global lastBattery_Year_A, lastBattery_Mon_A, lastBattery_Day_A
 		global nextBattery_Year_A, nextBattery_Mon_A, nextBattery_Day_A
 		global serialName_B, systemMode_B, UPS_Life_B
 		global inputLine_B, inputFreq_B, inputVolt_B
 		global outputLine_B, outputFreq_B, outputVolt_B, outputWatt_B, outputAmp_B, outputPercent_B
 		global batteryHealth_B, batteryStatus_B, batteryCharge_Mode_B
 		global batteryRemain_Min_B, batteryRemain_Sec_B, batteryVolt_B, batteryTemp_B, batteryRemain_Percent_B
 		global lastBattery_Year_B, lastBattery_Mon_B, lastBattery_Day_B
 		global nextBattery_Year_B, nextBattery_Mon_B, nextBattery_Day_B
 		return { 'connect_A' : serialName_A, 'connect_B' : serialName_B, 'ups_Life_A' : UPS_Life_A, 'ups_Life_B' : UPS_Life_B, \
 		         'input_A' : [{ 'inputLine_A' : str(inputLine_A), 'inputFreq_A' : str(inputFreq_A), 'inputVolt_A' : str(inputVolt_A) }], \
 		         'input_B' : [{ 'inputLine_B' : str(inputLine_B), 'inputFreq_B' : str(inputFreq_B), 'inputVolt_B' : str(inputVolt_B) }], \
 		         'output_A' : [{ 'systemMode_A' : systemMode_A, 'outputLine_A' : str(outputLine_A), 'outputFreq_A' : str(outputFreq_A), 'outputVolt_A' : str(outputVolt_A), 'outputAmp_A' : str(outputAmp_A), 'outputWatt_A' : str(outputWatt_A/1000), 'outputPercent_A' : str(outputPercent_A)}], \
 		         'output_B' : [{ 'systemMode_B' : systemMode_B, 'outputLine_B' : str(outputLine_B), 'outputFreq_B' : str(outputFreq_B), 'outputVolt_B' : str(outputVolt_B), 'outputAmp_B' : str(outputAmp_B), 'outputWatt_B' : str(outputWatt_B/1000), 'outputPercent_B' : str(outputPercent_B)}], \
 		         'battery_A' : [{ 'status' : [{ 'batteryHealth_A' : batteryHealth_A, 'batteryStatus_A' : batteryStatus_A, 'batteryCharge_Mode_A' : batteryCharge_Mode_A, 'batteryRemain_Min_A' : batteryRemain_Min_A, 'batteryRemain_Sec_A' : batteryRemain_Sec_A, 'batteryVolt_A' : str(batteryVolt_A), 'batteryTemp_A' : str(batteryTemp_A), 'batteryRemain_Percent_A' : str(batteryRemain_Percent_A)}]}, \
 		         { 'lastBattery_Year_A' : str(lastBattery_Year_A), 'lastBattery_Mon_A' : str(lastBattery_Mon_A), 'lastBattery_Day_A' : str(lastBattery_Day_A)}, { 'nextBattery_Year_A' : str(nextBattery_Year_A), 'nextBattery_Mon_A' : str(nextBattery_Mon_A), 'nextBattery_Day_A' : str(nextBattery_Day_A)}], \
 		         'battery_B' : [{ 'status' : [{ 'batteryHealth_B' : batteryHealth_B, 'batteryStatus_B' : batteryStatus_B, 'batteryCharge_Mode_B' : batteryCharge_Mode_B, 'batteryRemain_Min_B' : batteryRemain_Min_B, 'batteryRemain_Sec_B' : batteryRemain_Sec_B, 'batteryVolt_B' : str(batteryVolt_B), 'batteryTemp_B' : str(batteryTemp_B), 'batteryRemain_Percent_B' : str(batteryRemain_Percent_B)}]}, \
 		         { 'lastBattery_Year_B' : str(lastBattery_Year_B), 'lastBattery_Mon_B' : str(lastBattery_Mon_B), 'lastBattery_Day_B' : str(lastBattery_Day_B)}, { 'nextBattery_Year_B' : str(nextBattery_Year_B), 'nextBattery_Mon_B' : str(nextBattery_Mon_B), 'nextBattery_Day_B' : str(nextBattery_Day_B)}]}		
api.add_resource(jsonReturn, '/')
 
@app.route('/show')
def dashBoard():
	global serialName_A, systemMode_A, UPS_Life_A
	global inputLine_A, inputFreq_A, inputVolt_A
	global outputLine_A, outputFreq_A, outputVolt_A, outputWatt_A, outputAmp_A, outputPercent_A
	global batteryHealth_A, batteryStatus_A, batteryCharge_Mode_A
	global batteryRemain_Min_A, batteryRemain_Sec_A, batteryVolt_A, batteryTemp_A, batteryRemain_Percent_A
	global lastBattery_Year_A, lastBattery_Mon_A, lastBattery_Day_A
	global nextBattery_Year_A, nextBattery_Mon_A, nextBattery_Day_A
	global serialName_B, systemMode_B, UPS_Life_B
	global inputLine_B, inputFreq_B, inputVolt_B
	global outputLine_B, outputFreq_B, outputVolt_B, outputWatt_B, outputAmp_B, outputPercent_B
	global batteryHealth_B, batteryStatus_B, batteryCharge_Mode_B
	global batteryRemain_Min_B, batteryRemain_Sec_B, batteryVolt_B, batteryTemp_B, batteryRemain_Percent_B
	global lastBattery_Year_B, lastBattery_Mon_B, lastBattery_Day_B
	global nextBattery_Year_B, nextBattery_Mon_B, nextBattery_Day_B
	connectDevice()
	return render_template('mainBoard.html', \
		 		serName_A = serialName_A, \
		 		ups_Life_A = UPS_Life_A, \
		 		inputVolt_A = inputVolt_A, \
		 		inputFreq_A = inputFreq_A, \
		 		inputLine_A = inputLine_A, \
		 		systemMode_A = str(systemMode_A), \
				outputLine_A = outputLine_A, \
				outputVolt_A = outputVolt_A, \
				outputAmp_A = Decimal(outputAmp_A)*1, \
		 		outputPercent_A = outputPercent_A, \
		 		outputWatt_A = outputWatt_A/1000, \
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
		 		ups_Life_B = UPS_Life_B, \
				inputVolt_B = inputVolt_B, \
				inputFreq_B = inputFreq_B, \
				inputLine_B = inputLine_B, \
				systemMode_B = str(systemMode_B), \
				outputLine_B = outputLine_B, \
				outputVolt_B = outputVolt_B, \
				outputAmp_B = Decimal(outputAmp_B)*1, \
				outputPercent_B = outputPercent_B, \
				outputWatt_B = outputWatt_B/1000, \
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
	app.run(host = '0.0.0.0', port=3000, debug = True)

from decimal import getcontext, Decimal

import serial, time

getcontext().prec = 6
with serial.Serial('COM3', 2400, timeout=1) as ser:			# select which your protocol & link path on UPS
	while(ser.isOpen()):
		print("USB 連接位置 : " + ser.name)             	# check which port was really used
		print("-----------------------------------------")
	#	--> STI 輸入資料
		ser.write(b"~00P000STI")                       		# write a UPS RS232 format string
	#	ser.write(bytes(b'~00D0101;600;2190')   			# Return data format 1 Test
	# 	ser.write(bytes('~00D0101;600;2190', 'UTF-8'))		# Return data format 2 Test
		s = ser.read(30)        							# read up to return data 30 bytes (timeout)
	# 	print(s)
		countLine = ""
		s = s.decode('ascii')								# decode UPS return string format
	# 	print(s)
		tmp = str(s).split(';')								# split data by ";" on data format
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
		print ("輸入線路 : " + str(inputLine) + " 號線路")
		print ("輸入頻率 : " + str(inputFreq) + " Hz")
		print ("輸入電壓 : " + str(inputVolt) + " V")
		print("-----------------------------------------")
		time.sleep(1)
	#	--> STO
		ser.write(b"~00P000STO")
	# 	ser.write(b'~00D0230;600;1;2210;;03169;037')
		s = ser.read(30)
		countMode = ""
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
		systemMode = ""
		if mode == 0:
			systemMode = "Normal"
		if mode == 1:
			systemMode = "Battery"
		if mode == 2:
			systemMode = "Bypass(3phase Reserve Power Path)"
		if mode == 3:
	 		psystemMode = "Reducing"
		if mode == 4:
			systemMode = "Boosting"
		if mode == 5:
	 		systemMode = "Manual Bypass"
		if mode == 6:
			systemMode = "Other"
		if mode == 7:
			systemMode = "No output"
		outputFreq = float(tmp[1])/10
		outputLine = int(tmp[2])
		outputVolt = float(tmp[3])/10
		outputWatt = int(tmp[5])
		outputAmp = float(outputWatt/outputVolt)
		outputPersent = int(tmp[6])
		print ("輸出狀態 : "+ systemMode)
		print ("輸出線路 : " + str(outputLine) + " 號線路")
		print ("輸出頻率 : " + str(outputFreq) + " Hz")
		print ("輸出電壓 : " + str(outputVolt) + " V")
		print ("輸出電流 : %3.3f A" %outputAmp)
		print ("輸出瓦特 : " + str(outputWatt/1000) + " KW")
		print ("輸出負載比 : " + str(outputPersent) + " %")
		print("-----------------------------------------")
		time.sleep(1)
	# 	--> BRD
		ser.write(b"~00P000BRD")
	# 	ser.write(b'~00D01720170322;20200322')
		s = ser.read(30)
		countLastDate = ""
		s = s.decode('ascii')
	# 	print(s)
		tmp = str(s).split(';')
	# 	print (tmp)
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
		print ("電池更換時間 : " + str(lastBattery_Year) + " 年 " + str(lastBattery_Mon) + " 月 " + str(lastBattery_Day) + " 日")
		print ("下次更換時間 : " + str(nextBattery_Year) + " 年 " + str(nextBattery_Mon) + " 月 " + str(nextBattery_Day) + " 日")
		ser.close()             # close port

from flask import Flask
from flask import render_template
from decimal import getcontext, Decimal

import serial

app = Flask(__name__)
@app.route("/")

def connectDevice():
	getcontext().prec = 6
	with serial.Serial('COM9', 2400, timeout=1) as ser:
		while(ser.isOpen()):
		 	print("USB 連接位置 : " + ser.name)         # check which port was really used
		 	print("-----------------------------------------")
		#	--> STI 輸入資料
		 	ser.write(b"~00P000STI")     # write a string
		# 	ser.write(bytes('~00D0101;600;2190', 'UTF-8'))
		 	s = ser.read(30)        # read up to ten bytes (timeout)
		# 	print(s)
		 	countLine = ""
		 	s = s.decode('ascii')
		# 	print(s)
		 	tmp = str(s).split(';')
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
		 	ser.close()             # close port
		 	ser.open()
		#	--> STO
		# 	ser.write(b'~00D0230;600;1;2210;;03169;037')
		 	ser.write(b'~00P000STO')
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
		 	mode = int(countMode)
		 	if mode == 0:
		 		print("輸出模式 : Normal")
		 	if mode == 1:
			 	print("輸出模式 : Battery")
		 	if mode == 2:
		 		print("輸出模式 : Bypass(3phase Reserve Power Path)")
		 	if mode == 3:
			 	print("輸出模式 : Reducing")
		 	if mode == 4:
		 		print("輸出模式 : Boosting")
		 	if mode == 5:
			 	print("輸出模式 : Manual Bypass")
		 	if mode == 6:
		 		print("輸出模式 : Other")
		 	if mode == 7:
			 	print("輸出模式 : No output") 	
		 	outputFreq = float(tmp[1])/10
		 	outputLine = int(tmp[2])
		 	outputVolt = float(tmp[3])/10
		 	outputWatt = int(tmp[5])
		 	outputAmp = float(outputWatt/outputVolt)
		 	outputPersent = int(tmp[6])
		 	print ("輸出線路 : " + str(outputLine) + " 號線路")
		 	print ("輸出頻率 : " + str(outputFreq) + " Hz")
		 	print ("輸出電壓 : " + str(outputVolt) + " V")
		 	print ("輸出電流 : %3.3f A" %outputAmp)
		 	print ("輸出瓦特 : " + str(outputWatt/1000) + " KW")
		 	print ("輸出負載比 : " + str(outputPersent) + " %")
		 	print("-----------------------------------------")
		 	ser.close()             # close port
		 	ser.open()
		 	return render_template('mainBoard.html', \
		 		SerName = str(ser.name), \
		 		InputVolt = inputVolt, \
		 		InputFreq = inputFreq, \
		 		InputLine = inputLine, \
				OutputLine = outputLine, \
				OutputVolt = outputVolt, \
				OutputAmp = Decimal(outputAmp)*1, \
		 		OutputPersent = outputPersent, \
		 		OutputWatt = outputWatt/1000, \
		 		OutputFreq = outputFreq)
if __name__ == "__main__":
	app.run(host="0.0.0.0")

import sys
from decimal import getcontext, Decimal
import serial, time
import paho.mqtt.client as mqtt
import json

if (not(len(sys.argv) == 2 and str(sys.argv[1]).lower() in ['a', 'b'])):
    print("python argv error")
    exit()
    

broker_ip = "10.20.0.19"
broker_port = 1883

while(True):
    try:
        client = mqtt.Client()
        client.connect(broker_ip, broker_port)
        break
    except:
        print("mqtt error")
        time.sleep(1)

alertTopic = "UPS/" + str(sys.argv[1]).upper() + "/Alert"
monitorTopic = "UPS/" + str(sys.argv[1]).upper() + "/Monitor"

def checkSerail():
    global ser
    sendScan = 0
    while (sendScan == 0):
        try:
            ser = serial.Serial('/dev/ttyUSB0', 2400, timeout=1)
            sendScan = 1
        except:
            print("usb open fail")
            time.sleep(10)

checkSerail()

while(True): 
    dataCount = 0
    sendScan = 0
    sendData = {
        "input": {}, 
        "output": {}, 
        "battery": {
            "status": {},
            "lastChange": {},
            "nextChange": {}
        }
    }

    if str(sys.argv[1]).lower() == 'a': serName = ser.name + " (牆壁)"
    if str(sys.argv[1]).lower() == 'b': serName = ser.name + " (窗戶)"
    print("USB 連接位置 : " + serName)       # check which port was really used
    print("-----------------------------------------")
    # --> STI 輸入資料
    try:
        ser.write(b"~00P000STI")
        # Uart Data Respone Sample                     		# write a UPS RS232 format string
        # ser.write(bytes(b'~00D0101;600;2190'))   			# Return data format 1 Test
        # ser.write(bytes('~00D0101;600;2190', 'UTF-8'))	# Return data format 2 Test
        s = ser.read(30)        							# read up to return data 30 bytes (timeout)
        # print(s)
        s = s.decode('ascii')[7:]							# decode UPS return string format
        # print(s)
        tmp = s.split(';')								    # split data by ";" on data format
        # print (tmp)
        inputLine = int(tmp[0])
        inputFreq = float(tmp[1])/10
        inputVolt = float(tmp[2])/10
        print ("電源相位 : " + str(inputLine) + " 相線路")
        print ("輸入頻率 : " + str(inputFreq) + " Hz")
        print ("輸入電壓 : " + str(inputVolt) + " V")
        print("-----------------------------------------")
        dataCount += 1
        # time.sleep(1)
    except:
        checkSerail()

    # --> STO 輸出資料
    try:
        ser.write(b"~00P000STO")
        # Uart Data Respone Sample
        # ser.write(b'~00D0230;600;1;2210;;03169;037')
        s = ser.read(30)
        s = s.decode('ascii')[7:]
        # print(s)
        tmp = s.split(';')
        # print (tmp)
        if int(tmp[0]) == 0: outputMode = "Normal (市電輸入)"
        elif int(tmp[0]) == 1: outputMode = "Battery (電池轉換)"
        elif int(tmp[0]) == 2: outputMode = "Bypass(3phase Reserve Power Path)"
        elif int(tmp[0]) == 3: poutputMode = "Reducing"
        elif int(tmp[0]) == 4: outputMode = "Boosting"
        elif int(tmp[0]) == 5: outputMode = "Manual Bypass (手動屏蔽)"
        elif int(tmp[0]) == 6: outputMode = "Other (其他)"
        elif int(tmp[0]) == 7: outputMode = "No output (無輸出)"
        outputFreq = float(tmp[1])/10
        outputLine = int(tmp[2])
        outputVolt = float(tmp[3])/10
        outputWatt = round(int(tmp[5])/1000, 3)
        outputAmp = round(float(outputWatt*1000/outputVolt), 3)
        outputPercent = int(tmp[6])
        print ("輸出狀態 : "+ outputMode)
        print ("輸出線路 : " + str(outputLine) + " 相線路")
        print ("輸出頻率 : " + str(outputFreq) + " Hz")
        print ("輸出電壓 : " + str(outputVolt) + " V")
        print ("輸出電流 : " + str(outputAmp) + " A")
        print ("輸出瓦特 : " + str(outputWatt) + " KW")
        print ("輸出負載比 : " + str(outputPercent) + " %")
        print("-----------------------------------------")
        dataCount += 1
        # time.sleep(1)
    except:
        checkSerail()

    # --> STB 輸入資料
    try:
        ser.write(b'~00P000STB')
        # Uart Data Respone Sample
        # ser.write(b'~00D0250;0;1;;;000;2720;;031;100')
        s = ser.read(40)
        batteryCount = ''
        s = s.decode('ascii')[7:]
        # print(s)
        tmp = str(s).split(';')
        # print (tmp)
        if tmp[0] == '0': batteryHealth = 'Good (良好)'
        if tmp[0] == '1': batteryHealth = 'Weak (虛弱)'
        if tmp[0] == '2': batteryHealth = 'Replace (需更換)'
        if tmp[1] == '0': batteryStatus = 'OK (良好)'
        if tmp[1] == '1': batteryStatus = 'Low (低電量)'
        if tmp[1] == '2': batteryStatus = 'Depleted (耗盡)'
        if tmp[2] == '0': batteryChargeMode = 'Floating charging (微量充電)'
        if tmp[2] == '1': batteryChargeMode = 'Boost charging (快速充電)'
        if tmp[2] == '2': batteryChargeMode = 'Resting (休眠)'
        if tmp[2] == '3': batteryChargeMode = 'Discharging (未充電)'
        batteryVolt = round(float(tmp[6])/10, 1)
        innerTemp = int(tmp[8])
        batteryRemainPercent = int(tmp[9])
        print ('電池健康度 : ' + batteryHealth)
        print ('電池狀態 : ' + batteryStatus)
        print ('充電模式 : ' + batteryChargeMode)
        print ('電池電壓 : ' + str(batteryVolt) + ' V' )
        print ('電量剩餘百分比 : ' + str(batteryRemainPercent) + ' %')
        print ('UPS 內部溫度 : ' + str(batteryTemp) + ' °C')
        print("-----------------------------------------")
        dataCount += 1
        # time.sleep(1)
    except:
        checkSerail()

    # --> BRD
    try:
        ser.write(b"~00P000BRD")
        # Uart Data Respone Sample
        # ser.write(b'~00D01720170322;20200322')
        s = ser.read(30)
        countLastDate = ""
        s = s.decode('ascii')[7:]
        # print(s)
        tmp = str(s).split(';')
        # print (tmp)
        lastBattery_Year = int(tmp[0][0:4])
        lastBattery_Mon = int(tmp[0][4:6])
        lastBattery_Day = int(tmp[0][6:8])
        nextBattery_Year = int(tmp[1][0:4])
        nextBattery_Mon = int(tmp[1][4:6])
        nextBattery_Day = int(tmp[1][6:8])
        print ("電池更換時間 : " + str(lastBattery_Year) + " 年 " + str(lastBattery_Mon) + " 月 " + str(lastBattery_Day) + " 日")
        print ("下次更換時間 : " + str(nextBattery_Year) + " 年 " + str(nextBattery_Mon) + " 月 " + str(nextBattery_Day) + " 日")
        print("-----------------------------------------")
        dataCount += 1
        # time.sleep(1)
    except:
        checkSerail()

    if (dataCount == 3):
        sendData["input"]["line"] = inputLine
        sendData["input"]["freq"] = inputFreq
        sendData["input"]["volt"] = inputVolt
        sendData["output"]["mode"] = outputMode
        sendData["output"]["line"] = outputLine
        sendData["output"]["freq"] = outputFreq
        sendData["output"]["volt"] = outputVolt
        sendData["output"]["amp"] = outputAmp
        sendData["output"]["percent"] = outputPercent
        sendData["output"]["watt"] = outputWatt
        sendData["battery"]["status"]["health"] = batteryHealth
        sendData["battery"]["status"]["status"] = batteryStatus
        sendData["battery"]["status"]["chargeMode"] = batteryChargeMode
        sendData["battery"]["status"]["volt"] = batteryVolt
        sendData["temp"] = innerTemp
        sendData["battery"]["status"]["remainPercent"] = batteryRemainPercent
        sendData["battery"]["lastChange"]["year"] = lastBattery_Year
        sendData["battery"]["lastChange"]["month"] = lastBattery_Mon
        sendData["battery"]["lastChange"]["day"] = lastBattery_Day
        sendData["battery"]["nextChange"]["year"] = nextBattery_Year
        sendData["battery"]["nextChange"]["month"] = nextBattery_Mon
        sendData["battery"]["nextChange"]["day"] = nextBattery_Day
        print(json.dumps(sendData))
        try:
            client.publish(monitorTopic, json.dumps(sendData))
        except:
            pass

    time.sleep(1)
        
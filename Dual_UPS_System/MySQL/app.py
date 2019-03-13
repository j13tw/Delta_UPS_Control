import MySQLdb
import paho.mqtt.client as mqtt
import datetime
import json

# define Mysql status
mysql_host = "127.0.0.1"
mysql_port = 3306
mysql_db = "factory"
mysql_user = "imac"
mysql_passwd = "imacuser"

# define Mqtt status
mqtt_host = "10.20.0.19"
mqtt_port = 1883

try:
    conn = MySQLdb.connect(host = mysql_host, \
                            port=mysql_port, \
                            user=mysql_user, \
                            passwd=mysql_passwd, 
                            db=mysql_db, \
                            charset="utf8")
    cur = conn.cursor()
except:
    output = 'Database Connect Error !'

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.subscribe("DL303/CO2")
    client.subscribe("DL303/RH")
    client.subscribe("DL303/TC")
    client.subscribe("DL303/DC")
    client.subscribe("ET7044/DOstatus")
    client.subscribe("current")
    client.subscribe("UPS_Monitor")
    client.subscribe("air-conditioner-vent")
    client.subscribe("cabinet_A")
    client.subscribe("cabinet_B")

def on_message(client, userdata, msg):
    topic = msg.topic
    data = msg.payload.decode('utf-8')
    time_stamp = datetime.datetime.now()
    print(time_stamp)
    if topic == "DL303/CO2":
        try:
            # Insert DL-303_CO2 Table
            # print('INSERT INTO DL303_CO2(Time_Stamp, Co2) VALUE ("' + str(time_stamp) + '", ' + str(data) + ');')
            cur.execute('INSERT INTO DL303_CO2 \
                        (Time_Stamp, Co2) \
                        VALUE \
                        ("' + str(time_stamp) + '", ' + str(data) + ');')
        except:
            print("DL303_CO2 ERROR")
    if topic == "DL303/RH":
        try:
            # Insert DL-303_RH Table
            # print('INSERT INTO DL303_RH(Time_Stamp, Humi) VALUE ("' + str(time_stamp) + '", ' + str(data) + ');')
            cur.execute('INSERT INTO DL303_RH \
                        (Time_Stamp, Humi) \
                        VALUE \
                        ("' + str(time_stamp) + '", ' + str(data) + ');')
        except:
            print("DL303_RH ERROR")
    if topic == "DL303/TC":
        try:
            # Insert DL-303_TC Table
            # print('INSERT INTO DL303_TC(Time_Stamp, Temp) VALUE ("' + str(time_stamp) + '", ' + str(data) + ');')
            cur.execute('INSERT INTO DL303_TC \
                        (Time_Stamp, Temp) \
                        VALUE \
                        ("' + str(time_stamp) + '", ' + str(data) + ');')
        except:
            print("DL303_TC ERROR")
    if topic == "DL303/DC":
        try:
            # Insert DL-303_DC Table
            # print('INSERT INTO DL303_DC(Time_Stamp, Dew_Point) VALUE ("' + str(time_stamp) + '", ' + str(data) + ');')
            cur.execute('INSERT INTO DL303_DC \
                        (Time_Stamp, Dew_Point) \
                        VALUE \
                        ("' + str(time_stamp) + '", ' + str(data) + ');')
        except:
            print("DL303_DC ERROR")
    if topic == "ET7044/DOstatus":
        key = json.loads(data)
        try:
            # Insert ET-7044 Table
            # print('INSERT INTO ET7044(Time_Stamp, SW1, SW2, SW3, SW4, SW5, SW6, SW7, SW8) VALUE ("' + str(time_stamp) + '", ' + str(key[0]) + ', ' + str(key[1]) + ', ' + str(key[2]) + ', ' + str(key[3]) + ', ' + str(key[4])  + ', ' + str(key[5]) + ', ' + str(key[6]) + ', ' + str(key[7]) + ');')
            cur.execute('INSERT INTO ET7044 \
                        (Time_Stamp, SW1, SW2, SW3, SW4, SW5, SW6, SW7, SW8) \
                        VALUE \
                        ("' + str(time_stamp) + '", ' + str(key[0]) + ', ' + str(key[1]) + ', ' + str(key[2]) + ', ' + str(key[3]) + ', ' + str(key[4])  + ', ' + str(key[5]) + ', ' + str(key[6]) + ', ' + str(key[7]) + ');')
        except:
            print("ET7044_ERROR")
    if topic == "current":
        key = json.loads(data)
        try:
            # Insert Power-Meter Table
            # print('INSERT INTO Power_Meter(Time_Stamp, Humi, Temp, Current) VALUE ("' + str(time_stamp) + '", ' + str(key['Humidity']) + ', ' + str(key['Temperature']) + ', ' + str(key['currents']) + ');')
            cur.execute('INSERT INTO Power_Meter \
                    (Time_Stamp, Humi, Temp, Current) \
                    VALUE \
                    ("' + str(time_stamp) + '", ' + str(key['Humidity']) + ', ' + str(key['Temperature']) + ', ' + str(key['currents']) + ');')
        except:
            print("Power_Meter_ERROR")
    if topic == "UPS_Monitor":
        key = json.loads(data)
        print (key)
        ups_Life_A = key['ups_Life_A']
        serialName_A = key['connect_A']
        inputStatus_A = key['input_A']
        inputLine_A = inputStatus_A['inputLine_A']
        inputFreq_A = inputStatus_A['inputFreq_A']
        inputVolt_A = inputStatus_A['inputVolt_A']
        outputStatus_A = key['output_A']
        systemMode_A = outputStatus_A['systemMode_A']
        outputLine_A = outputStatus_A['outputLine_A']
        outputFreq_A = outputStatus_A['outputFreq_A']
        outputVolt_A = outputStatus_A['outputVolt_A']
        outputAmp_A = outputStatus_A['outputAmp_A']
        outputWatt_A = outputStatus_A['outputWatt_A']
        outputPercent_A = outputStatus_A['outputPercent_A']
        status_A = key['battery_A']['status']
        batteryHealth_A = status_A['batteryHealth_A']
        batteryStatus_A = status_A['batteryStatus_A']
        batteryCharge_Mode_A = status_A['batteryCharge_Mode_A']
        batteryVolt_A = status_A['batteryVolt_A']
        batteryTemp_A = status_A['batteryTemp_A']
        batteryRemain_Percent_A = status_A['batteryRemain_Percent_A']
        lastBattery_A = key['battery_A']['lastChange']
        nextBattery_A = key['battery_A']['nextChange']
        lastBattery_Year_A = lastBattery_A['lastBattery_Year_A']
        lastBattery_Mon_A = lastBattery_A['lastBattery_Mon_A']
        lastBattery_Day_A = lastBattery_A['lastBattery_Day_A']
        nextBattery_Year_A = nextBattery_A['nextBattery_Year_A']
        nextBattery_Mon_A = nextBattery_A['nextBattery_Mon_A']
        nextBattery_Day_A = nextBattery_A['nextBattery_Day_A']
        # Insert UPS_A Table
        print("INSERT INTO UPS_A Table")
        cur.execute('INSERT INTO UPS_A \
                    (Time_Stamp, Device_Locate, Device_Life, System_Mode, \
                    Input_Line, Input_Freq, Input_Volt, \
                    Output_Line, Output_Freq, Output_Volt, Output_Amp, Output_Watt, Output_Percent, \
                    Battery_Volt, Battery_Remain_Percent, Battery_Health, Battery_Status, Battery_Charge_Mode, Battery_Temp, \
                    Battery_Last_Change_Year, Battery_Last_Change_Mon, Battery_Last_Change_Day, \
                    Battery_Next_Change_Year, Battery_Next_Change_Mon, Battery_Next_Change_Day) \
                    VALUE \
                    ("' + str(time_stamp) + '", "' + str(serialName_A) + '", "' + str(ups_Life_A) + '", "' + str(systemMode_A) + '", ' + \
                    str(inputLine_A) + ', ' + str(inputFreq_A) + ', ' + str(inputVolt_A) + ', ' + \
                    str(outputLine_A) + ', ' + str(outputFreq_A) + ', ' + str(outputVolt_A) + ', ' + str(outputAmp_A) + ', ' + str(outputWatt_A) + ', ' + str(outputPercent_A) + ', ' + \
                    str(batteryVolt_A) + ', ' + str(batteryRemain_Percent_A) + ', "' + str(batteryHealth_A) + '", "' + str(batteryStatus_A) + '", "' + str(batteryCharge_Mode_A) + '", ' + str(batteryTemp_A) + ', ' +\
                    str(lastBattery_Year_A) + ', ' + str(lastBattery_Mon_A) + ', ' + str(lastBattery_Day_A) + ', ' + \
                    str(nextBattery_Year_A) + ', ' + str(nextBattery_Mon_A) + ', ' + str(nextBattery_Day_A) + ');')
        ups_Life_B = key['ups_Life_B']
        serialName_B = key['connect_B']
        status_B = key['battery_B']['status']
        batteryHealth_B = status_B['batteryHealth_B']
        batteryStatus_B = status_B['batteryStatus_B']
        batteryCharge_Mode_B = status_B['batteryCharge_Mode_B']
        batteryRemain_Min_B = status_B['batteryRemain_Min_B']
        batteryRemain_Sec_B = status_B['batteryRemain_Sec_B']
        batteryVolt_B = status_B['batteryVolt_B']
        batteryTemp_B = status_B['batteryTemp_B']
        batteryRemain_Percent_B = status_B['batteryRemain_Percent_B']
        lastBattery_B = key['battery_B']['lastChange']
        nextBattery_B = key['battery_B']['nextChange']
        inputStatus_B = key['input_B']
        outputStatus_B = key['output_B']
        inputLine_B = inputStatus_B['inputLine_B']
        inputFreq_B = inputStatus_B['inputFreq_B']
        inputVolt_B = inputStatus_B['inputVolt_B']
        systemMode_B = outputStatus_B['systemMode_B']
        outputLine_B = outputStatus_B['outputLine_B']
        outputFreq_B = outputStatus_B['outputFreq_B']
        outputVolt_B = outputStatus_B['outputVolt_B']
        outputAmp_B = outputStatus_B['outputAmp_B']
        outputWatt_B = outputStatus_B['outputWatt_B']
        outputPercent_B = outputStatus_B['outputPercent_B']
        lastBattery_Year_B = lastBattery_B['lastBattery_Year_B']
        lastBattery_Mon_B = lastBattery_B['lastBattery_Mon_B']
        lastBattery_Day_B = lastBattery_B['lastBattery_Day_B']
        nextBattery_Year_B = nextBattery_B['nextBattery_Year_B']
        nextBattery_Mon_B = nextBattery_B['nextBattery_Mon_B']
        nextBattery_Day_B = nextBattery_B['nextBattery_Day_B']
        # Insert UPS_A Table
        print("INSERT INTO UPS_A Table")
        cur.execute('INSERT INTO UPS_A \
                    (Time_Stamp, Device_Locate, Device_Life, System_Mode, \
                    Input_Line, Input_Freq, Input_Volt, \
                    Output_Line, Output_Freq, Output_Volt, Output_Amp, Output_Watt, Output_Percent, \
                    Battery_Volt, Battery_Remain_Percent, Battery_Health, Battery_Status, Battery_Charge_Mode, Battery_Temp, \
                    Battery_Last_Change_Year, Battery_Last_Change_Mon, Battery_Last_Change_Day, \
                    Battery_Next_Change_Year, Battery_Next_Change_Mon, Battery_Next_Change_Day) \
                    VALUE \
                    ("' + str(time_stamp) + '", "' + str(serialName_B) + '", "' + str(ups_Life_B) + '", "' + str(systemMode_B) + '", ' + \
                    str(inputLine_B) + ', ' + str(inputFreq_B) + ', ' + str(inputVolt_B) + ', ' + \
                    str(outputLine_B) + ', ' + str(outputFreq_B) + ', ' + str(outputVolt_B) + ', ' + str(outputAmp_B) + ', ' + str(outputWatt_B) + ', ' + str(outputPercent_B) + ', ' + \
                    str(batteryVolt_B) + ', ' + str(batteryRemain_Percent_B) + ', "' + str(batteryHealth_B) + '", "' + str(batteryStatus_B) + '", "' + str(batteryCharge_Mode_B) + '", ' + str(batteryTemp_B) + ', ' +\
                    str(lastBattery_Year_B) + ', ' + str(lastBattery_Mon_B) + ', ' + str(lastBattery_Day_B) + ', ' + \
                    str(nextBattery_Year_B) + ', ' + str(nextBattery_Mon_B) + ', ' + str(nextBattery_Day_B) + ');')
    if topic == "air-conditioner-vent":
        key = json.loads(data)
        try:
            # Insert Air_Coundiction Table
            # print('INSERT INTO Air_Condiction(Time_Stamp, Humi, Temp) VALUE ("' + str(time_stamp) + '", ' + str(key['Humi']) + ', ' + str(key[Temp]) + ');')
            cur.execute('INSERT INTO Air_Condiction \
                        (Time_Stamp, Humi, Temp) \
                        VALUE \
                        ("' + str(time_stamp) + '", ' + str(key['Humi']) + ', ' + str(key[Temp]) + ');')
        except:
            print("Air_Condiction_ERROR")
    if topic == "cabinet_A":
        key = json.loads(data)
        try:
            # Insert Power_Box_A Table
            # print('INSERT INTO Power_Box_A(Time_Stamp, In_A, In_B, Out_A, Out_B, Out_C, Out_D, Out_E) VALUE ("' + str(time_stamp) + '", ' + str(key['IN_V110_A']) + ', ' + str(key['IN_V110_B']) + ', ' + str(key['OUT_V110_A']) + ', ' + str(key['OUT_V110_B']) + ', ' + str(key['OUT_V110_C']) + ', ' + str(key['OUT_V110_D']) + ', ' + str(key['OUT_V110_E']) + ');')
            cur.execute('INSERT INTO Power_Box_A \
                        (Time_Stamp, In_A, In_B, Out_A, Out_B, Out_C, Out_D, Out_E) \
                        VALUE \
                        ("' + str(time_stamp) + '", ' + str(key['IN_V110_A']) + ', ' + str(key['IN_V110_B']) + ', ' + str(key['OUT_V110_A']) + ', ' + str(key['OUT_V110_B']) + ', ' + str(key['OUT_V110_C']) + ', ' + str(key['OUT_V110_D']) + ', ' + str(key['OUT_V110_E']) + ');')
        except:
            print("Power_Box_A_ERROR")
    if topic == "cabinet_B":
        key = json.loads(data)
        try:
            # Insert Power_Box_B Table
            # print('INSERT INTO Power_Box_B(Time_Stamp, In_A, In_B, Out_A, Out_B, Out_C, Out_D, Out_E) VALUE ("' + str(time_stamp) + '", ' + str(key['IN_V110_A']) + ', ' + str(key['IN_V110_B']) + ', ' + str(key['OUT_V110_A']) + ', ' + str(key['OUT_V110_B']) + ', ' + str(key['OUT_V110_C']) + ', ' + str(key['OUT_V110_D']) + ', ' + str(key['OUT_V110_E']) + ');')
            cur.execute('INSERT INTO Power_Box_B \
                        (Time_Stamp, In_A, In_B, Out_A, Out_B, Out_C, Out_D, Out_E) \
                        VALUE \
                        ("' + str(time_stamp) + '", ' + str(key['IN_V110_A']) + ', ' + str(key['IN_V110_B']) + ', ' + str(key['OUT_V110_A']) + ', ' + str(key['OUT_V110_B']) + ', ' + str(key['OUT_V110_C']) + ', ' + str(key['OUT_V110_D']) + ', ' + str(key['OUT_V110_E']) + ');')
        except:
            print("Power_Box_B_ERROR")
#    print(data)
    conn.commit()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(mqtt_host, mqtt_port)
client.loop_forever()
import MySQLdb
import paho.mqtt.client as mqtt
import datetime

# define Mysql status
mysql_host = "127.0.0.1"
mysql_port = 3306
mysql_db = "factory"
mysql_user = "imac"
mysql_passwd = "imacuser"

time_stamp = datetime.datetime.now()

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

try:
    # Insert Power-Meter Table
    cur.execute('INSERT INTO Power_Meter \
                (Time_Stamp, Humi, Temp, Current) \
                VALUE \
                ("' + str(time_stamp) + '", 11.5, 20.3, 12.5);')
    conn.commit()
    print("INSERT INTO Power-Meter Table")
except:
    print("Power-Meter Table ERROR")

try:
    # Insert DL-303_TC Table
    cur.execute('INSERT INTO DL303 \
                (Time_Stamp, Temp) \
                VALUE \
                ("' + str(time_stamp) + '", 29.3);')
    conn.commit()
    print("INSERT INTO DL303_TC Table")
except:
    print("DL303_TC Table ERROR")

try:
    # Insert DL-303_RH Table
    cur.execute('INSERT INTO DL303_RH \
                (Time_Stamp, Humi) \
                VALUE \
                ("' + str(time_stamp) + '", 75.3);')
    conn.commit()
    print("INSERT INTO DL303_RH Table")
except:
    print("DL303_RH Table ERROR")

try:
    # Insert DL-303_DC Table
    cur.execute('INSERT INTO DL303_DC \
                (Time_Stamp, Dew_Point) \
                VALUE \
                ("' + str(time_stamp) + '", 10.3);')
    conn.commit()
    print("INSERT INTO DL303_DC Table")
except:
    print("DL303_DC Table ERROR")

try:
    # Insert DL-303_CO2 Table
    cur.execute('INSERT INTO DL303 \
                (Time_Stamp, Co2) \
                VALUE \
                ("2018-03-11", 500);')
    conn.commit()
    print("INSERT INTO DL303_CO2 Table")
except:
    print("DL303_CO2 Table ERROR")

try:
    # Insert ET-7044 Table
    cur.execute('INSERT INTO ET7044 \
                (Time_Stamp, SW1, SW2, SW3, SW4, SW5, SW6, SW7, SW8) \
                VALUE \
                ("2018-03-11", False, False, False, False, True, False, False, False);')
    conn.commit()
    print("INSERT INTO ET-7044 Table")
except:
    print("ET-7044 Table ERROR")

try:
    # Insert Air_Coundiction Table
    cur.execute('INSERT INTO Air_Condiction \
                (Time_Stamp, Humi, Temp) \
                VALUE \
                ("2018-03-11", 11.5, 20.3);')
    conn.commit()
    print("INSERT INTO Air_Condiction Table")
except:
    print("Air_Condiction Table ERROR")

try:
    # Insert Power_Box_A Table
    cur.execute('INSERT INTO Power_Box_A \
                (Time_Stamp, In_A, In_B, Out_A, Out_B, Out_C, Out_D, Out_E) \
                VALUE \
                ("2018-03-11", 11.2, 10.3, 16.5, 20.3, 15.5, 20.5, 13.5);')
    conn.commit()
    print("INSERT INTO Power_Box_A Table")
except:
    print("Power_Box_A Table ERROR")

try:
    # Insert Power_Box_B Table
    cur.execute('INSERT INTO Power_Box_B \
                (Time_Stamp, In_A, In_B, Out_A, Out_B, Out_C, Out_D, Out_E) \
                VALUE \
                ("2018-03-11", 12.2, 11.3, 14.5, 21.3, 15.4, 21.5, 12.5);')
    conn.commit()
    print("INSERT INTO Power_Box_B Table")
except:
    print("Power_Box_B Table ERROR")

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
                    ("2018-03-11", "/dev/ttyUSB0 (牆壁)", "onLine(在線)", "Normal", \
                    1, 59.9, 215,\
                    1, 60.0, 220, 16.2345, 4.567, 45, \
                    271, 100, "Good (良好)", "OK (良好)", "Boost charging (快速充電)", 33, \
                    2017, 03, 25, \
                    2020, 03, 24);')
        # Insert UPS_B Table
        print("INSERT INTO UPS_B Table")
        cur.execute('INSERT INTO UPS_B \
                    (Time_Stamp, Device_Locate, Device_Life, System_Mode, \
                    Input_Line, Input_Freq, Input_Volt, \
                    Output_Line, Output_Freq, Output_Volt, Output_Amp, Output_Watt, Output_Percent, \
                    Battery_Volt, Battery_Remain_Percent, Battery_Health, Battery_Status, Battery_Charge_Mode, Battery_Temp, \
                    Battery_Last_Change_Year, Battery_Last_Change_Mon, Battery_Last_Change_Day, \
                    Battery_Next_Change_Year, Battery_Next_Change_Mon, Battery_Next_Change_Day) \
                    VALUE \
                    ("2018-03-11", "/dev/ttyUSB0 (牆壁)", "onLine(在線)", "Normal", \
                    1, 59.9, 215,\
                    1, 60.0, 220, 16.2345, 4.567, 45, \
                    271, 100, "Good (良好)", "OK (良好)", "Boost charging (快速充電)", 33, \
                    2017, 03, 25, \
                    2020, 03, 24);')
        print("Table INSERT INTO OK !")
        conn.commit()
    except MySQLdb.OperationalError:
        output = 'INSERT INTO Table Error !'
    else:
        cur.close()
'''
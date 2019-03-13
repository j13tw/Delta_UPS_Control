import MySQLdb

# define Mysql status
mysql_host = "127.0.0.1"
mysql_port = 3306
mysql_db = "factory"
mysql_user = "imac"
mysql_passwd = "imacuser"
mysql_error = 0
mysql_output = ""

try:
    conn = MySQLdb.connect(host = mysql_host, \
                            port=mysql_port, \
                            user=mysql_user, \
                            passwd=mysql_passwd, \
                            db=mysql_db, \
                            charset="utf8")
    cur = conn.cursor()
    try:
        # Create Power_Meter Table
        cur.execute('CREATE TABLE Power_Meter (\
                        Count_Log   int AUTO_INCREMENT, \
                        Time_Stamp  datetime NOT NULL, \
                        Humi        float(5, 2) NOT NULL, \
                        Temp        float(5, 2) NOT NULL, \
                        Current     float(5, 2) NOT NULL, \
                        PRIMARY KEY(Count_Log));')
        print("Create Power_Meter Table")
    except:
        print("Create Power_Meter Table Fail !")
    try:
        # Create DL303_CO2 Table
        cur.execute('CREATE TABLE DL303_CO2 (\
                        Count_Log   int AUTO_INCREMENT, \
                        Time_Stamp  datetime NOT NULL, \
                        Co2         float(5, 2) NOT NULL, \
                        PRIMARY KEY(Count_Log));')
        print("Create DL303_CO2 Table")
    except:
        print("Create DL303_CO2 Table Fail !")
    try:
        # Create DL-303_RH Table
        cur.execute('CREATE TABLE DL303_RH (\
                        Count_Log   int AUTO_INCREMENT, \
                        Time_Stamp  datetime NOT NULL, \
                        Humi        float(5, 2) NOT NULL, \
                        PRIMARY KEY(Count_Log));')
        print("Create DL303_RH Table")
    except:
        print("Create DL303_RH Table Fail !")
    try:
        # Create DL303_TC Table
        cur.execute('CREATE TABLE DL303_TC (\
                        Count_Log   int AUTO_INCREMENT, \
                        Time_Stamp  datetime NOT NULL, \
                        Temp        float(5, 2) NOT NULL, \
                        PRIMARY KEY(Count_Log));')
        print("Create DL303_TC Table")
    except:
        print("Create DL303_TC Fail !")
    try:
        # Create DL303_DC Table
        cur.execute('CREATE TABLE DL303_DC (\
                        Count_Log   int AUTO_INCREMENT, \
                        Time_Stamp  datetime NOT NULL, \
                        Dew_Point   float(5, 2) NOT NULL, \
                        PRIMARY KEY(Count_Log));')
        print("Create DL303_DC Table")
    except:
        print("Create DL303_DC Table Fail !")
    try:
        # Create ET7044 Table
        cur.execute('CREATE TABLE ET7044 (\
                        Count_Log   int AUTO_INCREMENT, \
                        Time_Stamp  datetime NOT NULL, \
                        SW1        bool NOT NULL, \
                        SW2        bool NOT NULL, \
                        SW3        bool NOT NULL, \
                        SW4        bool NOT NULL, \
                        SW5        bool NOT NULL, \
                        SW6        bool NOT NULL, \
                        SW7        bool NOT NULL, \
                        SW8        bool NOT NULL, \
                        PRIMARY KEY(Count_Log));')
        print("Create ET7044 Table")
    except:
        print("Create ET7044 Table Fail !")
    try:
        # Create Air_Coundiction Table
        cur.execute('CREATE TABLE Air_Coundiction (\
                        Count_Log   int AUTO_INCREMENT, \
                        Time_Stamp  datetime NOT NULL, \
                        Humi        float(5, 2) NOT NULL, \
                        Temp        float(5, 2) NOT NULL, \
                        PRIMARY KEY(Count_Log));')
        print("Create Air_Condiction Table")
        conn.commit()
    except:
        print("Create Air_Condiction Table Fail !")
    try:
        # Create Power_Box_A Table
        cur.execute('CREATE TABLE Power_Box_A (\
                        Count_Log   int AUTO_INCREMENT, \
                        Time_Stamp  datetime NOT NULL, \
                        In_A        float(5, 2) NOT NULL, \
                        In_B        float(5, 2) NOT NULL, \
                        Out_A       float(5, 2) NOT NULL, \
                        Out_B       float(5, 2) NOT NULL, \
                        Out_C       float(5, 2) NOT NULL, \
                        Out_D       float(5, 2) NOT NULL, \
                        Out_E       float(5, 2) NOT NULL, \
                        PRIMARY KEY(Count_Log));')
        conn.commit()
        print("Create Power_Box_A Table")
    except:
        print("Create Power_Box_A Table Fail !")
    try:
        # Create Power_Box_B Table
        cur.execute('CREATE TABLE Power_Box_B (\
                        Count_Log   int AUTO_INCREMENT, \
                        Time_Stamp  datetime NOT NULL, \
                        In_A        float(5, 2) NOT NULL, \
                        In_B        float(5, 2) NOT NULL, \
                        Out_A       float(5, 2) NOT NULL, \
                        Out_B       float(5, 2) NOT NULL, \
                        Out_C       float(5, 2) NOT NULL, \
                        Out_D       float(5, 2) NOT NULL, \
                        Out_E       float(5, 2) NOT NULL, \
                        PRIMARY KEY(Count_Log));')
        conn.commit()
        print("Create Power_Box_B Table")
    except:
        print("Create Power_Box_A Table Fail !")
    try:
        # Create UPS_A Table
        cur.execute('CREATE TABLE UPS_A (\
                        Count_Log                 int AUTO_INCREMENT, \
                        Time_Stamp                datetime NOT NULL, \
                        Device_Locate             varchar(40) NOT NULL, \
                        Device_Life               varchar(20) NOT NULL, \
                        Input_Line                int NOT NULL, \
                        Input_Volt                float(5, 2) NOT NULL, \
                        Input_Freq                float(5, 2) NOT NULL, \
                        Output_Line               int NOT NULL, \
                        Output_Freq               float(5, 2) NOT NULL, \
                        Output_Volt               float(5, 2) NOT NULL, \
                        Output_Amp                float(6, 4) NOT NULL, \
                        Output_Watt               float(5, 3) NOT NULL, \
                        Output_Percent            int NOT NULL, \
                        System_Mode               varchar(20) NOT NULL, \
                        Battery_Volt              int NOT NULL, \
                        Battery_Remain_Percent    int NOT NULL, \
                        Battery_Health            varchar(20) NOT NULL, \
                        Battery_Status            varchar(20) NOT NULL, \
                        Battery_Charge_Mode       varchar(40) NOT NULL, \
                        Battery_Temp              int NOT NULL, \
                        Battery_Last_Change_Year  int NOT NULL, \
                        Battery_Last_Change_Mon   int NOT NULL, \
                        Battery_Last_Change_Day   int NOT NULL, \
                        Battery_Next_Change_Year  int NOT NULL, \
                        Battery_Next_Change_Mon   int NOT NULL, \
                        Battery_Next_Change_Day   int NOT NULL, \
                        PRIMARY KEY(Count_Log)) \
                        default charset=utf8;')
        print("Create UPS_A Table")
    except:
        print("Create UPS_A Table Fail !")
    try:
        # Create UPS_B Table
        cur.execute('CREATE TABLE UPS_B (\
                        Count_Log                 int AUTO_INCREMENT, \
                        Time_Stamp                datetime NOT NULL, \
                        Device_Locate             varchar(40) NOT NULL, \
                        Device_Life               varchar(20) NOT NULL, \
                        Input_Line                int NOT NULL, \
                        Input_Volt                float(5, 2) NOT NULL, \
                        Input_Freq                float(5, 2) NOT NULL, \
                        Output_Line               int NOT NULL, \
                        Output_Freq               float(5, 2) NOT NULL, \
                        Output_Volt               float(5, 2) NOT NULL, \
                        Output_Amp                float(6, 4) NOT NULL, \
                        Output_Watt               float(5, 3) NOT NULL, \
                        Output_Percent            int NOT NULL, \
                        System_Mode               varchar(20) NOT NULL, \
                        Battery_Volt              int NOT NULL, \
                        Battery_Remain_Percent    int NOT NULL, \
                        Battery_Health            varchar(20) NOT NULL, \
                        Battery_Status            varchar(20) NOT NULL, \
                        Battery_Charge_Mode       varchar(40) NOT NULL, \
                        Battery_Temp              int NOT NULL, \
                        Battery_Last_Change_Year  int NOT NULL, \
                        Battery_Last_Change_Mon   int NOT NULL, \
                        Battery_Last_Change_Day   int NOT NULL, \
                        Battery_Next_Change_Year  int NOT NULL, \
                        Battery_Next_Change_Mon   int NOT NULL, \
                        Battery_Next_Change_Day   int NOT NULL, \
                        PRIMARY KEY(Count_Log)) \
                        default charset=utf8;')
        print("Create UPS_B Table")
    except:
        print("Create UPS_B Table Fail !")
    conn.commit()
    print("Table Create OK !")
    cur.close()
except:
    output = 'Database Connect Fail !'
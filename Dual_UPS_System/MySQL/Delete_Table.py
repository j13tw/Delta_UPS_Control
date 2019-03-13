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
        # Delete Power-Meter Table
        print("Delete Power-Meter Table")
        cur.execute('DROP TABLE Power_Meter;')
    except:
        print("Delete Power-Meter Table Fail !")
    try:
        # Delete DL-303_CO2 Table
        print("Delete DL-303_CO2 Table")
        cur.execute('DROP TABLE DL303_CO2;')
    except:
        print("Delete DL-303_CO2 Table Fail !")
    try:
        # Delete DL-303_RH Table
        print("Delete DL-303_RH Table")
        cur.execute('DROP TABLE DL303_RH;')
    except:
        print("Delete DL-303_RH Table Fail !")
    try:
        # Delete DL-303_TC Table
        print("Delete DL-303_TC Table")
        cur.execute('DROP TABLE DL303_TC;')
    except:
        print("Delete DL-303_TC Table Fail !")
    try:
        # Delete DL-303_DC Table
        print("Delete DL-303_DC Table")
        cur.execute('DROP TABLE DL303_DC;')
    except:
        print("Delete DL-303_DC Table Fail !")
    try:
        # Delete ET-7044 Table
        print("Delete ET-7044 Table")
        cur.execute('DROP TABLE ET7044;')
    except:
        print("Delete ET-7044 Table Fail !")
    try:
        # Delete Air_Coundiction Table
        print("Delete Air_Condiction Table")
        cur.execute('DROP TABLE Air_Coundiction;')
    except:
        print("Delete Air_Condiction Table Fail !")
    try:
        # Delete Power_Box_A Table
        print("Delete Air_Condiction Table")
        cur.execute('DROP TABLE Power_Box_A;')
    except:
        print("Delete Air_Condiction Table Fail !")
    try:
        # Delete Power_Box_B Table
        print("Delete Power_Box_B Table")
        cur.execute('DROP TABLE Power_Box_B;')
    except:
        print("Delete Power_Box_B Table Fail !")
    try:
        # Delete UPS_A Table
        print("Delete UPS_A Table")
        cur.execute('DROP TABLE UPS_A;')
    except:
        print("Delete UPS_A Table Fail !")
    try:
        # Delete UPS_B Table
        print("Delete UPS_B Table")
        cur.execute('DROP TABLE UPS_B;')
    except:
        print("Delete UPS_B Table Fail !")
    conn.commit()
    print("Table Delete OK !")
    cur.close()
except:
    output = 'Database Connect Error !'
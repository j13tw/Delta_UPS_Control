/*
  Web client

  This sketch connects to a website (http://download.labs.mediatek.com)
  using LinkIt 7697

  This example is written for a network using WPA encryption. For
  WEP or WPA, change the Wifi.begin() call accordingly.

  Circuit:
  * LinkIt 7697

  created 13 July 2010
  by dlf (Metodo2 srl)
  modified 31 May 2012
  by Tom Igoe
  modified Jan 2017
  by MediaTek Labs
*/

#include <LWiFi.h>

char ssid[] = "IOT_outdoor";      //  your network SSID (name)
char pass[] = "kiss5891";  // your network password (use for WPA, or use as key for WEP)
int keyIndex = 0;               // your network key Index number (needed only for WEP)

int status = WL_IDLE_STATUS;
// if you don't want to use DNS (and reduce your sketch size)
// use the numeric IP instead of the name for the server:
//IPAddress server(117,185,24,248);
char server[] = "smart-factory-robot.herokuapp.com";   // http://download.labs.mediatek.com/linkit_7697_ascii.txt

// Initialize the Ethernet client library
// with the IP address and port of the server
// that you want to connect to (port 80 is default for HTTP):
WiFiClient client;

int upsAlert = 0;

int userTest = 0;
int upsStatus = 0;
int upsPower = 0;
int upsBackend = 0;
int upsBroken = 0;
int upsSupply = 0;

int upsPreStatus = 0;
int upsPrePower = 0;
int upsPreBackend = 0;
int upsPreBroken = 0;
int upsPreSupply = 0;

int userTestPin = 6;
int upsPin8Pin = 10;
int upsPin1Pin = 11;
int upsPin6Pin = 12;
int upsPin5Pin = 13;
int upsPin2Pin = 16;

String buildJson(int statusCount) {
  String upsStatusString = "";
  String upsPowerString = "";
  String upsBackendString = "";
  String upsBrokenString = "";
  String upsSupplyString = "";
  if (upsStatus == 0) upsStatusString = "異常";
  else upsStatusString = "正常";
  if (upsPower == 0) upsPowerString = "市電";
  else upsPowerString = "電池";
  if (upsBackend == 0) upsBackendString = "足夠";
  else upsBackendString = "告警";
  if (upsBroken == 0) upsBrokenString = "正常";
  else upsBrokenString = "故障";
  if (upsSupply == 0) upsSupplyString = "旁路";
  else upsSupplyString = "轉換";
  String data = "{\"message\":\"能源異常回覆系統";
  if (statusCount == 1) data += "(每月測試)";
  data += "\nUPS設備位置:UPS_A(牆壁)\n運轉狀態: ";
  data += upsStatusString;
  data += "\n供電狀況: ";
  data += upsPowerString;
  data += "\n備載狀態: ";
  data += upsBackendString;
  data += "\n故障狀態: ";
  data += upsBrokenString;
  data += "\n電源淨化: ";
  data += upsSupplyString;
  data += "\"}";
  return data;
}

void userTestAlert(){
  postAlert(1);
}

void postAlert(int statusCount){
  String PostData = buildJson(statusCount);
  Serial.print(PostData);
  // if you get a connection, report back via serial:
    if (client.connect(server, 443)) {
        Serial.println("connected to server (POST)");
        // Make a HTTP request:
        client.println("POST /message HTTP/1.1");
        client.println("Host: smart-factory-robot.herokuapp.com");
        client.println("Content-Type: application/json");
        client.println("Connection: close");
        client.print("Content-Length: ");
        client.println(PostData.length());
        client.println();
        client.println(PostData);  //send the HTTP POST body
        delay(10);
    }
    
    // if there are incoming bytes available
    // from the server, read them and print them:
    while (client.available()) {
        char c = client.read();
        Serial.write(c);
    }

    // if the server's disconnected, stop the client:
    if (!client.connected()) {
        Serial.println();
        Serial.println("disconnecting from server.");
        client.stop();
    }
}

void setup() {
    //Initialize serial and wait for port to open:
    Serial.begin(9600);
    while (!Serial) {
        ; // wait for serial port to connect. Needed for native USB port only
    }

    // attempt to connect to Wifi network:
    while (status != WL_CONNECTED) {
        Serial.print("Attempting to connect to SSID: ");
        Serial.println(ssid);
        // Connect to WPA/WPA2 network. Change this line if using open or WEP network:
        status = WiFi.begin(ssid, pass);
    }
    Serial.println("Connected to wifi");
    printWifiStatus();

    pinMode(userTestPin, INPUT);
    pinMode(upsPin1Pin, INPUT);
    pinMode(upsPin2Pin, INPUT);
    pinMode(upsPin5Pin, INPUT);
    pinMode(upsPin6Pin, INPUT);
    pinMode(upsPin8Pin, INPUT);
    attachInterrupt(userTestPin, userTestAlert, RISING); 
}

void loop() {
    upsAlert = 0;

    int upsPin1 = 0;
    int upsPin2 = 0;
    int upsPin5 = 0;
    int upsPin6 = 0;
    int upsPin8 = 0;
    
    userTest = digitalRead(userTestPin);
    upsPin1 = digitalRead(upsPin1Pin);
    upsPin2 = digitalRead(upsPin2Pin);
    upsPin5 = digitalRead(upsPin5Pin);
    upsPin6 = digitalRead(upsPin6Pin);
    upsPin8 = digitalRead(upsPin8Pin);

    Serial.print(upsPin8);
    Serial.print(upsPin1);
    Serial.print(upsPin6);
    Serial.print(upsPin5);
    Serial.print(upsPin2);
    Serial.println("\n");

    if (upsPin1 == 0 && upsPin6 == 0 && upsPin8 == 0) upsStatus = 1;
    else upsStatus = 0;
    if (upsPin8 == 1) upsPower = 1;
    else upsPower = 0;
    if (upsPin1 == 1) upsBackend = 1;
    else upsBackend = 0;
    if (upsPin6 == 1) upsBroken = 1;
    else upsBroken = 0;
    if (upsPin5 == 1 && upsPin2 == 0) upsSupply = 0;
    if (upsPin5 == 0 && upsPin2 == 1) upsSupply = 1;
    
    if (upsStatus != upsPreStatus) upsAlert |= 1;
    if (upsPower != upsPrePower) upsAlert |= 1;
    if (upsBackend != upsPreBackend) upsAlert |= 1;
    if (upsBroken != upsPreBroken) upsAlert |= 1;
    if (upsSupply != upsPreSupply) upsAlert |= 1;

    if (upsAlert == 1){
      postAlert(0);
    }

    upsPreStatus = upsStatus;
    upsPrePower = upsPower;
    upsPreBackend = upsBackend;
    upsPreBroken = upsBroken;
    upsPreSupply = upsSupply;
//    Serial.println("\n");
//    Serial.print(upsPreStatus);
//    Serial.print(upsStatus);
//    Serial.println("\n");
//    Serial.print(upsPrePower);
//    Serial.print(upsPower);
//    Serial.println("\n");
//    Serial.print(upsPreBackend);
//    Serial.print(upsBackend);
//    Serial.println("\n");
//    Serial.print(upsPreBroken);
//    Serial.print(upsBroken);
//    Serial.println("\n");
//    Serial.print(upsPreSupply);
//    Serial.print(upsSupply);
    Serial.println("\nWait for Scan Status Loop");
    delay(15000);
    
}


void printWifiStatus() {
    // print the SSID of the network you're attached to:
    Serial.print("SSID: ");
    Serial.println(WiFi.SSID());

    // print your WiFi shield's IP address:
    IPAddress ip = WiFi.localIP();
    Serial.print("IP Address: ");
    Serial.println(ip);

    // print the received signal strength:
    long rssi = WiFi.RSSI();
    Serial.print("signal strength (RSSI):");
    Serial.print(rssi);
    Serial.println(" dBm");
}

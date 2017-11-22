#include "ESP8266lib.h"

String server = "www.example.com";
String wifiName = "";
String wifiPassword = "";
ESP8266 esp(2, 3);

int sensorPin = A0;

void setup() 
{
  setupESPasAccessPoint();
}

void loop() 
{
 int reading = analogRead(A0);
 esp.sendDataPacket(server, String(reading), 5002);
}

void setupESPasAccessPoint()
{
 esp.resetDefaultAccessPoint();
 esp.changeESPWifiMode(3);
 esp.changeESPConnectionMode(1);
 esp.connectToNetwork(wifiName, wifiPassword);
}

String getHTMLdataAsString(int reading)
{
  String webpage = "HTTP/1.1 200 OK\r\n";
  webpage += "Content-Type: text/html\r\n\r\n";
  webpage += "<!DOCTYPE HTML>\r\n<html>\r\n";
  webpage += "<h1>Sensor Reading: " + String(reading) + "</h1>\r\n";
  webpage += "</html>";
  return webpage;
}


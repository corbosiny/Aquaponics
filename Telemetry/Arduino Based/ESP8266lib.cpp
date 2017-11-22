#include "ESP8266lib.h"
#include <SoftwareSerial.h>

ESP8266::ESP8266(int rxPin = 2, int txPin = 3, long int baudRate = 9600)
{
  SoftwareSerial newSerialLine(rxPin, txPin);
  newSerialLine.begin(baudRate);
  this->serialLine = &newSerialLine;
}


String ESP8266::getResponseFromESP(int delayTime = 0)
{
  String response;
  while(serialLine->available())
  {
    response += serialLine->read();
    delay(delayTime);
  }
  response;
}

void ESP8266::serialDump()
{
 getResponseFromESP(.2); 
}

boolean ESP8266::checkIfMessageSentCorrectly(String response)
{
  return response.indexOf("OK") != -1; 
}


String ESP8266::sendCommand(String command)
{
  command = "AT+" + command;
  serialLine->println(command);
  return getResponseFromESP();
}


String ESP8266::getFirmwareVersion()
{
  String response = sendCommand("GMR");
  return response;
}

boolean ESP8266::resetESP()
{
  String response = sendCommand("RST");
  return checkIfMessageSentCorrectly(response);
}

boolean ESP8266::changeESPWifiMode(int newMode)
{
  String command = "CWMODE=" + String(newMode);
  String response = sendCommand(command);
  return checkIfMessageSentCorrectly(response);
}


String ESP8266::getESPWifiMode()
{
 String response = sendCommand("CWMODE?");
 return response; 
}


boolean ESP8266::changeESPConnectionMode(int newMode)
{
  String response = sendCommand("CIPMUX=" + String(newMode));
  return checkIfMessageSentCorrectly(response);
}

boolean ESP8266::setServerMode(int serverMode, int port)
{
  String response = sendCommand("CIPSERVER=" + String(serverMode) + "," + String(port));
  return checkIfMessageSentCorrectly(response);
}

String ESP8266::getBaudRate()
{
  String response = sendCommand("CIOBAUD");
  return response;
}

String ESP8266::scanAccessPoints()
{
  String response = sendCommand("CWLAP");
  return response;
}

boolean ESP8266::resetDefaultAccessPoint()
{
  String response = sendCommand("CWQAP");
  return checkIfMessageSentCorrectly(response);
}

boolean ESP8266::connectToNetwork(String networkName, String password)
{
  String command = "CWJAP=\"" + networkName + "\",\"" + password + "\"";
  String response = sendCommand(command);
  return checkIfMessageSentCorrectly(response);
}

String ESP8266::getIPaddress()
{
  String ipAddr = sendCommand("CIFSR"); 
  return ipAddr;
}

boolean ESP8266::sendDataPacket(String server, String dataToSend, int port= 80)
{
  sendCommand("CIPSTART=\"TCP\",\"" + server + "\",\"80\"");
  sendCommand("CIPSEND=" + String(dataToSend.length()));
  serialLine->println(dataToSend);
  String response = sendCommand("CIPCLOSE");
  return checkIfMessageSentCorrectly(response);
}

boolean ESP8266::sendDataPacketUDP(String server, String dataToSend, int port= 80)
{
  sendCommand("CIPSTART=\"UDP\",\"" + server + "\",\"80\"");
  sendCommand("CIPSEND=" + String(dataToSend.length()));
  serialLine->println(dataToSend);
  String response = sendCommand("CIPCLOSE");
  return checkIfMessageSentCorrectly(response);
}

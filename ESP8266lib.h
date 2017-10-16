
#ifndef ESP8266lib_h
#define ESP8266lib_h

#include "Arduino.h"
#include <SoftwareSerial.h>

class ESP8266
{
  
  public:
  ESP8266(int rxPin = 2, int txPin = 3, long int baudRate = 9600);

  void serialDump();
  boolean resetESP();

  String sendCommand(String command);
  String getResponseFromESP(int delayTime = 0);

  String getFirmwareVersion();
  String getBaudRate();
  
  String scanAccessPoints();
  boolean resetDefaultAccessPoint();
  
  boolean changeESPWifiMode(int newMode);
  String getESPWifiMode();
  boolean changeESPConnectionMode(int newMode);
  boolean setServerMode(int serverMode, int port);
  
  boolean connectToNetwork(String networkName, String password);
  String getIPaddress();
  
  boolean sendDataPacket(String server, String dataToSend);
  boolean sendDataPacketUDP(String server, String dataToSend);  

  private:
  SoftwareSerial *serialLine; 
  
  boolean checkIfMessageSentCorrectly(String response);
  
};


#endif

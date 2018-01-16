#ifndef PHsensor_h
#define PHsensor_h

#include "Arduino.h"

class PHsensor
{

  public:
  static const int NUM_READINGS = 10;
  static const int DELAY_BETWEEN_READINGS = 2;
  
  PHsensor(int sensorPin, float offset = .23);

  float getPH();
  
  private:
  int sensorPin;
  int lastTenReadings[10];
  float offset;
  
  int getSensorReading();
  float averageReadings();
  
  float convertReadingToVolts(float reading);
  float convertVoltsToPH(float voltage);
  
};

#endif

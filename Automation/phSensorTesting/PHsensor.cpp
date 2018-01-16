#include "PHsensor.h"

PHsensor::PHsensor(int sensorPin, float offset)
{
  this->sensorPin = sensorPin;
  this->offset = offset;
}

float PHsensor::getPH()
{
  for(int readingNum = 0; readingNum < NUM_READINGS; readingNum++)
  {
    lastTenReadings[readingNum] = getSensorReading();
    delay(DELAY_BETWEEN_READINGS);
  }

  float averageReading = averageReadings();
  float voltage = convertReadingToVolts(averageReading);
  float phReading = convertVoltsToPH(voltage);
  return phReading;
}

int PHsensor::getSensorReading()
{
  return analogRead(sensorPin);
}

float PHsensor::averageReadings()
{
  float total = 0;
  for(int i = 0; i < NUM_READINGS; i++)
  {
    total += lastTenReadings[i];
  }
  float average = total / NUM_READINGS;
  return average;
}


float PHsensor::convertReadingToVolts(float averageReading)
{
  return averageReading * 5.0 / 1024;
}


float PHsensor::convertVoltsToPH(float voltageReading)
{
  return 3.5 * voltageReading - offset;
}


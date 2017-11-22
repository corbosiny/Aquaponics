#include "System.h";

#define NUM_SYSTEMS 1

float heaterThresholds[] = {10, 40};
int heaterRelayPin = 5;
float getHeaterReading();
System heater(heaterThresholds, heaterRelayPin, &(getHeaterReading));


float(*sensorFunctions[])(void) = {&(getHeaterReading)};
System systems[] = {heater};

#define E_STOP_PIN 2
#define E_STOP_LED 3

void setup() 
{
  pinMode(E_STOP_LED, OUTPUT);
  digitalWrite(E_STOP_LED, LOW);
  attachInterrupt(E_STOP_PIN, eStopInterrupt, RISING);
}

void loop() 
{
  updateSystemStatuses();
}



void updateSystemStatuses()
{
  for(int systemNum = 0; systemNum < NUM_SYSTEMS; systemNum++)
  {
    systems[systemNum].controlSystem();
  }
}

void eStopInterrupt()
{
  for(int systemNum = 0; systemNum < NUM_SYSTEMS; systemNum++)
  {
    systems[systemNum].controlRelay(LOW);
  }
  digitalWrite(E_STOP_LED, HIGH);
  while(digitalRead(E_STOP_PIN) == HIGH)
  {
    ;
  }
  digitalWrite(E_STOP_LED, LOW);
}

float getHeaterReading()
{
  return 2.0;
}



#include "System.h";

#include <OneWire.h>
#include <DallasTemperature.h>

#define NUM_SYSTEMS 2
#define ONE_WIRE_BUS 2

float heaterThresholds[] = {10, 40};
int heaterRelayPin = 5;
OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature tempSensor(&oneWire);
float getHeaterReading();
System heater(heaterThresholds, heaterRelayPin, &(getHeaterReading));

float waterHeightThresholds[] = {10, 65};
float pumpRelayPin = 6;
int ultraSonicPins[] = {6,7};
float getWaterLevel();
System pump(waterHeightThresholds, pumpRelayPin, &(getWaterLevel));

System systems[] = {heater, pump};

#define E_STOP_PIN 2
#define E_STOP_LED 3

void setup() 
{
  pinMode(E_STOP_LED, OUTPUT);
  digitalWrite(E_STOP_LED, LOW);
  attachInterrupt(E_STOP_PIN, eStopInterrupt, RISING);

  tempSensor.begin();

  pinMode(ultraSonicPins[0], OUTPUT); 
  pinMode(ultraSonicPins[1], INPUT);
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
  tempSensor.requestTemperatures();
  return tempSensor.getTempCByIndex(0);
}


float tankHeight = 50;
float getWaterLevel()
{
  int reading = getReading();
  float distanceToWater = reading*0.034/2; //converting time for wave to bounce back into centimeters
  if(distanceToWater == 0) {distanceToWater = 15;}
  float waterHeight = tankHeight - distanceToWater;
  return waterHeight;
}

int getReading()  //pin 0 sends out an ultra sonic pulse, pin 1 then times how long it takes to come back
{
  digitalWrite(ultraSonicPins[0], LOW);
  delayMicroseconds(2);
  digitalWrite(ultraSonicPins[0], HIGH);
  delayMicroseconds(10);
  digitalWrite(ultraSonicPins[0], LOW);
  return pulseIn(ultraSonicPins[1], HIGH);
}


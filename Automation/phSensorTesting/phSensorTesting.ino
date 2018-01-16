#include "PHsensor.h"

float offset = 0;
int sensorPin = 0;
PHsensor sensor(sensorPin, offset);

void setup() 
{
  Serial.begin(9600);
  Serial.println("Setup");
}

void loop() 
{
  while(true)
  {
    Serial.println(sensor.getPH());
    delay(500);
  }
}

#include "PHsensor.h"

float offset = .25;
int sensorPin = 0;
PHsensor sensor(sensorPin, offset);

void setup() 
{

}

void loop() 
{
  while(true)
  {
    Serial.println(sensor.getPH());
    delay(500);
  }
}

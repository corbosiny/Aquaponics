#include "System.h"

System::System(float thresholds[], int relayPin, float(*getSensorReading)(void))
{
  memcpy(this->thresholds, thresholds, sizeof(thresholds));
  this->relayPin = relayPin;
  if(relayPin >= 0) {pinMode(relayPin, OUTPUT);}
}

void System::controlSystem()
{
  float reading = getSensorReading();
  lastReading = reading;

  if(relayPin == -1) {return;}
  
  if(reading > thresholds[1])
  {
    controlRelay(LOW);
  }
  else if(reading < thresholds[0])
  {
    controlRelay(HIGH);
  }
}

void System::controlRelay(bool state)
{
  digitalWrite(relayPin, state);
}


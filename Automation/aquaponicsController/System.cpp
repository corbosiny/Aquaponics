#include "System.h"

System::System(float thresholds[], int relayPin, float(*getSensorReading)(void))
{
  memcpy(this->thresholds, thresholds, sizeof(thresholds));
  this->relayPin = relayPin;
}

void System::controlSystem()
{
  float reading = getSensorReading();
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


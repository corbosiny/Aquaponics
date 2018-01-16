#ifndef System_h
#define System_h

#include "Arduino.h"

class System
{

  public:
    System(float thresholds[], int relayPin, float(*getSensorReading)(void));

    void controlSystem();
    void controlRelay(bool state);
    
    float lastReading;
    
  private:
    float thresholds[2];
    int relayPin;
    float(*getSensorReading)(void);
    
};


#endif

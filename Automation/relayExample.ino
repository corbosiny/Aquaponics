//code is written for any arduino board
//code uses water temperature sensor to turn on and off heater
//heater uses a relay to turn it on or off
//we have our power wire connected to the normally closed pin on the relay

int relaySignalPin = 10;
int waterSensorPin = A0;

int upperTemperatureLimit = 100;
int lowerTemperatureLimit = 70;

void setup() 
{
  pinMode(relaySignalPin, OUTPUT);
  digitalWrite(relaySignalPin, LOW);
}

void loop() 
{
  int temperatureReading = getTemperatureReading();
  controlTemperature(temperatureReading);
}

int getTemperatureReading()
{
  return analogRead(waterSensorPin);  //just reads the analog pin, later this will include math to turn the reading into degrees celcius
}

void controlTemperature(int temperatureReading)
{
  if(temperatureReading < lowerTemperatureLimit)
  {
    digitalWrite(relaySignalPin, HIGH); //turning on the heater if our temp is too low
  }
  else if(temperatureReading > upperTemperatureLimit)
  {
    digitalWrite(relaySignalPin, LOW); //turning off the heater if our temp is too high
  }
}



#include <Wire.h>

void setup() {
  Serial.begin (115200);
  Serial.println ();
  Serial.println ("I2C scanner. Scanning ...");
  byte count = 0;
  

  for (byte i = 1; i < 255; i++)
  {
    Wire.begin (i);
    Wire.onReceive(receiveEvent);
    Serial.print (i, DEC);
    Serial.println (" tested");
    delay (100);  // give devices time to recover
  } // end of for loop
  Serial.println ("Done.");
}  // end of setup

void loop() {}

void receiveEvent(int howMany)

{
  Serial.print("Received smthg");
}

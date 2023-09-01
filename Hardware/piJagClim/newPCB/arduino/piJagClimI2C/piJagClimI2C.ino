
#include <Wire.h>
byte dataArray[18];

void setup()

{
  
  Wire.begin(184);                // join i2c bus with address #184?56?

  //Wire.onReceive(receiveEvent); // register event

  //Serial.begin(115200);           // start serial for output
  
 //Serial.print("Initialisation");
 for(int i=0; i<12; i++){
  pinMode(i, OUTPUT);
  digitalWrite(i, LOW);
 }
}


void loop()

{
  digitalWrite(0, LOW);
  delay(1000);
  digitalWrite(0, HIGH);
  delay(500);
  
}


// function that executes whenever data is received from master

// this function is registered as an event, see setup()

void receiveEvent(int howmany) //howmany registers the number bytes received from Master
{
     for(int i=0; i<howmany; i++)
     {
          dataArray[i] = Wire.read();  
     }
/*
     for (int i=0; i<howmany; i++)
     {
         Serial.print(dataArray[i], HEX);   //check what you are receiving against an Intel-Hex frame
         Serial.print(" ");
      }*/
      if(howmany >= 17){
       Serial.print("Screen Logo, face arrow : ");
       Serial.print(dataArray[7], HEX);
       Serial.print("; ");
       Serial.print("Little Man, feet arrow : ");
       Serial.print(dataArray[9], HEX);
       Serial.print("; ");
       Serial.print("Auto : ");
       Serial.print(dataArray[10], HEX);
       Serial.print("; ");
       Serial.print("Half degree point: ");
       Serial.print(dataArray[11], HEX);
       Serial.print(dataArray[12], HEX);
       Serial.print("; ");
       Serial.print("units: ");
       Serial.print(dataArray[13], HEX);
       Serial.print(dataArray[14], HEX);
       Serial.print("; ");
       Serial.print("tens: ");
       Serial.print(dataArray[15], HEX);
       Serial.print("; ");
       Serial.print("Fan level: ");
       Serial.print(dataArray[16], HEX);
       Serial.print(dataArray[17], HEX);
       Serial.print("; ");
      }
       
      Serial.println();

}

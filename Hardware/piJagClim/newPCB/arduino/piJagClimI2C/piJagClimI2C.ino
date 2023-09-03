
#include <Wire.h>
byte dataArray[18];

void setup()

{
  
  Wire.begin(184);                // join i2c bus with address #184?56?

  Wire.onReceive(receiveEvent); // register event

  Serial.begin(115200);           // start serial for output
  
 Serial.print("Initialisation");
 pinMode(A0, OUTPUT);
 digitalWrite(A0, LOW);
 pinMode(A1, OUTPUT);
 digitalWrite(A1, LOW);
 
 for(int i=2; i<12; i++){
  pinMode(i, OUTPUT);
  digitalWrite(i, LOW);
 }
 // plus and minus temp
 test();
}


void loop()

{
  delay(10);
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
       Serial.println();
       if(dataArray[11] == 0x0){
        // press power on
        digitalWrite(A0, LOW);
        delay(10);
        digitalWrite(A0, HIGH);
        delay(800);
        digitalWrite(A0, LOW);
       }
      }
       
      

}
int press_button(int pin){
  if(pin==0){
    digitalWrite(A0, LOW);
    delay(10);
    digitalWrite(A0, HIGH);
    delay(800);
    digitalWrite(A0, LOW);
  }
  else if(pin==1){
    digitalWrite(A1, LOW);
    delay(10);
    digitalWrite(A1, HIGH);
    delay(800);
    digitalWrite(A1, LOW);
  }
  else {
    digitalWrite(pin, LOW);
    delay(10);
    digitalWrite(pin, HIGH);
    delay(800);
    digitalWrite(pin, LOW);
  }
  return pin;
}

void test() {
  int pressed;
  /*
  for(int i=0; i<12; i++){
    pressed = press_button(i);
    Serial.println(pressed);
    delay(1000);
  }*/
  
  // press plus
  for(int i=0; i<10; i++){
    pressed = press_button(2);
    Serial.println(pressed);
    delay(500);
  }
  // press minus
  for(int i=0; i<10; i++){
    pressed = press_button(1);
    Serial.println(pressed);
    delay(500);
  }
}

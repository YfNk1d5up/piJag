
#include <Wire.h>
byte dataArray[25];
byte x;
void setup()

{
  
  Wire.begin(184);                // join i2c bus with address #184?56?

  Wire.onReceive(receiveEvent); // register event

  Serial.begin(115200);           // start serial for output
  Serial.setTimeout(1);
 Serial.print("Initialisation");
   pinMode(A0, OUTPUT);
   digitalWrite(A0, LOW);
   pinMode(A1, OUTPUT);
   digitalWrite(A1, LOW);
   
   for(int i=2; i<14; i++){
    pinMode(i, OUTPUT);
    digitalWrite(i, LOW);
   }
 // plus and minus temp
 //test();
}


void loop()

{
  Serial.flush();
  while (!Serial.available());
  x = Serial.read();
  switch (x) {
  case 0x01:
    press_button(0);
    Serial.write(x);
    Serial.write(dataArray, 25);
    break;
  case 0x02:
    press_button(2);
    Serial.write(x);
    Serial.write(dataArray, 25);
    break;
  case 0x03:
    press_button(1);
    Serial.write(x);
    Serial.write(dataArray, 25);
    break;
  case 0x04:
    press_button(3);
    Serial.write(x);
    Serial.write(dataArray, 25);
    break;
  case 0x05:
    press_button(9);
    Serial.write(x);
    Serial.write(dataArray, 25);
    break;
  case 0x06:
    press_button(5);
    Serial.write(x);
    Serial.write(dataArray, 25);
    break;
  }
  
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
}
int press_button(int pin){
  if(pin==0){
    digitalWrite(A0, LOW);
    digitalWrite(A0, HIGH);
    delay(200);
    digitalWrite(A0, LOW);
  }
  else if(pin==1){
    digitalWrite(A1, LOW);
    digitalWrite(A1, HIGH);
    delay(200);
    digitalWrite(A1, LOW);
  }
  else {
    digitalWrite(pin, LOW);
    digitalWrite(pin, HIGH);
    delay(200);
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

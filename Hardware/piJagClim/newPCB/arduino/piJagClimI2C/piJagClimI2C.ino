
#include <Wire.h>
byte dataArray[25];
byte x;
int dir;
void setup()

{
  
  Wire.begin(184);                // join i2c bus with address #184?56?

  Wire.onReceive(receiveEvent); // register event

  Serial.begin(115200);           // start serial for output
  Serial.setTimeout(1);
  //Serial.print("Initialisation");
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
  case 0x01: // ON OFF
    press_button(0);
    break;
  case 0x02: // minus
    press_button(2);
    break;
  case 0x03: // plus
    press_button(1);
    break;
  case 0x04: // auto
    press_button(3);
    break;
  case 0x05: // front defrost
    press_button(9);
    break;
  case 0x06: // face
    press_button(5);
    break;
  case 0x07: // face & feet
    press_button(7);
    break;
  case 0x08: // feet
    press_button(6);
    break;
  case 0x09: // front defrost & feet
    press_button(4);
    break;
  case 0x0a: // A/C
    press_button(10);
    break;
  case 0x0b: // rear defrost
    press_button(11);
    break;
  case 0x0c: // Recycle
    press_button(8);
    break;
  case 0x0d: // up Fan
    dir = rotary_encode(0);
    break;
  case 0x0e: // down Fan
    dir = rotary_encode(1);
    break;
   case 0x10: // ask values
    break;
  }
  delay(100);
  Serial.write(x);
  Serial.write(dataArray, 25);
}


// function that executes whenever data is received from master

// this function is registered as an event, see setup()

void receiveEvent(int howmany) //howmany registers the number bytes received from Master
{
     for(int i=0; i<howmany; i++)
     {
          dataArray[i] = Wire.read();  
     }
     //Serial.write(dataArray, 25);
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
    delay(150);
    digitalWrite(A1, LOW);
  }
  else {
    digitalWrite(pin, LOW);
    digitalWrite(pin, HIGH);
    delay(150);
    digitalWrite(pin, LOW);
  }
  return pin;
}

int rotary_encode(int direction){
  if(direction==0){
    digitalWrite(12, LOW);
    digitalWrite(13, LOW);
    digitalWrite(12, HIGH);
    delay(20);
    digitalWrite(13, HIGH);
    delay(20);
    digitalWrite(12, LOW);
    delay(20);
    digitalWrite(13, LOW);
  }
  else if(direction==1){
    digitalWrite(12, LOW);
    digitalWrite(13, LOW);
    digitalWrite(13, HIGH);
    delay(20);
    digitalWrite(12, HIGH);
    delay(20);
    digitalWrite(13, LOW);
    delay(20);
    digitalWrite(12, LOW);
  }
  return direction;
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

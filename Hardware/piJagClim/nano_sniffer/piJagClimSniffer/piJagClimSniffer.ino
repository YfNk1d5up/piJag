#include "main.h"
#include "tuart.h"
#include "i2csniff.h"
#include "dummy_send.h"
void setup() {
   u8 bit_count; // needs to be global as it is used by the isr
  
  init_sw_uart();
  init_i2c();

  #ifdef PARSER_MODE
  i2c_sniff_sm();
  #endif

}

void loop() {
  // put your main code here, to run repeatedly:

}

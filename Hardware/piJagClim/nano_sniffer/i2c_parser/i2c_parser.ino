/************************************************************************/
/*                                                                      */
/*                      I2C Sniffer          */
/*                                                                      */
/*              Author: Peter Dannegger                                 */
/*                                                                      */
/************************************************************************/
#include "main.h"
#include "uart.h"
#include "i2csniff.h"
#include "PARSE.h"
#include "tuart.h"

void init_i2c( void )
{
  RAW = 0;
  RAW_DDR = 0;  // delay input
  DLA = 1;
  DLA_DDR = 1;  // delay output
  SCL = 1;
  SCL_DDR = 0;        // force busy waiting
  SDA = 1;
  SDA_DDR = 0;        // listen only, no ACK, no data
  USICR = 1<<USIWM1 ^ 1<<USIWM0;    // I2C, no counter
  USISR = 1<<USIPF ^ 1<<USISIF ^ 1<<USIOIF;  // clear start, stop and overflow
}

void i2c_sniff_sm( void )
{
  u8 get_ack = 0;
  u8 state_of_raw = 1;
  u8 sr;
  u8 dr;
  u8 rx_buff[RX0_SIZE];  // frame buffer
  u8 rx_buff_high_water = 0; // contents of the frame buffer
    
  for(;;)
  {
    state_of_raw = RAW_PIN;
    do { __asm__ __volatile__ ("nop"); } while (0);
    DLA = state_of_raw;
    
    sr = USISR;              // get the value of the status register into a variable
    
    if( sr & 1<<USIPF ) {     // if STOP received
      rx_buff_high_water = 0;
      USICR = 1<<USIWM1 ^ 1<<USIWM0;  // I2C, no counter
      USISR = 1<<USIPF;     // clear USIPF (STOP flag)
      continue;
    }

    if( sr & 1<<USISIF ) {    // if START received
      get_ack = 0;              // set up get_ack for the next received symbol being data
      rx_buff_high_water = 1;     // start of a new message
      while( SCL_PIN );     // wait until SCL = low
      USICR = 1<<USICS1 ^ 1<<USICS0 ^ 1<<USIWM1 ^ 1<<USIWM0;    // set control register : I2C mode, turn off clock
      USISR = 1<<USISIF ^ 1<<USIOIF ^ (0x0F & -16);     // clear USISIF (start detect) and USIOIF (overflow detect), prime to count 16 edges (8 bits)
      continue;
    }

    if( sr & 1<<USIOIF ) {    // if Data / ACK received (overflowed at 16 edges or 2 edges)
      dr = USIDR;     // get the data / ack status from the data register
      if( ++get_ack & 1 ) {   // if this is data (++ primes for the next event)
        USISR = 1<<USIOIF ^ (0x0F & -2);  // prime the counter to count 2 edges next time
        //transmit_bytes(rx_buff, 1);
        if (rx_buff_high_water) {  //  means that we are currently gathering all good data in our frame
          *(rx_buff + (rx_buff_high_water++)-1) = dr;   // put the data into the frame buffer, increment the frame level
          }
      }
      else {  // if we are looking for an ACK / NACK
        USISR = 1<<USIOIF ^ (0x0F & -16); // clear the overflow and count 16 edges next time
        if (0 == (dr & 1)) {
          rx_buff_high_water = 0;   // if this was an ACK, we can discard as not valid (we only like ACKless frames)
        }
      }
      continue;
    }
    
    if (18 == rx_buff_high_water) {
      munge_frame(rx_buff);
      rx_buff_high_water = 0;
      USISR = 1<<USISIF ^ 1<<USIOIF;  // clear flags as we have been away in the uart routine a long time and might have missed something.
      continue;
    }
  }
}

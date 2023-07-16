/*
 * tuart.h
 *
 * Created: 23/02/2020 20:07:58
 *  Author: david
 */ 


#ifndef TUART_H_
#define TUART_H_


#define TX0_SIZE	24		// usable: TX0_SIZE - 1 (1 .. 255)
#define NUMBITS 20       // each byte has 8 data bits and a stop bit

#define COMPARE_VALUE 215  // compare value of 215 always
#define PRESCALE_VALUE 1<<CS11   // prescaler setting for timer 1

void init_sw_uart(void);
void set_tx(u8);
void transmit_byte(u8);
void transmit_bytes(u8 *, u8);


#endif /* TUART_H_ */
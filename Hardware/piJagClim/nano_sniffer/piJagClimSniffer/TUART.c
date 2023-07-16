
#include "main.h"
#include "tuart.h"

volatile u8 bit_count;

void init_sw_uart()
{
	// clear interrupts
	cli();

	// set timer compare value
	OCR1A = COMPARE_VALUE;
	// clear interrupt flag at the same time
	OCR1C = COMPARE_VALUE;

	// set up timer compare to clear the timer when compare value C is reached
	// and set prescaler : CS12 gives 9600bd; CS11 gives 38400bd
	TCCR1 = 1<<CTC1^PRESCALE_VALUE;
	
	// set UART transmit output high
	UTX = 1;

	// disable PWM and pin outputs
	GTCCR = 0;
	
	// output enable
	UTX_DDR = 1;
	
	// Turn on timer 1 compare interrupt A enable
	TIMSK = 1<<OCIE1A;
}

void set_tx(u8 tx_state)
{
	UTX = (tx_state ? 1 : 0);
}

void transmit_byte(u8 byte)
{
	set_tx(0); // start bit
	while (bit_count == NUMBITS + 2); // wait on interrupt for end of start bit
	
	set_tx((byte&0x01)); // send bit 0
	//set_tx((byte&0x80)>>7); // send bit 7
	while (bit_count == NUMBITS + 1); // wait one bit period
	
	set_tx((byte&0x02)>>1); // send bit 1
	//set_tx((byte&0x40)>>6); // send bit 6
	while (bit_count == NUMBITS); // wait one bit period

	set_tx((byte&0x04)>>2); // send bit 2
	//set_tx((byte&0x20)>>5); // send bit 5
	while (bit_count == NUMBITS - 1); // wait one bit period

	set_tx((byte&0x08)>>3); // send bit 3
	//set_tx((byte&0x10)>>4); // send bit 4
	while (bit_count == NUMBITS - 2); // wait one bit period

    set_tx((byte&0x10)>>4); // send bit 4
	//set_tx((byte&0x08)>>3); // send bit 3
	while (bit_count == NUMBITS - 3); // wait one bit period

	set_tx((byte&0x20)>>5); // send bit 5
	//set_tx((byte&0x04)>>2); // send bit 2
	while (bit_count == NUMBITS - 4); // wait one bit period

    set_tx((byte&0x40)>>6); // send bit 6
	//set_tx((byte&0x02)>>1); // send bit 1
	while (bit_count == NUMBITS - 5); // wait one bit period

	set_tx((byte&0x80)>>7); // send bit 7
	//set_tx((byte&0x01)); // send bit 0
	while (bit_count == NUMBITS - 6); // wait one bit period

	set_tx(1); // send stop bit
	while (bit_count); // wait one bit period
}

void transmit_bytes(u8 * tx_queue, u8 tx_count)
{	    
    //  wait for a guaranteed one bit time
    bit_count = 2;
    sei();  // enable interrupts for the bit counter
    while(bit_count);
  
    // and send out the data
    while (tx_count--)
    {
        // reset the bit counter
        bit_count = NUMBITS + 2;
        
		// transmit all bytes in frame
		transmit_byte(* tx_queue);
		tx_queue++;
    }
    
    // wait til the next clock interrupt
    cli();  // disable interrupts - not used outside UART code
}

ISR( TIM1_COMPA_vect )
{
	// update volatile flag when compare A is matched
    bit_count--;
}
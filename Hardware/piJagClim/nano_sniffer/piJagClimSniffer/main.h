#ifndef _main_h_
#define _main_h_
#include <avr\interrupt.h>
#include <avr\io.h>
#include <stddef.h>
#include "mydefs.h"


// #define SNIFFER_MODE
// #define TEST_MODE
#define PARSER_MODE


#define	LINEFEED	"\r\n"


//#define	STX_DDR		SBIT( DDRB, 1 )		// must be OC1A !

#define	SDA		SBIT( PORTB, 0 )
#define	SDA_DDR		SBIT( DDRB, 0 )
#define	SDA_PIN		SBIT( PINB, 0 )

#define	UTX		SBIT( PORTB, 1 )
#define	UTX_DDR		SBIT( DDRB, 1 )
#define	UTX_PIN		SBIT( PINB, 1 )

#define	SCL		SBIT( PORTB, 2 )
#define SCL_DDR		SBIT( DDRB, 2 )
#define	SCL_PIN		SBIT( PINB, 2 )

#define	RAW		SBIT( PORTB, 3 )
#define RAW_DDR		SBIT( DDRB, 3 )
#define	RAW_PIN		SBIT( PINB, 3 )

#define	DLA		SBIT( PORTB, 4 )
#define DLA_DDR		SBIT( DDRB, 4 )
#define	DLA_PIN		SBIT( PINB, 4 )

#endif

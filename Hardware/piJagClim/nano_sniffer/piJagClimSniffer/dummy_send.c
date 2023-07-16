/*
 * dummy_send.c
 *
 * Created: 23/02/2020 20:36:18
 *  Author: david
 */ 

#include "main.h"
#include "dummy_send.h"
#include "tuart.h"
#include "PARSE.h"

#define adata 0x50
#define bdata 0x44
#define cdata 0x20

static u8 dummy_tx_buff[TX0_SIZE];

void dummy_fill_frame()
{
	dummy_tx_buff[0] = adata;
	dummy_tx_buff[1] = bdata;
	dummy_tx_buff[2] = cdata;
	dummy_tx_buff[3] = adata;
	dummy_tx_buff[4] = bdata;
	dummy_tx_buff[5] = bdata;
	dummy_tx_buff[6] = bdata;
	dummy_tx_buff[7] = bdata;
	dummy_tx_buff[8] = cdata;
	dummy_tx_buff[9] = cdata;
	dummy_tx_buff[10] = cdata;

	transmit_bytes(dummy_tx_buff, 10);
}

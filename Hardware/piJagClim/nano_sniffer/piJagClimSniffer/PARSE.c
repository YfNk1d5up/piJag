/*
 * PARSE.c
 *
 * Created: 28/01/2020 20:18:57
 *  Author: david
 */ 

#include "main.h"
#include "PARSE.h"
#include "tuart.h"

#define temp_ext_units tx_buff[0]
#define temp_ext_tens tx_buff[1]
#define screen_face tx_buff[2]
#define man_feet tx_buff[3]
#define auto_symbol tx_buff[4]
#define half_degree tx_buff[5]
#define temp_setpoint_units tx_buff[6]
#define temp_setpoint_tens tx_buff[7]
#define fan_symbol tx_buff[8]
#define fan_level tx_buff[9]
#define final_null_character tx_buff[10]

static u8 tx_buff[TX0_SIZE];

u8 bitmask;

void munge_frame(u8 * buff)  // turns i2c words into ascii representation of lcd
{
	temp_ext_units = 0x31;
	temp_ext_tens = 0x34;
	screen_face = 0;
	man_feet = 0;
	auto_symbol = 0;
	half_degree = 0;
	temp_setpoint_units = 0;
	temp_setpoint_tens = 0;
	fan_symbol = 0;
	fan_level = 0;
	
	if (buff[0] == 0x70) {
		if (buff[1] == 0xC8) {
			if (buff[2] == 0x8D) {
				if (buff[3] == 0xE0) {
					if (buff[4] == 0x78) {
						bitmask = buff[7] & 0x88;
						switch (bitmask) {
							case 0x00 :
								screen_face = '-';
								break;
							case 0x80 :
								screen_face = 's';
								break;
							case 0x08 :
								screen_face = 'f';
								break;
							case 0x88 :
								screen_face = 'b';
						}
						bitmask = buff[9] & 0x88;
						switch (bitmask) {
							case 0x00 :
							man_feet = '-';
							break;
							case 0x80 :
							man_feet = 'm';
							break;
							case 0x08 :
							man_feet = 'f';
							break;
							case 0x88 :
							man_feet = 'b';
						}
						auto_symbol = buff[10] & 0x04 ? 'a' : '-';
						bitmask = buff[11];
						switch (bitmask) {
							case 0x00 :
							half_degree = '-';
							break;
							case 0xB0 :
							half_degree = '0';
							break;
							case 0xE0 :
							half_degree = '5';
							break;
						}
						if (buff[13] == 0xB0) {
							temp_setpoint_units = '0';
						}
						if ((buff[13] == 0x30) && (buff[14] == 0x00)) {
							temp_setpoint_units = '1';
						}
						if (buff[13] == 0xD0) {
							temp_setpoint_units = '2';
						}
						if ((buff[13] == 0xF0) && (buff[14] == 0x14)) {
							temp_setpoint_units = '3';
						}
						if ((buff[13] == 0x70) && (buff[14] == 0x05)) {
							temp_setpoint_units = '4';
						}
						if ((buff[13] == 0xE0) && (buff[14] == 0x15)) {
							temp_setpoint_units = '5';
						}
						if ((buff[13] == 0xE0) && (buff[14] == 0x17)) {
							temp_setpoint_units = '6';
						}
						if ((buff[13] == 0x30) && (buff[14] == 0x11)) {
							temp_setpoint_units = '7';
						}
						if ((buff[13] == 0xF0) && (buff[14] == 0x17)) {
							temp_setpoint_units = '8';
						}
						if ((buff[13] == 0x70) && (buff[14] == 0x15)) {
							temp_setpoint_units = '9';
						}
						if (buff[15] == 0x30) {
							temp_setpoint_tens = '1';
						}
						if (buff[15] == 0xD0) {
							temp_setpoint_tens = '2';
						}
						if (buff[15] == 0xF0) {
							temp_setpoint_tens = '3';
						}
						if (buff[15] == 0x70) {
							temp_setpoint_tens = 'H';
						}
						if (buff[15] == 0x80) {
							temp_setpoint_tens = 'L';
						}
						fan_symbol = buff[16] & 0x80 ? 'F' : '-';
						if ((buff[17] == 0x00) && (buff[18] == 0xA0)) {
							fan_level = '1';
						}
						if ((buff[17] == 0x00) && (buff[18] == 0xE0)) {
							fan_level = '2';
						}
						if ((buff[17] == 0x00) && (buff[18] == 0xF0)) {
							fan_level = '3';
						}
						if ((buff[17] == 0x00) && (buff[18] == 0xF0)) {
							fan_level = '4';
						}
						if (buff[17] == 0x05) {
							fan_level = '5';
						}
						if (buff[17] == 0x07) {
							fan_level = '6';
						}
						if (buff[17] == 0x0F) {
							fan_level = '7';
						}
						if (buff[17] == 0x8F) {
							fan_level = '8';
						}
						if (buff[17] == 0xAF) {
							fan_level = '9';
						}
						if (buff[17] == 0xEF) {
							fan_level = 'A';
						}
						if (buff[17] == 0xFF) {
							fan_level = 'B';
						}
						final_null_character = 0;		
									
						transmit_bytes(tx_buff,11);	
						
					}
				}
			}
		}
	}
}

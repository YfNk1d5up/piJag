#ifndef _parse_h_
#define _parse_h_

// structure of the input :
//  23 uint8_t
//
// structure of the output :
//  15 uint8_t
// e.g. T245AF11V1RO10x_
// temp 24.5 auto fan 11 vents setting 1 recirc outdoor 10


void munge_frame(u8 *);

#define RX0_SIZE    20

#endif

//avr-gcc -Os -g -o water_level.elf water_level.c -mmcu=atmega328p

#ifndef F_CPU
#define F_CPU 16000000UL // telling controller crystal frequency (16 MHz AVR ATMega328P)
#endif

#include <avr/io.h> // Defines pins, ports, etc.

#define BUTTON1 0 // button switch connected to port B pin 0

#define LED1 1 // Led1 connected to port B pin 0

void init_ports_mcu()
{
	DDRB = 0b00000010; // Configures PB1 as output rest as input
}

void water_level(){
	if (PINB & (1<<BUTTON1)){
		PORTB |= (1<<LED1);
	}
	else{
		PORTB &= ~(1<<LED1);
	}
}

int main (void)
{
	init_ports_mcu();
	while (1){	
		water_level();
	}
	return (0); 
}
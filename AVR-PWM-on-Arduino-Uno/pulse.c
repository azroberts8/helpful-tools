#include <avr/io.h>
#include <avr/interrupt.h>
#include <stdbool.h>

// Gradually pluse LED brightness over 4s period

char brightness = 0;
char step = 0;
bool state = 0;
bool increasing = 1;

void setup() {
  DDRB |= (1 << PORTB3); // Pin 11 output
  cli(); // stop interrupts

  // set timer0 interrupt at 12.8KHz
  TCCR0A = 0b00000010;
  TCCR0B = 0b00000010; // 8 prescaler
  TCNT0 = 0; // set timer to 0
  OCR0A = 155;
  TIMSK0 |= (1 << OCIE0A); // enable timer compare interrupt

  // set timer1 interrupt at 64Hz
  TCCR1A = 0;
  TCCR1B = 0;
  TCNT1 = 0; // set timer to 0
  OCR1A = 976;
  TCCR1B |= (1 << WGM12); // enable CTC
  TCCR1B |= (1 << CS12); // 256 prescaler
  TIMSK1 |= (1 << OCIE1A);

  sei(); // resume interrupts
}

ISR(TIMER0_COMPA_vect) {
  if(step <= brightness && !state) {
    // turn on
    PORTB |= (1 << PORTB3);
    state = 1;
  } else if(step > brightness && state) {
    // turn off
    PORTB &= ~(1 << PORTB3);
    state = 0;
  }
  step = (step + 1) % 128;
}

ISR(TIMER1_COMPA_vect) {
  if(increasing) {
    if(brightness == 126) increasing = 0;
    brightness++;
  } else {
    if(brightness == 1) increasing = 1;
    brightness--;
  }
}

void loop() {
  // put your main code here, to run repeatedly:
  ;
}

int main(void) {
  setup();

  while(true) {
    loop();
  }
}
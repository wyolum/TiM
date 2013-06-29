#include "TiM.h"
#include <Adafruit_NeoPixel.h>
TiM tim;

// Use Arduino Pins 2-9 for controling the rows of TiM
uint8_t pins[8] = {2, 3, 4, 5, 6, 7, 8, 9};
// uint8_t pins[8] = {0,1,2, 3, 4, 5, 6, 7};
const uint16_t n_led_per_row = 64;

void setup(){
  tim.setup(8, n_led_per_row, pins);
}

void loop(){
  uint8_t row, col, r, g, b;
  for(int ii = 0; ii < 20; ii++){
    row = random(0, 8);
    col = random(0, 16);
    r = random(0, 24);
    g = random(0, 24);
    b = random(0, 24);
    tim.setPixel(row, col, Color(r, g, b));
  }
  tim.show();
}


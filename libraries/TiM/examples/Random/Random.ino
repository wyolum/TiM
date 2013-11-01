#include "TiM.h"
#include <Adafruit_NeoPixel.h>
TiM tim;

// Use Arduino Pins 2-9 for controling the rows of TiM
uint8_t pins[8] = {2, 3, 4, 5, 6, 7, 8, 9};
// uint8_t pins[8] = {0,1,2, 3, 4, 5, 6, 7};
const uint16_t n_led_per_row = 32;

const uint8_t N_ROW = 32;
const uint8_t N_COL = 8;
const uint8_t BRIGHT = 255;
const uint8_t N_LED_PER_STEP = 20;

void setup(){
  tim.setup(8, n_led_per_row, pins);
}

void loop(){
  uint8_t row, col, r, g, b;
  for(int ii = 0; ii < N_LED_PER_STEP; ii++){
    row = random(0, N_ROW);
    col = random(0, N_COL);
    r = random(0, BRIGHT);
    g = random(0, BRIGHT);
    b = random(0, BRIGHT);
    tim.setPixel(row, col, Color(r, g, b));
  }
  tim.show();
}


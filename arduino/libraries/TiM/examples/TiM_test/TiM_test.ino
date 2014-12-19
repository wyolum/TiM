#include "TiM.h"
#include "Adafruit_NeoPixel.h"
TiM tim;

// Use Arduino Pins 2-9 for controling the rows of TiM
uint8_t pins[8] = {2, 3, 4, 5, 6, 7, 8, 9};
// uint8_t pins[8] = {0, 1, 2, 3, 4, 5, 6, 7};

void setup(){
  // each Pin has 32 leds
  //    #rows #led pin_ids
  tim.setup(8, 64, pins);
  tim.setall(Color(255, 255, 255));
  tim.show();
  delay(1000);
  tim.setall(Color(255, 0, 0));
  tim.show();
  delay(1000);
  tim.setall(Color(0, 255, 0));
  tim.show();
  delay(1000);
  tim.setall(Color(0, 0, 255));
  tim.show();
  delay(1000);
}

uint32_t count = 0;
int row, col;

void loop(){
  // grab a color from the color wheel
  //                     HUE 0-255  brightness 0-255
  uint32_t color = Wheel(count % 256, 255);
  
  // turn off column
  for(row = 0; row < tim.n_strip; row++){
  // tim.setPixel(row, col, 0);
  }

  // turn on new column
  col++;
  col %= tim.strips[0].numLEDs;
  for(row = 0; row < tim.n_strip; row++){
    tim.setPixel(row, col, color);
  }

  // update the display
  tim.show();
  count++;
}


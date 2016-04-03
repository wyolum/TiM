/*
  Mood lighting app for TiM.
  A0 -- POT -- Red
  A1 -- POT -- Green
  A2 -- POT -- Blue
  A3 -- POT -- Fader
 */

#include <Adafruit_NeoPixel.h>

#define N_PIXEL 256
Adafruit_NeoPixel strip = Adafruit_NeoPixel(N_PIXEL, 2, NEO_GRB + NEO_KHZ800);

void colorWipe(Adafruit_NeoPixel *strip_p,uint32_t c, uint8_t wait) {
  for(uint16_t i=0; i<strip_p->numPixels(); i++) {
      strip_p->setPixelColor(i, c);
      if(wait > 0){
	strip_p->show();
	delay(wait);
      }
  }
  strip_p->show();
}

void setColor(uint8_t r, uint8_t g, uint8_t b, uint8_t brightness){
  uint32_t color = strip.Color(r, g, b);
  strip.setBrightness(brightness);
  colorWipe(&strip, color, 0);
}

void setup(){
  pinMode(A0, INPUT);
  pinMode(A1, INPUT);
  pinMode(A2, INPUT);
  pinMode(A3, INPUT);
}
uint8_t r_val, g_val, b_val, f_val;
void loop(){
  uint8_t new_r_val = analogRead(A0) >> 2;
  uint8_t new_g_val = analogRead(A1) >> 2;
  uint8_t new_b_val = analogRead(A2) >> 2;
  uint8_t new_f_val = analogRead(A3) >> 2;
  if((r_val != new_r_val) ||
     (g_val != new_g_val) ||
     (b_val != new_b_val) ||
     (f_val != new_f_val)){
    setColor(r_val, g_val, b_val, f_val);
  }
}

#include <Adafruit_NeoPixel.h>

// Parameter 1 = number of pixels in strip
// Parameter 2 = pin number (most are valid)
// Parameter 3 = pixel type flags, add together as needed:
//   NEO_RGB     Pixels are wired for RGB bitstream
//   NEO_GRB     Pixels are wired for GRB bitstream
//   NEO_KHZ400  400 KHz bitstream (e.g. FLORA pixels)
//   NEO_KHZ800  800 KHz bitstream (e.g. High Density LED strip)
Adafruit_NeoPixel strip = Adafruit_NeoPixel();

void setup() {
  strip.setup(250, 2, NEO_GRB + NEO_KHZ800);
  strip.begin();
  strip.show(); // Initialize all pixels to 'off'
}

void loop() {
  // Some example procedures showing how to display to the pixels:
  colorWipe(strip.Color(0, 0, 0), 0); // Off
  colorWipe(strip.Color(255, 0, 0), 1); // Red
  colorWipe(strip.Color(0, 255, 0), 1); // Green
  colorWipe(strip.Color(0, 0, 255), 1); // Blue
  rainbow(1);
  rainbowCycle(0);
  colorWipe(strip.Color(0, 0, 0), 0); // Off
  int i = 0;
  while(i < strip.numPixels() * 3){
    strip.setPixelColor(i % strip.numPixels(), strip.Color(0, 0, 0));
    strip.setPixelColor(i % strip.numPixels() + 1, strip.Color(255, 0, 0));
    
    if(i % 2 == 0){
      strip.setPixelColor((i/2 + strip.numPixels()) % strip.numPixels(), strip.Color(0, 0, 0));
      strip.setPixelColor((i/2 + 1 + strip.numPixels()) % strip.numPixels(), strip.Color(0, 255, 0));
    }
    if(i % 3 == 0){
      strip.setPixelColor((i/3 + strip.numPixels()) % strip.numPixels(), strip.Color(0, 0, 0));
      strip.setPixelColor((i/3 + 1 + strip.numPixels()) % strip.numPixels(), strip.Color(0, 0, 255));
    }
    strip.show();
    delay(80);
    i += 1;
  }
  colorWipe(strip.Color(0, 0, 0), 0); // Off
  while(1); delay(1000);
}

// Fill the dots one after the other with a color
void colorWipe(uint32_t c, uint8_t wait) {
  for(uint16_t i=0; i<strip.numPixels(); i++) {
      strip.setPixelColor(i, c);
      strip.show();
      delay(wait);
  }
}

void rainbow(uint8_t wait) {
  uint16_t i, j;

    for(i=0; i<strip.numPixels(); i++) {
      strip.setPixelColor(i, Wheel((i+j) & 255));
      strip.show();
      delay(wait);
  }
}

// Slightly different, this makes the rainbow equally distributed throughout
void rainbowCycle(uint8_t wait) {
  uint16_t i, j;

  for(j=0; j<256*5; j++) { // 5 cycles of all colors on wheel
    for(i=0; i< strip.numPixels(); i++) {
      strip.setPixelColor(i, Wheel(((i * 256 / strip.numPixels()) + j) & 255));
    }
    strip.show();
    delay(wait);
  }
}

// Input a value 0 to 255 to get a color value.
// The colours are a transition r - g - b - back to r.
uint32_t Wheel(byte WheelPos) {
  if(WheelPos < 85) {
   return strip.Color(WheelPos * 3, 255 - WheelPos * 3, 0);
  } else if(WheelPos < 170) {
   WheelPos -= 85;
   return strip.Color(255 - WheelPos * 3, 0, WheelPos * 3);
  } else {
   WheelPos -= 170;
   return strip.Color(0, WheelPos * 3, 255 - WheelPos * 3);
  }
}

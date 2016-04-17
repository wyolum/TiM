#ifndef ___TEXTYH___
#define ___TEXTYH___
#include "displayMode.h"

#include <Adafruit_GFX.h>
#include <Adafruit_NeoMatrix.h>
#include <Adafruit_NeoPixel.h>
#define potPin A0
#define PIN 5
  Adafruit_NeoMatrix matrix = Adafruit_NeoMatrix(16, 8, PIN,
  NEO_MATRIX_TOP     + NEO_MATRIX_RIGHT +
  NEO_MATRIX_ROWS + NEO_MATRIX_PROGRESSIVE,
  NEO_GRB            + NEO_KHZ800);
class texty : public displayMode{
  public:
    texty(void);
    void setup(void);
    void draw(void);
  private:
    uint16_t pass=0;
    int x = matrix.width();
    };
texty::texty(){}
void texty::setup(){
  Serial.println("setting up texty");
  matrix.begin();
   matrix.setTextWrap(false);
  matrix.setBrightness(40);
  matrix.setTextColor(matrix.Color(192,192,192));
}

void texty::draw(void){
  if (checkTime()){
    if (checkButton())
     return;
  setDelay(analogRead(potPin));
  matrix.fillScreen(0);
  matrix.setCursor(x, 0);
  matrix.print(F("Maker's Asylum"));
  if(--x < -72) {
    x = matrix.width();
    if(++pass >= 3) pass = 0;
    //matrix.setTextColor(colors[pass]);
  }
  matrix.show();
  }
}

#endif


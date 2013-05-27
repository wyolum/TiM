#include "TiM.h"
#include "Adafruit_NeoPixel.h"
TiM tim;
uint32_t count = 0;
uint16_t row, col;
const uint16_t n_led = 64;
const uint16_t n_byte = 3 * n_led;
const uint16_t n_bit = 8 * n_byte;
const uint8_t READY = 0b10101010;

// Use Arduino Pins 2-9 for controling the rows of TiM
uint8_t pins[8] = {2, 3, 4, 5, 6, 7, 8, 9};
uint8_t pixels[n_byte];

void setup(){
  pinMode(13, OUTPUT);
  tim.setup(8, n_led, pins);
  Serial.begin(9600);
}

// Class BitArray
bool BitArray_get(uint8_t *arr, int16_t idx){
  bool out = false;
  if(idx >= 0){
    out = (bool)((arr[idx / 8] >> (idx % 8)) & 1);
  }
  return out;
}

bool BitArray_set(uint8_t *arr, uint16_t idx, bool bit){
  uint8_t byte_i = idx / 8;
  uint8_t bit_j = (idx % 8);
  if(bit){ // set bit
    arr[byte_i] |= (bit << bit_j);
  }
  else{ // unset bit
    if(arr[byte_i] & (1L << bit_j)){
      arr[byte_i] -= (1L << bit_j);
    }
  }
}

void loop(){
  count++;
  interact();
  // tim.strips[row].setPixelColor(col, Color(25, 255, 0));
  // tim.strips[row].show();
}

void interact(){
  int count = 0;
  uint8_t val;

  col = 0;
  Serial.write(READY);
  Serial.write(row);
  delay(1);
  if(Serial.available()){
    while(col < n_byte && count < 10){
      if(!Serial.available()){
	delay(100);
      }
      val = (uint8_t)Serial.read();
      if(val != 255){
	count = 0;
	tim.strips[row].pixels[col] = val;
	col++;
      }
      else{
	count++;
      }
    }
    if(col == n_byte){
      tim.strips[row].show();
      row++;
      row %= 8;
    }
  }
}

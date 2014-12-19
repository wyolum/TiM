#include <Adafruit_NeoPixel.h>
#include <SPI.h>
#include <SD.h>

const uint8_t n_strip = 8;
const uint16_t n_led_per_strip = 16;
const uint8_t n_byte_per_led = 3;
const uint16_t n_byte_per_strip = n_led_per_strip * n_byte_per_led;
uint8_t buffer[n_byte_per_strip];

Adafruit_NeoPixel strips[n_strip];

//Global vars
File unifont_file;
File display_file;
const uint8_t SCREEN_WIDTH = 33;
const uint8_t UNIFONT_RECLEN = 33;
uint8_t unifont_data[UNIFONT_RECLEN - 1];
int count = 0;

// Use Arduino Pins 2-9 for controling the strips of TiM
uint8_t pins[8] = {2, 3, 4, 5, 6, 7, 8, 9};

/*
  convert a physical xy coord to TiM row/col based on
   B --> C
   ^     |
   |     v
-->A     D

parallel config
 */

void xy2tim(uint8_t x, uint8_t y, uint16_t *row_p, uint16_t *col_p){
  if(x < 16){ // LEFT x < 16
    if(y >= 8){// bottom left (BOARD A)
      *col_p = x;
      *row_p = y % 8;
    } 
    else{ // top left (BOARD B)
      *col_p = 16 + x;
      *row_p = y;
    }
  }
  else{ // RIGHT 16 < x < 32
    if(y < 8){// bottom left (BOARD C)
      *col_p = 16 + x;
      *row_p = y;
    } 
    else{ // top left (BOARD B)
      *col_p = 32 + x;
      *row_p = y % 8;
    }
  }
}

void SD_show(){
  Serial.print("SD_show() ");
  Serial.println(count);
  display_file.seek(0);
  
  for(uint8_t i = 0; i < n_strip; i++){
    display_file.read(strips[i].pixels, n_byte_per_strip);
    strips[i].show();
  }
}

void SD_setPixel(uint8_t x, uint8_t y, uint32_t color){
  uint16_t row, col;
  uint8_t r, g, b, brightness=20;
  
  xy2tim(x, y, &row, &col);
  
  display_file.seek((uint16_t)n_byte_per_strip * row + (uint16_t)n_byte_per_led * col);
  display_file.write((color >> 8) & 255);
  display_file.write((color >> 16) & 255);
  display_file.write((color >> 0) & 255);
}

void setup(){
  uint16_t row, col;

  Serial.begin(115200);
  if (!SD.begin(10)) {
    Serial.println("initialization failed!");
    while(1) delay(100);
  }
  else{
    Serial.println("SD initialized!");
  }

  for(uint8_t i = 0; i < n_strip; i++){
    // all strips share the same buffer
    strips[i].setup(n_led_per_strip, pins[i], NEO_GRB + NEO_KHZ800, buffer);
  }

  unifont_file = SD.open("UNIFONT.WFF");
  if(!unifont_file){
    Serial.println("No unifont file present");
  }
  display_file = SD.open("_.DSP", FILE_WRITE);

  // initialize display file
  for(uint8_t y=0; y < 16; y++){
    for(uint16_t x=0; x < 32; x++){
      display_file.write((uint8_t)1);
      display_file.write((uint8_t)2);
      display_file.write((uint8_t)3);
    }
  }
  // SD_show(); // only first show works??
}

void loop(){
  uint8_t r, g, b, brightness=20;
  uint16_t row, col;
  count++;

  for(int y = 0; y < 16; y++){
    for(int x = 0; x < 32; x++){
      // convert pysical x,y coords to TiM electrical row, col coords
      xy2tim(x, y, &row, &col);
      SD_setPixel(x, y, Color(x * count, y * count, 5*count));
    }
  }
  SD_show();
}

uint8_t screen_putchar(uint16_t unic, uint8_t left_x, uint32_t color){
  uint32_t pos;
  uint8_t char_width;
  uint8_t out = 16;
  uint16_t row;
  uint16_t col;
  uint8_t val;
  uint8_t bit_i;
  bool bit;
  
  if(left_x < 32){
    char_width = unifont_read_char(unic, unifont_data) / 16;
    for(uint16_t y = 0; y < 32; y++){
      for(byte x = 0; x < char_width; x++){
	for(byte j = 0; j < char_width; j++){
	  val = unifont_data[char_width * y + j];
	  for(bit_i = 0; bit_i < 8; bit_i++){
	    bit = (val >> bit_i) && 1;
	    xy2tim(x, y, &row, &col);
	    display_file.seek((y * SCREEN_WIDTH + col) * 3);
	    if(bit){
	      display_file.write((uint8_t)((color >>  0) & 0b11111111));
	      display_file.write((uint8_t)((color >>  8) & 0b11111111));
	      display_file.write((uint8_t)((color >> 16) & 0b11111111));
	    }
	    else{
	      display_file.write((uint8_t)(0));
	      display_file.write((uint8_t)(0));
	      display_file.write((uint8_t)(0));
	    }
	  }
	}
      } 
    }
    out = char_width * 8;
  }
  return out;
}

uint8_t unifont_read_char(uint32_t i, uint8_t *dest){
  uint8_t n_byte;
  unifont_file.seek(i * UNIFONT_RECLEN);
  n_byte = (uint8_t)unifont_file.read();

  for(uint8_t i = 0; i < n_byte; i++){
    dest[i] = (uint8_t)unifont_file.read();
  }
  return n_byte;
}

// Convert separate R,G,B into packed 32-bit RGB color.
// Packed format is always RGB, regardless of LED strand color order.
uint32_t Color(uint8_t r, uint8_t g, uint8_t b) {
  return ((uint32_t)r << 16) | ((uint32_t)g <<  8) | b;
}

// TODO Add Licence

#include "TiM.h"
#include "Adafruit_NeoPixel.h"

// constants
const uint8_t N_STRIP = 8;
const uint16_t N_LED_PER_STRIP = 64;
const uint8_t N_BYTE_PER_LED = 3;
const uint8_t N_LED_PER_MSG = 16;
const uint16_t N_BYTE_PER_STRIP = N_LED_PER_STRIP * N_BYTE_PER_LED;
const char READY = 'R';
const char CKSUM_FAIL = 'F';
const char CMD_SHOW = 'S';
const uint16_t MSG_LEN = (1                   + // CKSUM
			  N_BYTE_PER_LED * N_LED_PER_MSG + 
			  1                   + // ROW
                          1                   + // COL
			  1                   + // COMMAND
                          1);                   // carrage return
const uint8_t DAT_IDX = 1;
const uint8_t ROW_IDX = N_BYTE_PER_LED * N_LED_PER_MSG + 1;
const uint8_t COL_IDX = N_BYTE_PER_LED * N_LED_PER_MSG + 2;
const uint8_t CMD_IDX = N_BYTE_PER_LED * N_LED_PER_MSG + 3;
const uint32_t TIMEOUT_MS = 1000;

// globals
uint8_t buffer[N_BYTE_PER_STRIP];          // data for next pixel setting

// Use Arduino Pins 2-9 for controling the strips of TiM
uint8_t pins[8] = {2, 3, 4, 5, 6, 7, 8, 9};

// TiM global
TiM tim;

// the last row that was updated
uint8_t last_row = N_STRIP;

// Serial message
uint8_t message[MSG_LEN];

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

void setup(){
  pinMode(13, OUTPUT);
  tim.setup(N_STRIP, N_LED_PER_STRIP, pins, buffer);
  Serial.begin(115200);
}

uint32_t loop_count;

void loop(){
  int row = loop_count % 8;

  // for(int i=0; i < N_BYTE_PER_STRIP; i++){
  //  buffer[i] = (loop_count + (i * 10) % 25 + (row * 10) % 25) % 25;
  // }
  // tim.strips[row].changed = true;
  // tim.show();
  loop_count++;
  interact();
}

// cursors for msg buffer
uint8_t end_cursor = 0;

void interact(){
  uint8_t row, col, cmd, i, j;
  
  uint32_t start = millis();
  while(millis() - start < TIMEOUT_MS && 
	end_cursor < MSG_LEN){
    if(Serial.available()){
      message[end_cursor] = Serial.read();
      end_cursor++;
    }
  }
  if(end_cursor == MSG_LEN){
    if(cksum(message) == 0 && 
       message[MSG_LEN - 1] == '\n'){
      end_cursor = 0; // get ready for next msg
      Serial.write(READY); 

      row = message[ROW_IDX];
      col = message[COL_IDX];
      cmd = message[CMD_IDX];
      if(row != last_row){
	last_row = row;
	tim.show();
      }
      for(i=0; i < N_LED_PER_MSG; i++){
	for(j=0; j < N_BYTE_PER_LED; j++){
	  buffer[(col + i) * N_BYTE_PER_LED + j] = 
	    message[DAT_IDX + i * N_BYTE_PER_LED + j];
	}
      }
      tim.strips[row].changed = true;
      tim.show();
      //if(cmd == CMD_SHOW) tim.show();
    }
    else{
      Serial.write(CKSUM_FAIL);
      // Serial.write(cksum(message));
      // toss out first letter and resubmit
      end_cursor = MSG_LEN - 1;
      for(i = 0; i < MSG_LEN - 1; i++){
	message[i] = message[i + 1];
      }
    }
  }
}

uint8_t cksum(uint8_t *msg){
  uint8_t i, val = 0;
  for(i=0; i < MSG_LEN; i++){
    val += (i + 1) * (uint8_t)msg[i];
  }
#ifdef NOT_DEF
  if(val != 0){
    val = 0;
    for(i=0; i < MSG_LEN; i++){
      val += (i + 1) * (uint8_t)msg[i];
      Serial.print("    ");
      Serial.print(i);
      Serial.print(", ");
      Serial.print(msg[i]);
      Serial.print(",");
      Serial.println(val);
    }
  }
#endif
  return val;
}

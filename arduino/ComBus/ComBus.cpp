#include <Wire.h>
#include "ComBus.h"

//********************************************************
// Low level functions prototypes
//********************************************************
volatile int message[5];
void sendData();
void receiveData(int byteCount);
uint8_t id;
int16_t value;
uint8_t sendIndex;

//********************************************************
// Class implementation
//********************************************************
ComBus::ComBus(void) {
}

void ComBus::begin(void) {
  Wire.begin(ARDUINO_ADDR);                //Set up I2C
  Wire.onReceive(receiveData);
  Wire.onRequest(sendData);
  _cmd = 0;
  _param0 = 0;
  _param1 = 0;
  _param2 = 0;
  message[0] = 0;
  sendIndex = 0;
}

int8_t ComBus::readParam0(void) {
  return(_param0);
}

uint8_t ComBus::readCmd(void) {
  return(_cmd);
}

int8_t ComBus::readParam1(void) {
  return(_param1);
}

int8_t ComBus::readParam2(void) {
  return(_param2);
}

bool ComBus::newMessage(void) {
  if (message[0] != 0) {
    _cmd = message[0];
    _param0 = message[1];
    _param1 = message[2];
    _param2 = message[3];
    message[0] = 0;
    return (true);
  } else {
    return(false);
  }
}

void ComBus::sendMessage(uint8_t newId, int16_t newValue) {
	id = newId;
	value = newValue;
}


//Receive commands via I2C
void receiveData(int byteCount) {  
   static int index = 0;
   
    while(Wire.available()) {
        //When the buffer gets filled up with 4 bytes( the commands have to be 4 bytes in size), set the index back to 0 to read the next command
        if (Wire.available() == 4) {
            index=0;
        }
        message[index++] = Wire.read(); //Load the command into the buffer
     }
 }


// callback for sending data
void sendData() {
	switch (sendIndex) {
		case 0:
			Wire.write(id);
			sendIndex++;
			break;
		case 1:
			Wire.write(value & 0x00FF);
			sendIndex++;
			break;
		case 2:
			Wire.write(value >> 8);
			id = 0;
			value = 0;
			sendIndex = 0;
			break;
		default:
			Wire.write(0);
	}
	
}


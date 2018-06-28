#include <bacarMotor.h>
#include <Wire.h>
#include <I2C_comm.h>


BacarMotor motorA(9, 7, 8);
BacarMotor motorB(10, 11, 12);
I2C_comm comm;


void setup() {
  Serial.begin(9600);
  comm.begin();
  motorA.begin();
  motorB.begin();
  pinMode(2, OUTPUT);
  pinMode(3, OUTPUT);
  pinMode(4, OUTPUT);
  pinMode(5, OUTPUT);
}

void loop() {
  int cmd;

  if (comm.newMessage()==true) {
    cmd = comm.readCmd();
    Serial.println(cmd);
    if(cmd==CMD_LED1_ON) {
      digitalWrite(2, HIGH);
    }
    if(cmd==CMD_LED1_OFF) {
      digitalWrite(2, LOW);
    }
    if(cmd==CMD_LED2_ON) {
      digitalWrite(3, HIGH);
    }
    if(cmd==CMD_LED2_OFF) {
      digitalWrite(3, LOW);
    }
    if(cmd==CMD_LED3_ON) {
      digitalWrite(4, HIGH);
    }
    if(cmd==CMD_LED3_OFF) {
      digitalWrite(4, LOW);    }
    if(cmd==CMD_LED4_ON) {
      digitalWrite(5, HIGH);
    }
    if(cmd==CMD_LED4_OFF) {
      digitalWrite(5, LOW);
    }
    if(cmd == CMD_FORWARD) {
      motorA.actuate(comm.readParam1()/100.0);
      motorB.actuate(comm.readParam1()/100.0);
    }
    if(cmd == CMD_BACKWARD) {
      motorA.actuate(-comm.readParam1()/100.0);
      motorB.actuate(-comm.readParam1()/100.0);
    }
    if(cmd == CMD_LEFT) {
      motorA.actuate(comm.readParam1()/100.0);
      motorB.actuate(-comm.readParam1()/100.0);
    }
    if(cmd == CMD_RIGHT) {
      motorA.actuate(-comm.readParam1()/100.0);
      motorB.actuate(comm.readParam1()/100.0);
    }
  }
}





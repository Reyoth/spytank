#include <comBus.h>
#include <motor.h>


Motor m1(10, 7, 8);
Motor m2(9, 11, 12);
ComBus comm;

#define LED0     2
#define LED1     3
#define LED2     4
#define LED3     5

#define LIGNE_G  6
#define LIGNE_D  7


#define CMD_STOP    0
#define CMD_AVANCE  1
#define CMD_RECULE  2
#define CMD_DROITE  3
#define CMD_GAUCHE  4
#define CMD_MOTEURS 5

#define CMD_LIT_DISTANCE 10

#define CMD_DIGITAL_READ  20
#define CMD_DIGITAL_WRITE 21
#define CMD_ANALOG_READ   22
#define CMD_ANALOG_WRITE  23



void setup() {
  // Initialisation des moteurs
  m1.begin();
  m2.begin();
  // Active la patte STBY du TB6612
  pinMode(6, OUTPUT);
  digitalWrite(6, HIGH);
  
  // Initialisation de la communication
  comm.begin();
  // Configuration des pattes des LEDs
  pinMode(LED0, OUTPUT);
  pinMode(LED1, OUTPUT);
  pinMode(LED2, OUTPUT);
  pinMode(LED3, OUTPUT);
}

void loop() {
  int cmd;

  if (comm.newMessage() == true) {
    cmd = comm.readCmd();
    if (cmd == CMD_DIGITAL_READ) {
      comm.sendMessage( CMD_DIGITAL_READ, digitalRead( comm.readParam0() ) );
    }
    if (cmd == CMD_DIGITAL_WRITE) {
      digitalWrite( comm.readParam0(), comm.readParam1() );
    }
    if (cmd == CMD_ANALOG_READ) {
      comm.sendMessage( CMD_ANALOG_READ, analogRead( comm.readParam0() ) );
    }
	
    if(cmd == CMD_AVANCE) {
      m1.actuate(comm.readParam0());
      m2.actuate(comm.readParam0());
    }
    if(cmd == CMD_RECULE) {
      m1.actuate(-comm.readParam0());
      m2.actuate(-comm.readParam0());
    }
    if(cmd == CMD_GAUCHE) {
      m1.actuate(comm.readParam0());
      m2.actuate(-comm.readParam0());
    }
    if(cmd == CMD_DROITE) {
      m1.actuate(-comm.readParam0());
      m2.actuate(comm.readParam0());
    }
    if(cmd == CMD_STOP) {
      m1.actuate(0);
      m2.actuate(0);
    }
  }
}

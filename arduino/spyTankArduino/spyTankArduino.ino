#include <ComBus.h>
#include <motor.h>


Motor motA(9, 8, 7);
Motor motB(10, 11, 12);
ComBus comm;


#define CMD_AVANCE  1
#define CMD_RECULE  2
#define CMD_DROITE  3
#define CMD_GAUCHE  4
#define CMD_MOTEURS 5
#define CMD_STOP    6

#define CMD_DISTANCE 10

#define LED0 2
#define LED1 4
#define LED2 3
#define LED3 5
#define DISTANCE_PIN  17


#define CMD_DIGITAL_READ  20
#define CMD_DIGITAL_WRITE 21
#define CMD_ANALOG_READ   22
#define CMD_ANALOG_WRITE  23



void setup() {
  // Initialisation des moteurs
  motA.begin();
  motB.begin();
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
  pinMode(DISTANCE_PIN, INPUT);
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
    else if (cmd == CMD_ANALOG_READ) {
      comm.sendMessage( CMD_ANALOG_READ, analogRead( comm.readParam0() ) );
    }
    else if(cmd == CMD_AVANCE) {
      motA.changeVitesse(comm.readParam0());
      motB.changeVitesse(comm.readParam0());
    }
    else if(cmd == CMD_RECULE) {
      motA.changeVitesse(-comm.readParam0());
      motB.changeVitesse(-comm.readParam0());
    }
    else if(cmd == CMD_GAUCHE) {
      motA.changeVitesse(comm.readParam0());
      motB.changeVitesse(-comm.readParam0());
    }
    else if(cmd == CMD_DROITE) {
      motA.changeVitesse(-comm.readParam0());
      motB.changeVitesse(comm.readParam0());
    }
    else if(cmd == CMD_STOP) {
      motA.changeVitesse(0);
      motB.changeVitesse(0);
    }
    else if(cmd == CMD_MOTEURS) {
      motA.changeVitesse(comm.readParam0());
      motB.changeVitesse(comm.readParam1());
    }
    else if(cmd == CMD_DISTANCE) {
      comm.sendMessage( CMD_DISTANCE, distanceRead(1000) );    }
  }
}

unsigned long lastEnterTime = 0;
long _measureValue = 0;

long measure(unsigned long timeout) {
  long duration;
  
  if(millis() - lastEnterTime > 23) {
    lastEnterTime = millis();

    pinMode(DISTANCE_PIN, OUTPUT);
    digitalWrite(DISTANCE_PIN, LOW);
    delayMicroseconds(2);
    digitalWrite(DISTANCE_PIN, HIGH);
    delayMicroseconds(10);
    digitalWrite(DISTANCE_PIN, LOW);
    pinMode(DISTANCE_PIN, INPUT);
    duration = pulseIn(DISTANCE_PIN, HIGH, timeout);
    _measureValue = duration;
  }
  else {
    duration = _measureValue;
  }
  return(duration);
}


int distanceRead(unsigned int maxCm) {
  long distance;
  
  distance = measure(maxCm * 55 + 200);
    if(distance == 0) {
    distance = maxCm * 58;
  }
  return( (int)(distance / 58.0));
}

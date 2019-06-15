#include "motor.h"


Motor::Motor (int pwm_pin, int in1_pin, int in2_pin) :
  pwm_pin(pwm_pin), in1_pin(in1_pin), in2_pin(in2_pin) {
      _pwm_value = 0;
  }

void Motor::begin() {
  TCCR1B = TCCR1B & B11111000 | B00000001;    // set timer 1 divisor to     1 for PWM frequency of 31372.55 Hz
  pinMode(pwm_pin, OUTPUT);
  analogWrite(pwm_pin, 0);
  pinMode(in1_pin, OUTPUT);
  digitalWrite(in1_pin, 0);
  pinMode(in2_pin, OUTPUT);
  digitalWrite(in2_pin, 0);
}

/** stop Motor **/
void Motor::stop() {
  changeVitesse(0);
}

float Motor::vitesseRead() {
  return _pwm_value;
}

void Motor::changeVitesse(int vitesse) {
  // First we saturate the input value in the admissible range (-1 -> 1)
  if (vitesse < -255) {
    vitesse = -255;
  } else if (vitesse > 255) {
    vitesse = 255;
  }
  _pwm_value = vitesse;
  if (_pwm_value >=0) {
    analogWrite(pwm_pin, _pwm_value);
    digitalWrite(in1_pin, HIGH);
    digitalWrite(in2_pin, LOW);
  } else {
    analogWrite(pwm_pin, -_pwm_value);
    digitalWrite(in1_pin, LOW);
    digitalWrite(in2_pin, HIGH);
  }
}

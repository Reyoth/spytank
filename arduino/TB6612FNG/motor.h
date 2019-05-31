#ifndef Motor_H
#define Motor_H

#include <Arduino.h>

class Motor {
private:
  const int pwm_pin;         // pin on which to apply the PWM signal
  const int in1_pin;         // pin that dictates direction
  const int in2_pin;         // pin that dictates direction

  const int PWM_MAX = 255;
  const int PWM_MIN = PWM_MAX / 5; //if actuated, actuate at least for 20 %

  float _pwm_value; //pwm actuation value (between 0 and PWM_MAX)

public:
  /** Crée un objet 'moteur'.
   * Paramètres : 
   *   pwm_pin : numéro de la pin de l'arduino connectée à la pin PWMA/PWMB du TB6612NG
   *             ATTENTION : ce doit absolument être D9 ou D10 !!
   *   in1_pin : numéro de la pin de l'arduino connectée à la pin AIN1/Bin1 du TB6612NG
   *   in2_pin : numéro de la pin de l'arduino connectée à la pin AIN2/Bin2 du TB6612NG
   *             in1_pin et in2_pin peuvent valoir de 2 à 12. */  
  Motor (int pwm_pin, int in1_pin, int in2_pin);

  /** Initialise l'objet moteur. Cette fonction doit être appelée dans le setup du croquis.
   *  Le moteur est initialement à l'arrêt */
  void begin();

  /** Stoppe immédiatement le moteur */
  void halt();

  /** Modifie la commande appliquée au moteur.
   *  Le moteur est commandé en PWM (Pulse Width Modulation).
   *  La commande peut varier de -1 à 1, cette valeur représente la fraction de la tension
   *  d'alimentation du TB6612NG qui est appliquée au moteur.
   *  0 correspond à une tension nulle et 1 à la tension d'alimentation.
   *  Le signe de la commande définit le sens de rotation du moteur.
   *  Paramètre :
   *    pwm_value : commande à appliquer au moteur, peut varier de -1 à 1. */
  void actuate(float pwm_value);
  
  /** Renvoie la valeur de la commande actuellement appliquée au moteur 
   *  Retour : valeur de la commande, entre -1 et 1 */
  float getPwmValue();
};

#endif /* end of include guard Motor_H */

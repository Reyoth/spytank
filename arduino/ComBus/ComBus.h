#ifndef ComBus_H
#define ComBus_H

#include <Arduino.h>

#define ARDUINO_ADDR        8       // Adresse de l'Arduino sur le bus I2C


class ComBus {
private:
  uint8_t _cmd;
  int8_t _param0, _param1, _param2;
  uint8_t _id;
  int16_t _value;

public:
  /** Crée un objet bacarComm */
  ComBus ();

  /** Initialise la communication avec la RPi.
   *  Cette fonction doit être appelée dans setup(). */
  void begin(void);

  /** Vérifie si un nouveau message de la RPi a été reçu.
   *  Si oui, la commande et les 3 paramètres du message sont lus et sauvés
   *  dans des champs privés de l'objet.
   *  Retour :
   *    true si un nouveau message a été reçu, false sinon. */
  bool newMessage(void);

  /** Renvoie la commande du dernier message reçu */
  uint8_t readCmd(void);

  /** Renvoie le param0 du dernier message reçu */
  int8_t readParam0(void);

  /** Renvoie le param1 du dernier message reçu */
  int8_t readParam1(void);
    
  /** Renvoie le param2 du dernier message reçu */
  int8_t readParam2(void);

  /** Envoie un message à l RPi.
   *  Paramètres :
   *    . */
  void sendMessage(uint8_t id, int16_t value);
};

#endif /* end of include guard #ifndef ComBus_H */


#!/usr/bin/env python
from __future__ import print_function
from __future__ import division
# the above lines are meant for Python3 compatibility.
# they force the use of Python3 functionality for print()
# and the integer division
# mind your parentheses!

########################################################################
#
# Librairie des fonctions de communication entre la RPi et l'Arduino du
# SpyTank de la SmartFormation de FIJ
#
# History
# ------------------------------------------------
# Author	Date      		Comments
# M. Osee	07 Nov   18  	Creation, basee sur la librairie Gopigo
#
########################################################################


# comBus contient les fonctions de bas niveau pour utiliser le bus de
# communication entre la RPi et l'Arduino.
from comBus import *



########################################################################
# Definition des pattes utilisees de l'Arduino
########################################################################
# Pattes pour les LEDs
PIN_LED0 = 2
PIN_LED1 = 3
PIN_LED2 = 4
PIN_LED3 = 5
# Pattes des capteurs de ligne
PIN_CAPTEUR_DROIT  = 0
PIN_CAPTEUR_GAUCHE = 1


########################################################################
# Definition de l'identifiant des commandes
########################################################################
# Commandes de mouvements
CMD_STOP   = 0
CMD_AVANCE = 1
CMD_RECULE = 2
CMD_DROITE = 3
CMD_GAUCHE = 4
CMD_LIT_DISTANCE = 10
# Commandes generiques
CMD_DIGITAL_READ  = 20
CMD_DIGITAL_WRITE = 21
CMD_ANALOG_READ   = 22
CMD_ANALOG_WRITE  = 23




########################################################################
# Fonctions specifiques au SpyTank
########################################################################

# Determine l'etat du capteur de ligne gauche
#
# Parametres :
#   aucun
# Renvoie : 
#   1, si le capteur voit du "blanc"
#   0, si le capteur voit du "noir"
#  -1, si la communication a echoue  
def etatGauche():
    etat = litCapteurGauche()
    if etat > 300:
        return 1
    else if etat >=0:
        return 0
    else:
        return -1


# Determine l'etat du capteur de ligne droit
#
# Parametres :
#   aucun
# Renvoie : 
#   1, si le capteur voit du "blanc"
#   0, si le capteur voit du "noir"
#  -1, si la communication a echoue  
def etatGauche():
    etat = litCapteurDroit()
    if etat > 300:
        return 1
    else if etat >=0:
        return 0
    else:
        return -1


# commande l'etat d'une LED
#
# Parametres :
#   ledNum : identifiant de la LED sur laquelle on veut agir (0 -> 3)
#   ledEtat : nouvel etat a imposer a la LED (0 = eteinte, 1 = allumee)
# Renvoie : 
#   1, si l'ordre a bien ete envoye
#  -1, si la communication a echoue  
def led(ledNum, ledEtat):
    return digitalWrite(ledNum, ledEtat)


# fait avancer le SpyTank a une vitesse donnee
#
# Parametre :
#   vitesse : vitesse de rotation des moteurs (0 -> 255)
# Renvoie : 
#   1, si l'ordre a bien ete envoye
#  -1, si la communication a echoue  
def avance(vitesse):
    return sendCmd(CMD_AVANCE, vitesse)


# fait reculer le SpyTank a une vitesse donnee
#
# Parametre :
#   vitesse : vitesse de rotation des moteurs (0 -> 255)
# Renvoie : 
#   1, si l'ordre a bien ete envoye
#  -1, si la communication a echoue  
def recule(vitesse):
    return sendCmd(CMD_RECULE, vitesse)


# fait tourner le SpyTank a droite a une vitesse donnee
#
# Parametre :
#   vitesse : vitesse de rotation des moteurs (0 -> 255)
# Renvoie : 
#   1, si l'ordre a bien ete envoye
#  -1, si la communication a echoue  
def droite(vitesse):
    return sendCmd(CMD_DROITE, vitesse)


# fait tourner le SpyTank a gauche a une vitesse donnee
#
# Parametre :
#   vitesse : vitesse de rotation des moteurs (0 -> 255)
# Renvoie : 
#   1, si l'ordre a bien ete envoye
#  -1, si la communication a echoue  
def gauche(vitesse):
    return sendCmd(CMD_GAUCHE, vitesse)


# Stoppe le SpyTank
#
# Parametre :
#   aucun
# Renvoie : 
#   1, si l'ordre a bien ete envoye
#  -1, si la communication a echoue  
def stop():
    return sendCmd(CMD_STOP)


# impose separement les vitesses des deux moteurs du SpyTank
#
# Parametre :
#   vitesseGauche : vitesse de rotation du moteur gauche (-255 -> 255)
#   vitesseDroite : vitesse de rotation du moteur droit (-255 -> 255)
# Renvoie : 
#   1, si l'ordre a bien ete envoye
#  -1, si la communication a echoue 
def vitMoteurs(vitesseGauche, vitesseDroite)
    return sendCmd(CMD_MOTEURS, vitesseGauche, vitesseDroite)


# Lit la tension de sortie du capteur de ligne droit
#
# Parametre :
#   aucun
# Renvoie : 
#   la valeur lue sur le capteur (0 -> 1023), si la communication s'est bien passee
#  -1, si la communication a echoue  
def litCapteurDroit():
    return analogRead(PIN_CAPTEUR_DROIT)

# Lit la tension de sortie du capteur de ligne gauche
#
# Parametre :
#   aucun
# Renvoie : 
#   la valeur lue sur le capteur (0 -> 1023), si la communication s'est bien passee
#  -1, si la communication a echoue  
def litCapteurGauche():
    return analogRead(PIN_CAPTEUR_GAUCHE)


# Lit la tension de sortie du capteur de distance
#
# Parametre :
#   aucun
# Renvoie : 
#   la valeur lue sur le capteur (0 -> 1023), si la communication s'est bien passee
#  -1, si la communication a echoue  
def litDistance():
    sendCmd(CMD_LIT_DISTANCE)
    time.sleep(0.2)
    try:
        b1 = bus.read_byte(address)
        b0 = bus.read_byte(address)
    except IOError:
        return -1
    return b1*256 + b0



########################################################################
# Fonctions generiques
########################################################################


# ordonne à l'Arduino de lire la valeur d'une patte d'entree digitale
#
# Parametre :
#   digitalIn : identifiant de la patte a lire (0 -> 13)
# Renvoie : 
#   la valeur lue (0 -> 1), si la communication s'est bien passee
#  -1, si la communication a echoue  
def digitalRead(digitalIn):
    sendCmd(CMD_DIGITAL_READ, digitalIn)
    time.sleep(0.1)
    try:
        b = bus.read_byte(address)
    except IOError:
        return -1
    return b


# ordonne à l'Arduino d'imposer l'etat d'une patte de sortie digitale
#
# Parametres :
#   digitalOut : identifiant de la patte a modifier (0 -> 13)
#   etat : nouvel etat a imposer a la patte (0 = LOW, 1 = HIGH)
# Renvoie : 
#   1, si l'ordre a bien ete envoye
#  -1, si la communication a echoue  
def digitalWrite(digitalOut, etat):
    return sendCmd(CMD_DIGITAL_WRITE, digitalOut, etat)


# ordonne à l'Arduino de lire la valeur d'une patte d'entree analogique
#
# Parametre :
#   analogIn : identifiant de la patte a lire (0 -> 7)
# Renvoie : 
#   la valeur lue (0 -> 1023), si la communication s'est bien passee
#  -1, si la communication a echoue  
def analogRead(analogIn):
    sendCmd(CMD_ANALOG_READ, analogIn)
    time.sleep(0.1)
    try:
        b1 = bus.read_byte(address)
        b0 = bus.read_byte(address)
    except IOError:
        return -1
    return b1*256 + b0



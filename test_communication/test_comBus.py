#!/usr/bin/env python


import spytank
import time

for i in range(4):
    spytank.led(i, 1)
    time.sleep(0.25)
time.sleep(1)
for i in range(4):
    spytank.led(i, 0)
    time.sleep(0.25)

spytank.avance(150)
time.sleep(1)
spytank.stop()
time.sleep(1)
spytank.recule(150)
time.sleep(1)
spytank.stop()
time.sleep(1)
spytank.droite(150)
time.sleep(1)
spytank.stop()
time.sleep(1)
print(spytank.gauche(150))
time.sleep(1)
print(spytank.stop())
##time.sleep(1)

for i in range(1):
    print( "capteur gauche : " + str(spytank.litCapteurGauche()) )
    print( "capteur droit : " + str(spytank.litCapteurDroit()) )
    time.sleep(1)



#!/usr/bin/env python


#from gopigo import *
#import sys
from I2C_comm import *
import time

print "Avance"
for i in range(4):
    led(i,True)
    avance((i+1)*25);
    time.sleep(0.25)
for i in range(4):
    led(3-i, False)
    avance((3-i)*25);
    time.sleep(0.25)

print "Recule"
for i in range(4):
    led(i,True)
    recule((i+1)*25);
    time.sleep(0.25)
for i in range(4):
    led(3-i, False)
    recule((3-i)*25);
    time.sleep(0.25)

print "Droite"
for i in range(4):
    led(i,True)
    droite((i+1)*25);
    time.sleep(0.25)
for i in range(4):
    led(3-i, False)
    droite((3-i)*25);
    time.sleep(0.25)

print "Gauche"
for i in range(4):
    led(i,True)
    gauche((i+1)*25);
    time.sleep(0.25)
for i in range(4):
    led(3-i, False)
    gauche((3-i)*25);
    time.sleep(0.25)

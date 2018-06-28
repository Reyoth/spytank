#!/usr/bin/env python


from I2C_comm import *
import time

# Répète la séquence indéfiniment
while True:
    # Allume les LEDs une à une
    for i in range(4):
        led(i,True)
        time.sleep(1)
    # Eteint toutes les LEDs une à une
    for i in range(4):
        led(i,False)
        time.sleep(1)

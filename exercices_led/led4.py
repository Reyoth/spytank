#!/usr/bin/env python


from I2C_comm import *
import time

# Répète la séquence indéfiniment
while True:
    led(0, True)
    time.sleep(1)
    # Allume une seule LED à la fois, les unes après les autres
    for i in range(3):
        led(i,False)
        led(i,True)
        time.sleep(1)

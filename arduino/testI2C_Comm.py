#!/usr/bin/env python


#from gopigo import *
#import sys
from I2C_comm import *
import time

i = 0;
while True:
    for i in range(4):
        print "Acceleration"
        led(i,True)
        avance((i+1)*25);
        time.sleep(1)
       
    for i in range(4):
        print "Decelaration"
        led(3-i, False)
        avance((3-i)*25);
        time.sleep(1)

#!/usr/bin/env python

from gopigo import *
import sys


def led(ledNb, ledState):
    if ledNb == 0:
        if ledState == True:
            sendCmd(201)
        else:
            sendCmd(202)
    elif ledNb == 1:
        if ledState == True:
            sendCmd(203)
        else:
            sendCmd(204)
    elif ledNb == 2:
        if ledState == True:
            sendCmd(205)
        else:
            sendCmd(206)
    elif ledNb == 3:
        if ledState == True:
            sendCmd(207)
        else:
            sendCmd(208)


def avance(vitesse):
    sendCmd(motor_fwd_cmd[0], vitesse)

def recule(vitesse):
    sendCmd(motor_bwd_cmd[0], vitesse)

def droite(vitesse):
    sendCmd(right_rot_cmd[0], vitesse)

def gauche(vitesse):
    sendCmd(left_rot_cmd[0], vitesse)

def stop():
    sendCmd(stop_cmd)

	
def sendCmd(cmd, param1=0, param2=0, param3=0):
    #print([cmd, param1, param2, param3])
    write_i2c_block(address, [cmd, param1, param2, param3])

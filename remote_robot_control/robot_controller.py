#! /usr/bin/env python

from __future__ import print_function
from __future__ import division
from builtins import input
# the above lines are meant for Python3 compatibility.
# they force the use of Python3 functionality for print(), 
# the integer division and input()
# mind your parentheses!

import logging
import math
import time
try:
	import Queue as queue
except:
	import queue 
import threading
import gopigo
#--------------------------------------------------------------------------------------------------- 
debug=0
class RobotController:

	MAX_UPDATE_TIME_DIFF = 0.25
	TIME_BETWEEN_SERVO_SETTING_UPDATES = 1.0
	
	JOYSTICK_DEAD_ZONE = 0.1
	
	MOTION_COMMAND_TIMEOUT = 2.0 # If no commands for the motors are recieved in this time then
								 # the motors (drive and servo) are set to zero speed
	speed_l=200
	speed_r=200
	#-----------------------------------------------------------------------------------------------
	def __init__( self ):
		gopigo.set_speed(200)
		gopigo.stop()
		#gopigo.fwd()
		
		self.lastServoSettingsSendTime = 0.0
		self.lastUpdateTime = 0.0
		self.lastMotionCommandTime = time.time()
	
	#-----------------------------------------------------------------------------------------------
	def __del__( self ):
		
		self.disconnect()
	
	#-----------------------------------------------------------------------------------------------
	def disconnect( self ):
		print ("Closing")
	   
	def normaliseJoystickData( self, joystickX, joystickY ):
		stickVectorLength = math.sqrt( joystickX**2 + joystickY**2 )
		if stickVectorLength > 1.0:
			joystickX /= stickVectorLength
			joystickY /= stickVectorLength
		
		if stickVectorLength < self.JOYSTICK_DEAD_ZONE:
			joystickX = 0.0
			joystickY = 0.0
			
		return ( joystickX, joystickY )

	def centreNeck( self ):
		pass
	
	def setMotorJoystickPos( self, joystickX, joystickY ):
		joystickX, joystickY = self.normaliseJoystickData( joystickX, joystickY )
		if debug:
			print( "Left joy",joystickX, joystickY)
		
		#Tapez votre code ici.#####################################
		

















		
		#----------------------------------------------------------
		
	def setNeckJoystickPos( self, joystickX, joystickY ):
		joystickX, joystickY = self.normaliseJoystickData( joystickX, joystickY )
		if debug:	
			print ("Right joy",joystickX, joystickY)

	def update( self ):
		if debug:	
			print ("Updating")
		curTime = time.time()
		timeDiff = min( curTime - self.lastUpdateTime, self.MAX_UPDATE_TIME_DIFF )
		
		# Turn off the motors if we haven't received a motion command for a while
		#if curTime - self.lastMotionCommandTime > self.MOTION_COMMAND_TIMEOUT:
		#	self.leftMotorSpeed = 0.0
		#	self.rightMotorSpeed = 0.0
		#	self.panSpeed = 0.0
		#	self.tiltSpeed = 0.0

		self.lastUpdateTime = curTime

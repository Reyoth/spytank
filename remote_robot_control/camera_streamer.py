#!/usr/bin/env python

import copy
import os
import os.path
import subprocess
import time
import logging

#---------------------------------------------------------------------------------------------------
class CameraStreamer:
    
    """A class to look after streaming images from the Raspberry Pi camera.
       Ideally, the camera should only be on when somebody wants to stream images.
       Therefore, startStreaming must be called periodically. If startStreaming
       is not called before a timeout period expires then the streaming will stop"""

    DEFAULT_TIMEOUT = 4.0
    
    #-----------------------------------------------------------------------------------------------
    def __init__( self, timeout=DEFAULT_TIMEOUT ):
            
        self.cameraStreamerProcess = None
        self.streamingStartTime = 0
        self.streamingTimeout = timeout

    #-----------------------------------------------------------------------------------------------
    def __del__( self ):

        self.stopStreaming()
        
    #-----------------------------------------------------------------------------------------------
    def startStreaming( self ):
        
        # Start raspberry_pi_camera_streamer if needed
        if self.cameraStreamerProcess == None or self.cameraStreamerProcess.poll() != None:
            
            self.cameraStreamerProcess = subprocess.Popen( 
                [ "/usr/local/bin/raspberry_pi_camera_streamer" ] )
        
        self.streamingStartTime = time.time()         
                
    #-----------------------------------------------------------------------------------------------
    def update( self ):
        
        if time.time() - self.streamingStartTime > self.streamingTimeout:
            
            self.stopStreaming()
                
    #-----------------------------------------------------------------------------------------------
    def stopStreaming( self ):

        if self.cameraStreamerProcess != None:
            self.cameraStreamerProcess.terminate()

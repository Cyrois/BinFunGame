#!/usr/bin/python
from Buffer import Buffer
from collections import deque
from SDfile import SDfile
from Database import Database
from Display import Display

import web
import globalVars
import logging
import threading
import time
import sys, getopt

#initialize Buffer
def initBuffer():
    #Create the buffer
    location = raw_input('Please enter currect location of bin:')
    binBuffer = Buffer(location, "black", "green", "blue", "grey")
    time.sleep(10)
    
    #Clean buffer
    binBuffer.clear()
    binEmptyFlag = True
    
#Main
if __name__ == '__main__':
    #location to store files
    relativePath = "/home/pi/BinFunGame/src/TempFiles/"
	
    mainDeque = deque()
    
    #initialize Buffer, sdFile, database
    initBuffer()
    sdFile = SDfile(relativePath, location)
    db = Database("localhost", "bfg", "bfg123", "bfg")
    
    #Init global variables
    globalVars.init()

    #Start display thread
    displayThread = threading.Thread(target=Display.startDisplay)
    displayThread.start()
    
    while True:
        if binBuffer.getEmptyFlag() == False:
            #Empty buffer queue 
            mainDeque = binBuffer.flushBuffer()

            #Update global count values
            globalVars.blackCount = binBuffer.getCount("black")
            globalVars.greenCount = binBuffer.getCount("green")
            globalVars.blueCount = binBuffer.getCount("blue")
            globalVars.greyCount = binBuffer.getCount("grey")

            #send signal to SD to save
            sdFile.quickAppendBuffer(mainDeque)
            db.insertBuffer(mainDeque)

        #check Queues
        binBuffer.listenQueues()

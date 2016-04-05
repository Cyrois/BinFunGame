#!/usr/bin/python
from Buffer import Buffer
from collections import deque
from SDfile import SDfile
import datetime
from Database import Database


from Display import Display
import web
import globalVars
import logging
import threading
import time
import sys, getopt

if __name__ == '__main__':
    #location to store files
    relativePath = "/home/pi/BinFunGame/src/TempFiles/"
    
    mainDeque = deque()
    
    #Init buffer
    location = raw_input('Please enter currect location of bin:')
    #location = str(main(sys.argv[1:]))
    binBuffer = Buffer(location, "black", "green", "blue", "grey")
    time.sleep(10)
    
    #Clean buffer
    binBuffer.clear()
    
    binEmptyFlag = True
    
    #Init sdFile
    #headers = "ID,Location,Date,Time"
    sdFile = SDfile(relativePath, location)
    
    #Init global variables
    globalVars.init()
    
    while True:
        #if there is something in the buffer then update the count values of all the bin colours
        #then store all the signal data to the local SD card as well as attempt to store in a remote database
        if binBuffer.getEmptyFlag() == False:
            mainDeque = binBuffer.flushBuffer()

            #print "Sending signal to Display "
            #print binBuffer.getCount("black")
            #print binBuffer.getCount("green")
            #print binBuffer.getCount("blue")
            #print binBuffer.getCount("grey")

            #Update global count values
            globalVars.blackCount = binBuffer.getCount("black")
            globalVars.greenCount = binBuffer.getCount("green")
            globalVars.blueCount = binBuffer.getCount("blue")
            globalVars.greyCount = binBuffer.getCount("grey")
            
            #print "Sending signal to SD to save "
            sdFile.quickAppendBuffer(mainDeque)

            #inserts the buffer to database, and the count values to update the display
            try:
                db = Database("54.218.32.132", "bfguser", "bfg123", "bfg")
                db.updateDatabase(mainDeque, globalVars.blackCount, globalVars.greenCount, globalVars.blueCount, globalVars.greyCount)
                db.turnOff()
            except:
               print "could not connect to DB"

            #empty the buffer
            binBuffer.clear()

    #Test buffer
        #test = raw_input ("Enter stuff in deque: ")
        #color = raw_input ("Enter color: ")
        #binBuffer.simulateQueue(test,color)
        
        binBuffer.listenQueues()

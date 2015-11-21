#!/usr/bin/python
from Buffer import Buffer
from collections import deque
from SDfile import SDfile
import datetime


from display import Display
from display import web
from display import globalVars
import logging
import threading
import time


if __name__ == '__main__':
    
    mainDeque = deque()
    
    #Init buffer
    location = raw_input('Please enter currect location of bin:')
    binBuffer = Buffer(location,1,2,3,4)
    
    
    #Clean buffer
    binBuffer.flushBuffer()
    
    binEmptyFlag = True
    
    #Init sdFile
    headers = "ID,Location,Date,Time"
    sdFile = SDfile("./TempFiles/" + str(datetime.date.today()) + ".csv")
    sdFile.quickInit(headers)
    
    #Init global variables
    globalVars.init()

    #Start display thread
    displayThread = threading.Thread(target=Display.startDisplay)
    displayThread.start()
    
    while True:
        if binBuffer.getEmptyFlag() == False:
            mainDeque = binBuffer.flushBuffer()
            #Buffer queue should be empty
            print "Sending signal to Display "
            #Update global count values
            print binBuffer.getCount("black")
            globalVars.blackCount = binBuffer.getCount("black")
            print binBuffer.getCount("green")
            globalVars.greenCount = binBuffer.getCount("green")
            print binBuffer.getCount("blue")
            globalVars.blueCount = binBuffer.getCount("blue")
            print binBuffer.getCount("grey")
            globalVars.greyCount = binBuffer.getCount("grey")
            print "Sending signal to SD to save "
            sdFile.quickAppendBuffer(mainDeque)
            #print "quickRead: " + str(sdFile.quickRead())
    
    #Test buffer
        #test = raw_input ("Enter stuff in deque: ")
        #color = raw_input ("Enter color: ")
        #binBuffer.simulateQueue(test,color)
        
        binBuffer.listenQueues()

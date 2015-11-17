#!/usr/bin/python
from Buffer import Buffer
from collections import deque
from SDfile import SDfile
import datetime
import time

if __name__ == '__main__':
    #location to store files
    relativePath = "./TempFiles/"
	
    mainDeque = deque()
    
    #Init buffer
    location = raw_input('Please enter currect location of bin:')
    binBuffer = Buffer(location,1,2,3,4)
    
    
    #Clean buffer
    binBuffer.flushBuffer()
    
    binEmptyFlag = True
	
    #Init sdFile
    headers = "ID,Location,Date,Time"
    sdFile = SDfile(relativePath, location)
    sdFile.quickInit(headers)
    
    while True:
        if binBuffer.getEmptyFlag() == False:
            mainDeque = binBuffer.flushBuffer()
            #Buffer queue should be empty
            print "Sending signal to Display "
            print binBuffer.getCount("black")
            print binBuffer.getCount("green")
            print binBuffer.getCount("blue")
            print binBuffer.getCount("grey")
            print "Sending signal to SD to save "
            sdFile.quickAppendBuffer(mainDeque)
            date = time.strftime("%d_%m_%Y") #get current date
            filePath = relativePath + date + "_" + location + "_" + color + ".csv"
            #print "quickRead: " + str(sdFile.quickRead(filePath))
    
    #Test buffer
        test = raw_input ("Enter stuff in deque: ")
        color = raw_input ("Enter color: ")
        binBuffer.simulateQueue(test,color)
        
        binBuffer.listenQueues()

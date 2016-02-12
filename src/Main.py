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
"""
def main(argv):
    location = ''
    try:
       opts, args = getopt.getopt(argv,"hl:",["location="])
    except getopt.GetoptError:
       print 'Main.py -l <location>'
       sys.exit(2)
    for opt, arg in opts:
       if opt == '-h':
         print 'Main.py -l <location>'
         sys.exit()
       elif opt in ("-l", "--location"):
         location = arg

    print 'Bin Location is: ', location
"""
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
    #sdFile.quickInit(headers)

    #Init database
    #db = Database("54.218.32.132", "bfguser", "bfg123", "bfg")
    
    #Init global variables
    globalVars.init()

    #Start display thread
    #displayThread = threading.Thread(target=Display.startDisplay)
    #displayThread.start()
    
    while True:
        if binBuffer.getEmptyFlag() == False:
            mainDeque = binBuffer.flushBuffer()
            #Buffer queue should be empty
            #print "Sending signal to Display "
            #Update global count values
            print binBuffer.getCount("black")
            globalVars.blackCount = binBuffer.getCount("black")
            print binBuffer.getCount("green")
            globalVars.greenCount = binBuffer.getCount("green")
            print binBuffer.getCount("blue")
            globalVars.blueCount = binBuffer.getCount("blue")
            print binBuffer.getCount("grey")
            globalVars.greyCount = binBuffer.getCount("grey")
            #print "Sending signal to SD to save "
            sdFile.quickAppendBuffer(mainDeque)
            #inserts the buffer to database, and the count values to update the display
            #print "calling update database"
            db = Database("54.218.32.132", "bfguser", "bfg123", "bfg")
            db.updateDatabase(mainDeque, globalVars.blackCount, globalVars.greenCount, globalVars.blueCount, globalVars.greyCount)
            db.turnOff()
			
            #date = time.strftime("%d_%m_%Y") #get current date
            #filePath = relativePath + date + "_" + location + "_" + color + ".csv"
            #print "quickRead: " + str(sdFile.quickRead(filePath))
    
    #Test buffer
        #test = raw_input ("Enter stuff in deque: ")
        #color = raw_input ("Enter color: ")
        #binBuffer.simulateQueue(test,color)
        
        binBuffer.listenQueues()

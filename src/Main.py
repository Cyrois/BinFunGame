#!/usr/bin/python
from Buffer import Buffer
from collections import deque

if __name__ == '__main__':
    
    #Init buffer
    location = raw_input('Please enter currect location of bin:')
    binBuffer = Buffer(location,1,2,3,4)
    mainDeque = deque()
    binBuffer.flushQueue()
    binBuffer.initQueue()
    binEmptyFlag = True
    
    while True:
        if binEmptyFlag == False:
            mainDeque = binBuffer.flushQueue()
            #Buffer queue should be empty
            print "Sending signal to Display "
            print binBuffer.getCount("black")
            print binBuffer.getCount("green")
            print binBuffer.getCount("blue")
            print binBuffer.getCount("grey")
            print "Sending signal to SD to save "
            print mainDeque
        binBuffer.roundRobinCheck()
        binEmptyFlag = binBuffer.getEmptyFlag()
        
        test = raw_input ("Enter stuff in deque: ")
        color = raw_input ("Enter color: ")
        binBuffer.simulateQueue(test,color)
    
    
    """
        roundrobincheck
        if (new value of count)
        return mainSignal
        return nothing
        """
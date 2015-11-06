#!/usr/bin/python
from collections import deque

class Buffer:
    'This our buffer'
    """
        Gets deque from queue class, increments count values by checking length of deque, signals Main with updated bin values and bin
        When recieved new deque, append all deques together. Once main calls flushTable, dump queue to main
        Init queues and round robin them.
        
        Main execs roundrobin(since no threads), roundRobin should return with a new deque and dumps every round
    """
    #Count Values for each bin
    __blackCount = 0
    __greenCount = 0
    __blueCount = 0
    __greyCount = 0

    #Unique IDs for the 4 bins
    __blackID = -1
    __greenID = -1
    __blueID = -1
    __greyID = -1
    #Main deque
    bufferDeque = deque()
   
   #Simulate for Queue class
    blackDeque = deque("a")
    greenDeque = deque("bc")
    blueDeque = deque("defg")
    greyDeque = deque("hi")
    
# Manual input for location and IDs
    def __init__(self,location,blackID,greenID,blueID,greyID):
        self.location = location
        self.blackID = blackID
        self.greenID = greenID
        self.blueID = blueID
        self.greyID = greyID

# Break down struct of signal for count
    def parseSignal(self,color,signalDeque):
    #Increment Count
        self.incrementCount(color,signalDeque)
    #Append Deques
        self.appendToBufDeq(signalDeque)
    #Send desired count value

    
#   def signalMain():
    def getCount(self,color):
        if color == "black":
            return self.__blackCount
        elif color == "green":
            return self.__greenCount
        elif color == "blue":
            return self.__blueCount
        elif color == "grey":
            return self.__greyCount
        else :
            print "Error: Not a color"

    def incrementCount(self, color, deque):
        if color == "black":
            self.__blackCount += len(deque)
        elif color == "green":
            self.__greenCount += len(deque)
        elif color == "blue":
            self.__blueCount += len(deque)
        elif color == "grey":
            self.__greyCount += len(deque)
        else :
            print "Error: Not a color"

    def appendToBufDeq(self,signalDeque):
        for elem in range(0,len(signalDeque)):
            self.bufferDeque.append(signalDeque.popleft())

    def flushTable(self):
        newDeque = deque(self.bufferDeque)
        self.bufferDeque.clear()
        return newDeque

#    def initQueue(self):

    def roundRobinCheck(self):
    #Check black port
        #self.blackDeque = black.flushQueue()
        if len(self.blackDeque) != 0:
            self.parseSignal("black",self.blackDeque)
        #self.blackDeque.clear()
    #Check green port
        #greenDeque = green.flushQueue()
        if len(self.greenDeque) != 0:
            self.parseSignal("green",self.greenDeque)
        #self.greenDeque.clear()
    #Check blue port
        #blueDeque = blue.flushQueue()
        if len(self.blueDeque) != 0:
            self.parseSignal("blue",self.blueDeque)
        #self.blueDeque.clear()
    #Check grey port
        #greyDeque = grey.flushQueue()
        if len(self.greyDeque) != 0:
            self.parseSignal("grey",self.greyDeque)
        #self.greyDeque.clear()


#   def pullTable():







#!/usr/bin/python
from collections import deque
from Queue import Queue

class Buffer:
    'This our buffer'
    """
        Gets deque from queue class, increments count values by checking length of deque, signals Main with updated bin values and bin
        When recieved new deque, append all deques together. Once main calls flushQueue, dump queue to main
        Init queues and round robin them.
        
        Main execs roundrobin(since no threads), roundRobin should return with a new deque and dumps every round
    """
    #Count Values for each bin
    __blackCount = 0
    __greenCount = 0
    __blueCount = 0
    __greyCount = 0
    
    #Location of Bin
    __location = None
    #Unique IDs for the 4 bins
    __blackID = None
    __greenID = None
    __blueID = None
    __greyID = None
    
    #Empty flag
    __isEmpty = True
    #Main deque
    __bufferDeque = deque()
    
    #Queues
    __blackQueue = None
    __greenQueue = None
    __blueQueue = None
    __greyQueue = None
    
# Manual input for location and IDs
    def __init__(self,location,blackID,greenID,blueID,greyID):
        self.__location = location
        self.__blackID = blackID
        self.__greenID = greenID
        self.__blueID = blueID
        self.__greyID = greyID
    
    def initQueue(self):
        self.__blackQueue = Queue(self.__location,self.__blackID)
        self.__greenQueue = Queue(self.__location,self.__greenID)
        self.__blueQueue = Queue(self.__location,self.__blueID)
        self.__greyQueue = Queue(self.__location,self.__greyID)
    
    def getEmptyFlag(self):
        return self.__isEmpty
    
    def setEmptyFlag(self,empty):
        self.__isEmpty  = empty
    
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
    
    #Sets flag if there is something in bufferDeque or not
    def listenQueues(self):
        if len(self.__bufferDeque) > 0:
            print "Error: Flush buffer queue first!"
        #Check black queue
        if (self.__blackQueue.getEmptyFlag() == False) :
            self.appendSignal("black",self.__blackQueue.flushQueue())
        #Check green queue
        if (self.__greenQueue.getEmptyFlag() == False) :
            self.appendSignal("green",self.__greenQueue.flushQueue())
        #Check blue queue
        if (self.__blueQueue.getEmptyFlag() == False) :
            self.appendSignal("blue",self.__blueQueue.flushQueue())
        #Check grey queue
        if (self.__greyQueue.getEmptyFlag() == False) :
            self.appendSignal("grey",self.__greyQueue.flushQueue())
        if len(self.__bufferDeque) > 0:
            print "Buffer has something!"
            self.setEmptyFlag(False)
        else:
            self.setEmptyFlag(True)
            print  "Buffer has nothing!"

    #updates mainDeque and bin count values
    def appendSignal(self,color,signalDeque):
        #Increment Count
        self.incrementCount(color,signalDeque)
        #Append Deques
        self.appendToBufDeq(signalDeque)
    
    #update bin count value based on length of deque, or length of queue
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

    #appends the queueDeque to main Deque
    def appendToBufDeq(self,signalDeque):
        for elem in range(0,len(signalDeque)):
            self.__bufferDeque.append(signalDeque.popleft())

    def flushBuffer(self):
        newDeque = deque(self.__bufferDeque)
        self.__bufferDeque.clear()
        self.setEmptyFlag(True)
        return newDeque


#Testing Buffer
    def simulateQueue(self, simulateDeque,color):
        if color == "black":
            self.__blackQueue.push(simulateDeque)
            self.__blackQueue.setEmptyFlag(False)
        elif color == "green":
            self.__greenQueue.push(simulateDeque)
            self.__greenQueue.setEmptyFlag(False)
        elif color == "blue":
            self.__blueQueue.push(simulateDeque)
            self.__blueQueue.setEmptyFlag(False)
        elif color == "grey":
            self.__greyQueue.push(simulateDeque)
            self.__greyQueue.setEmptyFlag(False)
        else :
            print "Error: Not a color"

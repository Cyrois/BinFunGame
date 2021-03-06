#!/usr/bin/python
from collections import deque
from BFG_Queue import BFG_Queue

class Buffer:
    'This our buffer'
    
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
        self.initQueue()

    def initQueue(self):
        self.__blackQueue = BFG_Queue(self.__location,self.__blackID)
        self.__greenQueue = BFG_Queue(self.__location,self.__greenID)
        self.__blueQueue = BFG_Queue(self.__location,self.__blueID)
        self.__greyQueue = BFG_Queue(self.__location,self.__greyID)
    
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
            self.appendQueue("black",self.__blackQueue.flushQueue())
        #Check green queue
        if (self.__greenQueue.getEmptyFlag() == False) :
            self.appendQueue("green",self.__greenQueue.flushQueue())
        #Check blue queue
        if (self.__blueQueue.getEmptyFlag() == False) :
            self.appendQueue("blue",self.__blueQueue.flushQueue())
        #Check grey queue
        if (self.__greyQueue.getEmptyFlag() == False) :
            self.appendQueue("grey",self.__greyQueue.flushQueue())
        if len(self.__bufferDeque) > 0:
            #print "Buffer has something!"
            self.setEmptyFlag(False)
        else:
            #print  "Buffer has nothing!"
            self.setEmptyFlag(True)

    #updates mainDeque and bin count values
    def appendQueue(self,color,queueDeque):
        #Increment Count
        self.incrementCount(color,queueDeque)
        #Append Deques
        self.appendToBufDeq(queueDeque)
    
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
    def appendToBufDeq(self,queueDeque):
        for elem in range(0,len(queueDeque)):
            self.__bufferDeque.append(queueDeque.popleft())

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

    def clear(self):
        self.__bufferDeque.clear()
        self.setEmptyFlag(True)

#!/usr/bin/python
from collections import deque

class Buffer:
    'This our buffer'
    """
        Gets deque from queue class, increments count values by checking length of deque, signals Main with updated bin values and bin
        When recieved new deque, append all deques together. Once main calls flushTable, dump queue to main
        Init queues and round robin them.
    """
    __blackCount = 0
    __greenCount = 0
    __blueCount = 0
    __greyCount = 0

    #Unique IDs for the 4 bins
    __blackID = -1
    __greenID = -1
    __blueID = -1
    __greyID = -1
    

# Manual input for location and IDs
    def __init__(self,location,blackID,greenID,blueID,greyID):
        self.location = location
        self.blackID = blackID
        self.greenID = greenID
        self.blueID = blueID
        self.greyID = greyID

# Break down struct of signal for count
#   def parseSignal(Signal):
    #Increment Count
    #Signal Main
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
            print "Error: Not color"

    def incrementCount(self, color):
        if color == "black":
            self.__blackCount += 1
        elif color == "green":
            self.__greenCount += 1
        elif color == "blue":
            self.__blueCount += 1
        elif color == "grey":
            self.__greyCount += 1
        else :
            print "Error: Not color"
    
    
#   def flushTable():
#   def initQueue():
#   def roundRobinCheck():
#   def pullTable():

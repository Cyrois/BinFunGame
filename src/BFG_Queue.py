from collections import deque
from Sensor import Sensor

class BFG_Queue:
    __queue = deque() #internal data structure being used
    __isEmpty = True
    __location =  None #corresponds to the location of the recycling station
    __ID = None #corresponds to the bin colour that the sensor is placed in
    __signal = None
    __sensor = -1
    
    #constructor to set all of the class variables accordingly
    #the sensor for the bin colour will be attached to this queue
    def __init__(self,location,ID):
        print "initializing queue"
        self.__location = location
        self.__ID = ID
        self.__sensor = Sensor(ID, location)

    #push an item onto the end of the deque, set the flag indicating that the queue is not empty
    def push(self, Signal):
        #print "pushing: " + Signal
        self.__queue.append(Signal)
        self.setEmptyFlag(False)
            
    #take all of the items out of the queue and set the empty flag to true, used by the buffer class
    def flushQueue(self):
        newDeque = deque()
        for signal in self.__queue:
            newDeque.append(signal)
        self.__queue.clear()
        self.setEmptyFlag(True)
        return newDeque
        
    #used for testing purposes to print the current items in the queue
    def printQueue(self):
        for signal in self.__queue:
            print signal

    #set the empty flag to the given value
    def setEmptyFlag(self, empty):
        self.__isEmpty = empty

    #check if the sensor attached to this queue has detected a signal recently
    #if the sensor has, then take the data from the sensor and set the sensor class to be empty
    def getEmptyFlag(self):
        if not self.__sensor.isEmpty():
            self.push(self.__sensor.getSignal())
            self.setEmptyFlag(False)
        return self.__isEmpty




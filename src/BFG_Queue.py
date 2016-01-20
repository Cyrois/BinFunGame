from collections import deque
from Sensor import Sensor

class BFG_Queue:
    __queue = deque()
    __isEmpty = True    #Flag to check if Queue is empty 
    __Location =  None  #Location of the bin               
    __sensor = -1       #The sensor that the Queue belongs to 
    
    #initialize the Queue location and sensor 
    def __init__(self, Location, ID):
        self.__Location = Location
        self.__sensor = Sensor(ID, Location)

    #NOTE : do we need this?
    def push(self, Signal):
        self.__queue.append(Signal)
        self.setEmptyFlag(False)
                 
    def flushQueue(self):
        print "flush queue"
        newDeque = deque()
        for signal in self.__queue:
            newDeque.append(signal)
        self.__queue.clear()
        self.setEmptyFlag(True)
        return newDeque
        
    def printQueue(self):
        for signal in self.__queue:
            print signal

    def setEmptyFlag(self, empty):
        self.__isEmpty = empty

    #doing queue things    
    def getEmptyFlag(self):
        #NOTE : listenSignal was empty, what is this supposed to do?
        #self.__sensor.listenSignal()

        if not self.__sensor.isEmpty():
            self.push(self.__sensor.getSignal())
            self.setEmptyFlag(False)
            
        return self.__isEmpty
    
    def initSensor(self):
        __sensor = Sensor()




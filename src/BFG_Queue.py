from collections import deque
from Sensor import Sensor

class BFG_Queue:
    __queue = deque()
    __isEmpty = True
    __location =  None
    __ID = None
    __signal = None
    __sensor = -1
    
    def __init__(self,location,ID):
        print "initializing queue"
        self.__location = location
        self.__ID = ID
        self.__sensor = Sensor(ID, location)

    def push(self, Signal):
        print "pushing: " + Signal
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
        self.__sensor.listenSignal()
        
        if not self.__sensor.isEmpty():
            self.push(self.__sensor.getSignal())
            self.setEmptyFlag(False)
            
        return self.__isEmpty
    
    def initSensor(self):
        __sensor = Sensor()




from collections import deque
from Signal import Signal

class Queue:
    __queue = deque()
    __isEmpty = True
    __location =  None
    __ID = None
    __signal = None
    
    def __init__(self,location,ID):
        print "initializing queue"
        self.__location = location
        self.__ID = ID
                 
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
        
    def getEmptyFlag(self):
        return self.__isEmpty
    
    def initSensor(self):
        __signal = Signal()




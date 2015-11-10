from collections import deque

class Queue:
    __queue = deque()
    __isEmpty = None
    
    def __init__(self):
        print "initializing queue"
                 
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


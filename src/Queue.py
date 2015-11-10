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
        queue = self.__queue.copy()
        self.__queue.clear()
        self.setEmptyFlag(True)
        return queue
        
    def printQueue(queue):
        for signal in queue:
            print signal

    def setEmptyFlag(self, empty):
        self.__isEmpty = empty
        
    def getEmptyFlag(self):
        return self.__isEmpty
        
if __name__ == '__main__':
    print "testing"
    test = Queue()
    test.push("1")
    test.push("2")
    test.push("3")
    Queue.printQueue(test)
    
    newTest = test.flushQueue()
    Queue.printQueue(newTest)
    
    print("something")
    wait = input("PRESS ENTER TO CONTINUE.")
    print("something")

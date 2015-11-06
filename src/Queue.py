from collections import deque

class Queue:
    __queue = deque()
    test = deque(["a", "b", "c"])
    
    def __init__(self):
        print "init"
                 
    def push(self, Signal):
        print "pushing: " + Signal
        self.__queue.append(Signal)
                 
    def flushQueue(self):
        print "flush queue"
        #print test.queue
        #list(test)
        #for signal in test.queue:
         #   print signal
        #for signal in iter(self.get, self.test):
         #   print test.pop
        for signal in self.__queue:
            print signal
if __name__ == '__main__':
    print "testing"
    test = Queue()
    test.push("1")
    test.push("2")
    test.push("3")
    test.flushQueue()

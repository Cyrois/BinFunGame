#!/usr/bin/python

class Buffer:
    'This our buffer'
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
            return self.__blueCount
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


#   def pullTable():



if __name__ == '__main__':
    buf1 = Buffer("Nest 3rd Floor",1,2,3,4)
    print buf1.location
    print Buffer.__doc__
    print buf1.getCount("blue")
    for i in range(0,10):
         buf1.incrementCount("blue")
    print buf1.getCount("blue")



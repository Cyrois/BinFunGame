class Signal:
    #delimiter for the strings
    delim = ","
    
    #formats the given values to a string delimited by commas
    @classmethod
    def initializeSignal(self, ID, location, dateTime):
        signal = ''
        signal += str(ID) + self.delim + location + self.delim + str(dateTime)
        return signal

    #splits the given signal by the comma delimiter, returns a list
    @classmethod
    def parseSignal(self, signal):
        return signal.split(self.delim)


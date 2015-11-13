class Signal:
    #delimiter for the strings
    delim = ","
    
    #formats the given values to a string delimited by commas
    def initializeSignal(self, ID, location, dateTime):
        return ID + self.delim + location + self.delim + dateTime

    #splits the given signal by the comma delimiter, returns a list
    def parseSignal(signal):
        return signal.split(self.delim)


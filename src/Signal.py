class Signal:
    delim = ","
    
    #formats the given values to a string delimited by commas
    def initializeSignal(ID, location, dateTime):
        return ID + delim + location + delim + dateTime

    #splits the given signal by the comma delimiter, returns a list
    def parseSignal(signal):
        return signal.split(delim)


class Signal:
    def initializeSignal(ID, location, dateTime):
        return ID + "," + location + "," + dateTime

    def parseSignal(signal):
        return signal.split(',')


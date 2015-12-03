from Signal import Signal
import os
import datetime

def test_initializeSignal():
    dateTime = datetime.datetime.utcnow()
    testSignal = Signal.initializeSignal("green","Nest",dateTime)
    assert testSignal == ("green,Nest," + str(dateTime))

def test_parseSignal():
    dateTime = datetime.datetime.utcnow()
    testSignal = Signal.initializeSignal("green","Nest",dateTime)
    expectedSignal = ("green,Nest," + str(dateTime)).split(Signal.delim)
    assert Signal.parseSignal(testSignal) == expectedSignal




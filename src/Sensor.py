import RPi.GPIO as GPIO
import datetime
import Queue

class Sensor:
    __isEmpty = None
    __signal = ""
    __ID = ""
    __Location = ""
        
    #GPIO Input Pin for the Sensor
    __gpiopin = -1

    #set up GPIO
    def __init__(self, int, ID, Location):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        self.gpiopin = int
        GPIO.setup(self.gpiopin, GPIO.IN)
        self.__ID = ID
        self.__Location = Location

    #wait for sensor to turn on
    def listenSignal(self):
        while True:
            GPIO.wait_for_edge(self.gpiopin, GPIO.RISING)
            self.sendSignal()

    #refactor into signal class to parse and initialize signal
    def sendSignal(self):           
        #send date, time and id
        #need to send to queue instead 
        print datetime.datetime.utcnow()
        self.__signal = self.initializeSignal()
        self.setEmptyFlag(False)

    def initializeSignal(self):
        return self.__ID + "," + self.__Location + "," + datetime.datetime.utcnow()
        
    def setEmptyFlag(self, empty):
        self.__isEmpty = empty
        
    def getEmptyFlag(self):
        return self.__isEmpty




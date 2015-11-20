import RPi.GPIO as GPIO
import datetime
import Queue
from Signal import Signal

class Sensor:
    __isEmpty = None    #flag used by Queue to see if the Sensor is active
    __signal = ""   #the current Signal string, see Signal class for format
    __ID = ""   #the sensor ID
    __Location = "" #the location of the sensor
        
    #GPIO Input Pin for the Sensor
    __gpiopin = 11

    #set up GPIO
    def __init__(self, ID, Location):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        self.__gpiopin = self.getGPIOPin(ID)
        GPIO.setup(self.__gpiopin, GPIO.IN)
        self.__ID = ID
        self.__Location = Location
      #  GPIO.add_event_detect(self.__gpiopin, GPIO.RISING, callback=testSendSignal)

    #def testSendSignal():
     #   print 'testing the print signal callback'

    def getGPIOPin(self, ID):
        if ID == 1:
            return 11
        elif ID == 2:
            return 12
        elif ID == 3:
            return 18;
        elif ID == 4:
            return 7
        else:
            return 0

    #wait for sensor to turn on
    def listenSignal(self):
        if(GPIO.input(self.__gpiopin)):
            self.sendSignal()
        #while True:
         #   GPIO.wait_for_edge(self.gpiopin, GPIO.RISING)
          #  self.sendSignal()

    #refactor into signal class to parse and initialize signal
    def sendSignal(self):           
        #send date, time and id
        #need to send to queue instead 
        dateTime = datetime.datetime.utcnow()
        print dateTime
        self.__signal = Signal.initializeSignal(self.__ID, self.__Location, dateTime)
        self.setEmptyFlag(False)

    #sets the empty flag to the given empty variable, used by Queue class
    def setEmptyFlag(self, empty):
        self.__isEmpty = empty
        
    #returns the empty flag, used by Queue class    
    def isEmpty(self):
        return self.__isEmpty

    def getSignal(self):
        self.setEmptyFlag(True)
        return self.__signal

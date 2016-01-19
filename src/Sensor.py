import RPi.GPIO as GPIO
import datetime
import Queue
import time
from Signal import Signal

class Sensor:
    __isEmpty = True    #Flag used by Queue to see if the Sensor is active
    __signal = ''       #The current Signal string, see Signal class for format
    __ID = ''           #Sensor ID
    __Location = ''     #The location of the sensor  
    __gpiopin = 0       #GPIO Input Pin for the Sensor

    #set up GPIO
    def __init__(self, ID, Location):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        self.__ID = ID
        self.__Location = Location
        self.__gpiopin = self.getGPIOPin(ID)
        GPIO.setup(self.__gpiopin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        #sendSignal is called when sensor is activated
        GPIO.add_event_detect(self.__gpiopin, GPIO.RISING, callback=self.sendSignal)

    def getGPIOPin(self, ID):
        if ID is "black":
            return 12
        elif ID is "green":
            return 7
        elif ID is "blue":
            return 16
        elif ID is "grey":
            return 11
        else:
            return 0

    #calls Signal class to initialize signal 
    def sendSignal(self):       
        date = datetime.datetime.utcnow()
        self.__signal = Signal.initializeSignal(self.__ID, self.__Location, date)
        self.setEmptyFlag(False)

    #sets the empty flag to the given empty variable, used by Queue class
    def setEmptyFlag(self, empty):
        self.__isEmpty = empty
        
    #returns the empty flag, used by Queue class    
    def isEmpty(self):
        return self.__isEmpty

    #returns signal
    def getSignal(self):
        self.setEmptyFlag(True)
        return self.__signal
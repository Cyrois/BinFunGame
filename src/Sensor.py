import RPi.GPIO as GPIO
import datetime
import Queue
import time
from Signal import Signal

class Sensor:
    __isEmpty = True    #flag used by Queue to see if the Sensor is active
    __signal = ''   #the current Signal string, see Signal class for format
    __ID = ''   #the sensor ID, corresponds to the colour
    __Location = '' #the location of the sensor/recycling station
        
    #GPIO Input Pin for the Sensor
    __gpiopin1 = 7
    __gpiopin2 = 7
    __timestamp = ''

    #set up GPIO
    #constructor to set all the class flags accordingly
    def __init__(self, ID, Location):
        self.__ID = ID
        self.__Location = Location
        self.setGPIOPin(ID)

        #setup the GPIO pins
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        
	self.__timestamp = datetime.datetime.now()
    
        GPIO.setup(self.__gpiopin1, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.__gpiopin2, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(self.__gpiopin1, GPIO.RISING, callback=self.sendSignal)
        GPIO.add_event_detect(self.__gpiopin2, GPIO.RISING, callback=self.sendSignal)

    #This is the callback method when a sensors detects that an object has passed through.
    #Note that an old signal will be overwritten
    def sendSignal(self, pinNumber):
    #note that a timedelta is needed due to the use of two sensors
	a = self.__timestamp + datetime.timedelta(milliseconds=500)
	if datetime.datetime.now() > a:
	    print "signal callback from signal: " + str(pinNumber)

        #record the current time and create the string that will be stored into the database
	    self.__timestamp = datetime.datetime.now()
        self.__signal = Signal.initializeSignal(self.__ID, self.__Location, self.__timestamp)
        #indicate that a signal was detected
        self.setEmptyFlag(False)

    #sets the sensor to the appropriate GPIO pin. The pins are set according to the colour of bin that the sensor is placed in. Each bin has two sensors and the pins have been optimized to make cable management easier.
    def setGPIOPin(self, ID):
        if ID is "black":
            self.__gpiopin1 = 16 
            self.__gpiopin2 = 18
            return
        elif ID is "green":
            self.__gpiopin1 = 7
            self.__gpiopin2 = 11
            return
        elif ID is "blue":
            self.__gpiopin1 = 12 
            self.__gpiopin2 = 22
            return
        elif ID is "grey":
            self.__gpiopin1 = 35
            self.__gpiopin2 = 37
            return
        else:
            return 

    #sets the empty flag to the given empty variable, also used by Queue class
    def setEmptyFlag(self, empty):
        self.__isEmpty = empty
        
    #returns the empty flag, used by Queue class    
    def isEmpty(self):
        return self.__isEmpty

    def getSignal(self):
        self.setEmptyFlag(True)
        return self.__signal

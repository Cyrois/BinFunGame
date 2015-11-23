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
    __gpiopin = 7

    #set up GPIO
    def __init__(self, ID, Location):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        self.__gpiopin = self.getGPIOPin(ID)
        GPIO.setup(self.__gpiopin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        self.__ID = ID
        self.__Location = Location
        GPIO.add_event_detect(self.__gpiopin, GPIO.RISING, callback=self.testSendSignal)

    def testSendSignal(self, pinNumber):
        print "signal callback from signal: " + str(pinNumber)
        self.sendSignal()

    def getGPIOPin(self, ID):
        if ID == 1:
            return 7
        elif ID == 2:
            return 12
        elif ID == 3:
            return 16
        elif ID == 4:
            return 15
        else:
            return 0

    #wait for sensor to turn on
    def listenSignal(self):
        #if(GPIO.input(self.__gpiopin)):
        #    self.sendSignal()
        #print "WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW"
        #while True:
        #GPIO.wait_for_edge(self.__gpiopin, GPIO.RISING)
        #self.sendSignal()
        return
        
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
	
        
    # now we'll define two threaded callback functions  
    # these will run in another thread when our events are detected  
    def my_callback(channel):
        print "falling edge detected on 15"
    def my_callback2(channel):
        print "falling edge detected on 12"
    def my_callback3(channel):
        print "falling edge detected on 18"
    def my_callback4(channel):
        print "falling edge detected on 7" 
    	
    # when a falling edge is detected on port __gpiopin, regardless of whatever   
    # else is happening in the program, the function my_callback will be run
    #__init__(self, 1, "Nest")
    #GPIO.add_event_detect(19, GPIO.FALLING, callback=my_callback, bouncetime=300)
    #GPIO.add_event_detect(12, GPIO.FALLING, callback=my_callback, bouncetime=300)
    #GPIO.add_event_detect(18, GPIO.FALLING, callback=my_callback, bouncetime=300)
    #GPIO.add_event_detect(7, GPIO.FALLING, callback=my_callback, bouncetime=300)
	
    #Another example of interrupts:
    #try:  
    #   GPIO.wait_for_edge(23, GPIO.FALLING)  
    #except KeyboardInterrupt:  
    #   GPIO.cleanup()       # clean up GPIO on CTRL+C exit  
    #GPIO.cleanup()           # clean up GPIO on normal exit 

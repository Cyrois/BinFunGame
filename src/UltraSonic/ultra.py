import RPi.GPIO as GPIO
import time
import datetime
import Queue
import thread
from Signal import Signal

class Sensor:
	__isEmpty = True    #flag used by Queue to see if the Sensor is active
    __signal = ''   #the current Signal string, see Signal class for format
    __ID = ''   #the sensor ID
    __Location = '' #the location of the sensor
        
    #GPIO Input Pin for the Sensor
    __gpiopin = 7

	__trig = ''
	__echo = ''
	__base_distance = ''

    #set up GPIO
    def __init__(self, ID, Location):
		self.__ID = ID
        self.__Location = Location

		GPIO.setmode(GPIO.BCM)
		setGPIOPin(self)

		GPIO.setup(self.__trig, GPIO.OUT)
		GPIO.setup(self.__echo, GPIO.IN)
		calibrateSensor(self)

		try:
		   thread.start_new_thread( run, (self,) )
		except:
		   print "Error: unable to start thread"

	def run(self):
		while True:
			GPIO.output(self.__trig, True)
			time.sleep(0.00001)
			GPIO.output(self.__trig, False)

			while GPIO.input(self.__echo) == 0:
				pulse_start = time.time()

			while GPIO.input(self.__echo) == 1:
				pulse_end = time.time()
			
			distance = calculateDistance(pulse_start, pulse_end)

			if distance < base_distance:
			print "object detected at ", distance

			time.sleep(0.05)
		
	def calculateDistance(pulse_start, pulse_end):
		pulse_duration = pulse_end - pulse_start
		distance = pulse_duration * 17150
		distance = round(distance, 2)
		return distance
	
    def testSendSignal(self, pinNumber):
        print "signal callback from signal: " + str(pinNumber)
        self.sendSignal()

    def setGPIOPin(self):
        if self.__ID is "black":
			self.__trig = 7
			self.__echo = 11           
			return
        elif self.__ID is "green":
			self.__trig = 13
			self.__echo = 15       
			return
        elif self.__ID is "blue":
			self.__trig = 18
			self.__echo = 23           
			return
        elif self.__ID is "grey":
			self.__trig = 24
			self.__echo = 25       
			return
        else:
            return 0

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

	def calibrateSensor(self):
		print "Calibrating Sensor ", self.__ID
		print "Warming up..."
		GPIO.output(self.__trig, False)
		time.sleep(2)

		#activate the sensor with 10ms high signal
		GPIO.output(self.__trig, True) 
		time.sleep(0.00001)
		GPIO.output(self.__trig, False)
		
		#start calculating time of signal
		while GPIO.input(self.__echo) == 0:
			pulse_start = time.time()

		while GPIO.input(self.__echo) == 1:
			pulse_end = time.time()

		self.__base_distance = distance = calculateDistance(pulse_start, pulse_end)
		self.__base_distance = round(self.__base_distance)

		print "base distance is: ", self.__base_distance, " cm"
		print "Calibration Complete..."
		return	

test = Sensor("black", "Nest")	



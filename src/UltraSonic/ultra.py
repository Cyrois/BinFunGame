import RPi.GPIO as GPIO
import time
import datetime
import Queue
import thread
import threading
#from Signal import Signal

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
        self.setGPIOPin()

        GPIO.setup(self.__trig, GPIO.OUT)
        GPIO.setup(self.__echo, GPIO.IN)
        self.calibrateSensor()

        t=threading.Thread(target=self.run)
        t.daemon = True
        t.start()
        

    def run(self):
        while True:
            GPIO.output(self.__trig, True)
            time.sleep(0.01)
            GPIO.output(self.__trig, False)
            
            time1,time2 = time.time(),time.time()
            
            while GPIO.input(self.__echo) == 0:
                pulse_start = time.time()
                time2 = time.time()
                if time2 - time1 > 0.02:
                    print "breaking"
                    break
                
            
            while GPIO.input(self.__echo) == 1:
                pulse_end = time.time()
                if time2 - time1 > 0.02:
                    break
            
            distance = self.calculateDistance(pulse_start, pulse_end)

            if distance < self.__base_distance:
             #   print "object detected at ", distance
                print "object detected at ", distance, "by sensor ", self.__ID
            
            time.sleep(0.05)
        
    def calculateDistance(self, pulse_start, pulse_end):
        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance, 2)
        return distance
    
    def testSendSignal(self, pinNumber):
        print "signal callback from signal: " + str(pinNumber)
        self.sendSignal()

    def setGPIOPin(self):
        if self.__ID is "black":
            self.__trig = 4
            self.__echo = 17           
            return
        elif self.__ID is "green":
            self.__trig = 21
            self.__echo = 22       
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
        time.sleep(0.01)
        GPIO.output(self.__trig, False)
        
        #start calculating time of signal
        while GPIO.input(self.__echo) == 0:
            pulse_start = time.time()

        while GPIO.input(self.__echo) == 1:
            pulse_end = time.time()

        self.__base_distance = distance = self.calculateDistance(pulse_start, pulse_end)
        self.__base_distance = round(self.__base_distance)-1

        print "base distance is: ", self.__base_distance, " cm"
        time.sleep(2)
        print "Calibration Complete..."
        return  

#test = Sensor("black", "Nest")
test = Sensor("blue", "Nest")
#test = Sensor("green", "Nest")
#test = Sensor("grey", "Nest") 
while True:
    x="penis"


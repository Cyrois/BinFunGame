import datetime
import Queue
import RPi.GPIO as GPIO
import time
from Sensor import Sensor



def my_callback(channel):
    print "falling edge detected on 19"
    time.sleep(1)

sensor1 = Sensor(1, "Nest")
sensor2 = Sensor(2, "Nest")
sensor3 = Sensor(3, "Nest")
sensor4 = Sensor(4, "Nest")
#sensor1.GPIO.add_event_detect(getGPIOPin(1), GPIO.RISING, callback=my_callback, bouncetime=300)

while True:
    print "running"
    time.sleep(1)

import RPi.GPIO as GPIO
import datetime

class Sensor:
	"""

	"""

	#GPIO Input Pin for the Sensor
	__gpiopin = -1

	#set up GPIO
	def __init__(self, int):
		GPIO.setmode(GPIO.BOARD)
		GPIO.setwarnings(False)
		self.gpiopin = int
		GPIO.setup(self.gpiopin, GPIO.IN)

	#wait for sensor to turn on
	def listenSignal(self):
		while True:
			GPIO.wait_for_edge(self.gpiopin, GPIO.RISING)
			self.sendSignal()

	def sendSignal(self):			
		#send date, time and id
		#need to send to queue instead 
		print datetime.datetime.utcnow()
		




